import marimo as mo
from mohtml import div,p,a,h1,h2,h3,script,form,button,span
from pydantic import validate_call, Field, ValidationError, BaseModel, ConfigDict
from typing import Annotated, Callable, Any
from models import ICONS
from OpenRouter import OpenRouter


@validate_call
def sidebar_item(icon:ICONS,on_change:Callable[[Any],None],active:bool=False,tooltip:str=None,keyboard_shortcut:str=None)->div:
    """
    Create a discord style button
    Args:
        icon (ICONS): ICON Enum type
        on_change (Callable[[Any],None]): usually a mo.state lambda funtion
        active (bool): sets style to active, Defaults to False
        tooltip (str): hover tooltip
        keyboard_shortcut (str): keyboard shortcut like 'Ctrl+t'
    Returns:
        div (mohtml.div): a mo.ui.run_button wrapped in a div
    """
    #Sets active styling on sidebar-item div
    style = "sidebar-icon-active" if active else "sidebar-icon"

    #Checks for SVG ICONS
    if icon.value[0] == '<':
        icon = str(div(icon,span("",klass="sidebar-indicator"),klass=style)) if active else str(div(icon,klass=style))
    else:
        icon = str(div(mo.icon(icon,size=23).text,span("",klass="sidebar-indicator"),klass=style)) if active else str(div(mo.icon(icon,size=23).text,klass=style))

    return div(
        mo.ui.run_button(
            kind='neutral',
            tooltip=tooltip,
            label=icon,
            on_change=on_change,
            full_width=True,
            keyboard_shortcut=keyboard_shortcut
            ),
            klass="w-10 my-2"
        )


@validate_call(validate_return=True,config=ConfigDict(arbitrary_types_allowed=True,strict=True))
def connection_button_elm(icon:ICONS,active:bool=False,*,kwargs:dict):
    """
    Create a discord styled button to fit inside the `connections_sidebar_elm` as a `mo.vstack`.
    Args:
        icon (ICONS): ICONS StrEnum type
        active (bool): controlls the active styling on the button div. Defaults to False.
        kwargs (dict): arguments passed to the mo.ui.button()
    """
# Set active styling on sidebar-item div
    _style = "sidebar-icon-active" if active else "sidebar-icon"
# Check for SVG ICONS
    if icon.value[0] == '<':
        icon = str(div(icon,span("",klass="sidebar-indicator"),klass=_style)) if active else str(div(icon,klass=_style))
    else:
        icon = str(div(mo.icon(icon,size=23).text,span("",klass="sidebar-indicator"),klass=_style)) if active else str(div(mo.icon(icon,size=23).text,klass=_style))

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
def connection_buttons_tuple(active_connection:str|None,possible_connections:dict,connection_setter:mo._runtime.state.SetFunctor)->tuple[div,...]:
    """
    Creates a tuple of connection_button_elms, setting the active one if the slug matches the active_connection
    Args:
        active_connection (str|None): value from connection_getter()
        possible_connections (dict): ICONS.connections_dict()
        connection_setter (mo._runtime.state.SetFunctor): the setter part of a mo.state() instance. Needs to be active_connection_setter
    """
# List of connection_button_elm() while checking for the active_connection against the icon name found in ICONS.connections_dict()
    buttons = \
    [
        connection_button_elm(icon,True,kwargs={"tooltip":slug,"on_click":lambda _,s=slug:connection_setter(s)})
        if active_connection == slug
        else connection_button_elm(icon,kwargs={"tooltip":slug,"on_click":lambda _,s=slug:connection_setter(s)})
        for slug,icon in possible_connections.items()
    ]
# Tuple for immutable
    return tuple(buttons)


@validate_call(validate_return=True,config=ConfigDict(arbitrary_types_allowed=True,strict=True))
def connections_sidebar_elm(sidebar_buttons:tuple[div,...])->div:
    """
    A Discord styled sidebar for choosing a active connection.
    Args:
        active_connection (str|None): the choosen connection (ie "openai" or "anthropic")
    """
# Create a vstack from the sidebar_buttons tuple
    button_stack = mo.vstack(sidebar_buttons,align="center",justify="center")

# Create Sidebar Elm   
    return div(
        button_stack,
        klass="flex flex-col border-2 w-18 p-3 m-3 rounded-xl items-center justify-center bg-gray-900"
    )




#<--------OPENROUTER ELMS----------->
@validate_call
def openrouter_connection_bar(providers_dropdown:mo.ui.dropdown,models_dropdown:mo.ui.dropdown)->div:
    style = "flex mx-2"
    elms = [
        "Provider:",
        div(
            providers_dropdown,
            klass=style
        ),
        "Model:",
        div(
            models_dropdown,
            klass=style
        )
    ]
    return div(
        *elms,
        klass="flex bg-gray-900 w-fit justify-center items-center rounded-3xl border-2 border-solid px-5 py-1.5 m-auto"
    )


@validate_call
def openrouter_provider_dropdown(data:OpenRouter,kwargs:dict=None)->mo.ui.dropdown:
    """
    Creates a dropdown menue for OpenRouter provider picking.
    Args:
        data (OpenRouter): OpenRouter pydantic model
        kwargs (Optional[dict]): Will be passed as kwargs to mo.ui.dropdown.
    """
    return mo.ui.dropdown(options=data.providers_tuple,searchable=True) if kwargs is None else mo.ui.dropdown(options=data.providers_tuple,searchable=True,**kwargs)

@validate_call
def openrouter_models_dropdown(data:OpenRouter,active_provider:str|None,kwargs:dict=None)->mo.ui.dropdown:
    """
    Creates a dropdown menue for OpenRouter model picking.
    Args:
        data (OpenRouter): OpenRouter pydantic model
        active_provider (str|None): usually provider_dropdown.value
        kwargs (Optional[dict]): Will be passed as kwargs to mo.ui.dropdown.
    """
    if active_provider is None:
        _options = data.models_dict
        return mo.ui.dropdown(options=_options,searchable=True) if kwargs is None else mo.ui.dropdown(options=_options,searchable=True,**kwargs)
    
    elif active_provider in data.providers_tuple:
        _options = data.get_models_by_a_provider_dict(active_provider)
        return mo.ui.dropdown(options=_options,searchable=True) if kwargs is None else mo.ui.dropdown(options=_options,searchable=True,**kwargs)
    else:
        raise ValueError("Active Provider not in Providers Tuple")