import marimo as mo
from mohtml import div,p,a,h1,h2,h3,script,form,button,span
from pydantic import validate_call, Field, ValidationError, BaseModel, ConfigDict
from typing import Annotated, Callable, Any
from models import ACTIVECONNECTION
from OpenRouter import OpenRouter


@validate_call(validate_return=True,config=ConfigDict(arbitrary_types_allowed=True,strict=True))
def connection_button(icon: div,active:bool=False,*,kwargs:dict):
    """
    Create a discord styled button to fit inside the `connections_sidebar_elm` as a `mo.vstack`.
    Args:
        icon (div): mohtml.div object
        active (bool): controlls the active styling on the button div. Defaults to False.
        kwargs (dict): arguments passed to the mo.ui.button()
    """
    # Set active styling on sidebar-item div
    _style = "sidebar-icon-active" if active else "sidebar-icon"

    # Create a string which is valid HTML holding the icon and checks if active indicator style should be applied
    icon = str(div(icon,span("",klass="sidebar-indicator"),klass=_style)) if active else str(div(icon,klass=_style))

    # Create div to hold the `mo.ui.button` where the `label` obvisactes the button underneath
    return div(
        mo.ui.button(
            label=icon,
            full_width=True,
            **kwargs
            ),
            klass="w-10 my-2"
        )


@validate_call(validate_return=True,config=ConfigDict(arbitrary_types_allowed=True,strict=True))
def connection_buttons_tuple(active_connection:ACTIVECONNECTION,connection_setter:mo._runtime.state.SetFunctor)->tuple[div,...]:
    """
    Creates a tuple of connection_button_elms, setting the active one if the slug matches the active_connection
    Args:
        active_connection (ACTIVECONNECTION): ACTIVECONNECTION StrEnum value
        connection_setter (mo._runtime.state.SetFunctor): the setter part of a mo.state() instance. Needs to be active_connection_setter
    """
    # List of connection_button_elm() while checking for the active_connection against the icon name found in ICONS.connections_dict()
    buttons = \
    [
        connection_button(member.icon(),True,kwargs={"tooltip":member.value,"on_click":lambda _,m=member:connection_setter(m)})
        if active_connection is member
        else connection_button(member.icon(),kwargs={"tooltip":member.value,"on_click":lambda _,m=member:connection_setter(m)})
        for member in ACTIVECONNECTION
    ]
    # Tuple for immutable
    return tuple(buttons)


@validate_call(validate_return=True,config=ConfigDict(arbitrary_types_allowed=True,strict=True))
def connections_sidebar(sidebar_buttons:tuple[div,...])->div:
    """
    A Discord styled sidebar for choosing a active connection.
    Args:
        sidebar_buttons (tuple[div,...]): A tuple made from the function connection_buttons_tuple()
    """
    # Create a vstack from the sidebar_buttons tuple
    button_stack = mo.vstack(sidebar_buttons,align="center",justify="center")

    # Create Sidebar Elm   
    return div(
        button_stack,
        klass="flex flex-col border-2 w-18 p-3 m-3 rounded-xl items-center justify-center bg-gray-900"
    )


@validate_call(validate_return=True,config=ConfigDict(arbitrary_types_allowed=True,strict=True))
def display_active_connection_ui(active_connection:ACTIVECONNECTION,elms_dict:dict)->div:

    match active_connection:
        case ACTIVECONNECTION.OPENROUTER:
            return elms_dict[ACTIVECONNECTION.OPENROUTER]
        case ACTIVECONNECTION.OPENAI:
            return div("OpenAI")
        case ACTIVECONNECTION.ANTHROPIC:
            return div("Anthropic")
        case ACTIVECONNECTION.GOOGLE:
            return div("Google")
        case ACTIVECONNECTION.XAI:
            return div("X-AI")
        case ACTIVECONNECTION.BEDROCK:
            return div("Bedrock")
        case _:
            return div("")

    return None

#<--------OPENROUTER ELMS----------->
@validate_call(validate_return=True,config=ConfigDict(arbitrary_types_allowed=True,strict=True))
def openrouter_model_picker_bar(providers_dropdown:mo.ui.dropdown,models_dropdown:mo.ui.dropdown)->div:
    style = "flex text-gray-400 max-w-fit max-h-fit"
    elms = mo.vstack([
        mo.hstack([
            div("Provider",
                klass=style
            ),
            providers_dropdown
        ]),
        mo.hstack([
            div("Model",
                klass=style
            ),
            models_dropdown
        ])
    ])
    return div(
        elms,
        klass="flex flex-col bg-gray-900 w-fit justify-center items-start rounded-xl border-2 border-solid px-1.5 py-1.5 h-fit ml-2"
    )


@validate_call(validate_return=True,config=ConfigDict(arbitrary_types_allowed=True,strict=True))
def openrouter_provider_dropdown(data:OpenRouter,**kwargs:Any)->mo.ui.dropdown:
    """
    Creates a dropdown menue for OpenRouter provider picking.
    Args:
        data (OpenRouter): OpenRouter pydantic model
        kwargs (Optional[dict]): Will be passed as kwargs to mo.ui.dropdown.
    """
    return mo.ui.dropdown(options=data.providers_tuple,searchable=True,**kwargs)

@validate_call(validate_return=True,config=ConfigDict(arbitrary_types_allowed=True,strict=True))
def openrouter_models_dropdown(data:OpenRouter,active_provider:str|None,**kwargs)->mo.ui.dropdown:
    """
    Creates a dropdown menue for OpenRouter model picking.
    Args:
        data (OpenRouter): OpenRouter pydantic model
        active_provider (str|None): usually provider_dropdown.value
        kwargs (Optional[dict]): Will be passed as kwargs to mo.ui.dropdown.
    """
    if active_provider is None:
        _options = data.models_dict
        return mo.ui.dropdown(options=_options,searchable=True,**kwargs)
    
    elif active_provider in data.providers_tuple:
        _options = data.get_models_by_a_provider_dict(active_provider)
        return mo.ui.dropdown(options=_options,searchable=True,**kwargs)
    else:
        raise ValueError("Active Provider not in Providers Tuple")