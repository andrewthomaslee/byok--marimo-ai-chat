import requests
from pydantic import BaseModel, ConfigDict, Field, field_validator, ValidationError


class Architecture(BaseModel):
    model_config = ConfigDict()

    input_modalities: list[str] = Field(description="Supported input types")
    output_modalities: list[str] = Field(description="Supported output types")
    tokenizer: str = Field(description="Tokenization method used")
    instruct_type: str | None = Field(description="instruct_type")


class Pricing(BaseModel):
    model_config = ConfigDict()

    prompt: float | None = Field(default=None,description="Cost per input token")
    completion: float | None = Field(default=None,description="Cost per output token")
    request: float | None = Field(default=None,description="Fixed cost per API request")
    image: float | None = Field(default=None,description="Cost per image input")
    web_search: float | None = Field(default=None,description="Cost per web search operation")
    internal_reasoning: float | None = Field(default=None,description="Cost for internal reasoning tokens")
    input_cache_read: float | None = Field(default=None,description="Cost per cached input token read")
    input_cache_write: float | None = Field(default=None,description="Cost per cached input token write")


class TopProvider(BaseModel):
    model_config = ConfigDict()

    context_length: int | None = Field(description="Provider-specific context limit")
    max_completion_tokens: int | None = Field(description="Maximum tokens in response")
    is_moderated: bool = Field(description="Whether content moderation is applied")


class OpenRouterModel(BaseModel):
    # model_config = ConfigDict()

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
    supported_parameters: list[str] = Field(description="Array of supported API parameters for this model")


class OpenRouterData(BaseModel):
    model_config = ConfigDict()

    data: list[OpenRouterModel] = Field(description="List of available models")

    @classmethod
    def get_openrouter_data(self,headers:dict=None):
        """
        List available models (GET /models)
        """
        _headers = {} if headers is None else headers
        response = requests.get(
          "https://openrouter.ai/api/v1/models",
          headers=_headers,
        )
        response.raise_for_status()

        return response.json()




def test_no_validation_errors():
    assert OpenRouterData.model_validate(OpenRouterData.get_openrouter_data())
    pass

if __name__ == '__main__':
    test_no_validation_errors()