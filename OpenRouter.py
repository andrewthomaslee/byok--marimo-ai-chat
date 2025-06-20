import requests
from functools import lru_cache
from pydantic import BaseModel, ConfigDict, Field, field_validator, ValidationError, computed_field
from collections import defaultdict


class Architecture(BaseModel):
    model_config = ConfigDict(frozen=True)

    input_modalities: tuple[str,...] = Field(description="Supported input types")
    output_modalities: tuple[str,...] = Field(description="Supported output types")
    tokenizer: str = Field(description="Tokenization method used")
    instruct_type: str | None = Field(description="instruct_type")


class Pricing(BaseModel):
    model_config = ConfigDict(frozen=True)

    prompt: float | None = Field(default=None,description="Cost per input token")
    completion: float | None = Field(default=None,description="Cost per output token")
    request: float | None = Field(default=None,description="Fixed cost per API request")
    image: float | None = Field(default=None,description="Cost per image input")
    web_search: float | None = Field(default=None,description="Cost per web search operation")
    internal_reasoning: float | None = Field(default=None,description="Cost for internal reasoning tokens")
    input_cache_read: float | None = Field(default=None,description="Cost per cached input token read")
    input_cache_write: float | None = Field(default=None,description="Cost per cached input token write")


class TopProvider(BaseModel):
    model_config = ConfigDict(frozen=True)

    context_length: int | None = Field(description="Provider-specific context limit")
    max_completion_tokens: int | None = Field(description="Maximum tokens in response")
    is_moderated: bool = Field(description="Whether content moderation is applied")


class OpenRouterModel(BaseModel):
    model_config = ConfigDict(frozen=True)

    id_: str = Field(alias="id",description="Unique model identifier used in API requests")
    canonical_slug:  str = Field(description="Permanent slug for the model that never changes")
    name: str = Field(description="Human-readable display name for the model")
    created: int = Field(description="Unix timestamp of when the model was added to OpenRouter")
    description: str = Field(description="Detailed description of the model’s capabilities and characteristics")
    context_length: int = Field(description="Maximum context window size in tokens")
    architecture : Architecture
    pricing : Pricing
    top_provider : TopProvider
    per_request_limits: int | None = Field(description="Rate limiting information (null if no limits)")
    supported_parameters: tuple[str,...] = Field(description="Array of supported API parameters for this model")


class OpenRouter(BaseModel):
    '''
    Pydantic model to consume the OpenRouter /models API.
    '''
    model_config = ConfigDict(frozen=True)

    data: tuple[OpenRouterModel,...] = Field(description="List of available models")

    @classmethod
    def get_openrouter_data(self,headers:dict=None):
        """
        List available models (GET /models)
        """
        _headers = {} if headers is None else headers
        try:
            response = requests.get(
            "https://openrouter.ai/api/v1/models",
            headers=_headers,
            )
            response.raise_for_status()
            return response.json()
# Catch OpenRouter connection issues
        except requests.RequestException as e:
            print(f"An error occurred while fetching data from OpenRouter:\n{e}")
            raise

        
    
    @property
    def base_url(self):
        return "https://openrouter.ai/api/v1/"

    
    @computed_field
    @property
    def providers_and_models_dict(self)->dict:
        """
        A dict where keys are provider slug and values are `OpenRouterModel` pydantic models stored in a tuple
        """
        result = defaultdict(list)
        for model in self.data:
# Seperate Provider/Slug from id
            provider = model.id_.split("/")[0].casefold()
# Append every model that belongs to a certain provider
            result[provider].append(model)
# Make model list immutable
        result = {
            k:tuple(v)
            for k,v in result.items()
        }
# Sorting by key 
        return dict(sorted(result.items()))



    @lru_cache(maxsize=16)
    def get_models_by_a_provider_dict(self,provider:str)->dict:
        """
        Get a dict where keys are `model slug` and values are `OpenRouterModel` pydantic model
        Args:
            provider (str): A string for provider, must be in providers_and_models_dict.keys() to pass
        """
# Catch KeyError for provider not being in providers_and_models_dict.keys()
        try:
            _models = self.providers_and_models_dict[provider]
        except KeyError:
            raise KeyError("Provider not in providers_and_models_dict.keys()")
# Make a dict of `model slug` : `OpenRouterModel` pydantic model
        result = {
            model.id_.split("/")[1].casefold() : model
            for model in _models
        }
# Sort by keys
        return dict(sorted(result.items(),reverse=True))

    @computed_field
    @property
    def models_dict(self)->dict:
        """
        Dict of `model id` : `OpenRouterModel` pydantic model
        """
        result = {
            model.id_.casefold(): model
            for model in self.data
        }
# Sort by keys
        return dict(sorted(result.items()))
    
    @computed_field
    @property
    def models_tuple(self)->tuple:
        """
        Tuple of all models
        """
        _models = [
            model.id_.casefold()
            for model in self.data
        ]
# Sort by keys
        return tuple(sorted(_models))
    
    @computed_field
    @property
    def providers_tuple(self)->tuple:
        """
        Tuple of all unique providers
        """
        _set = {
            model.id_.split("/",1)[0].casefold()
            for model in self.data
        }
# Sort by keys
        return tuple(sorted(list(_set)))




def test_no_validation_errors():
    """
    Check that Pydantic model has no validation errors
    """
    assert OpenRouter.model_validate(OpenRouter.get_openrouter_data())
    pass

if __name__ == '__main__':
    test_no_validation_errors()
