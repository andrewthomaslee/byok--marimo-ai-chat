import marimo as mo
from mohtml import div,p,a,h1,h2,h3,script,form,button,span
from pydantic import validate_call, Field, ValidationError, BaseModel
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


@validate_call
def openrouter_connection_bar(data:OpenRouter,active_provider:str|None)->div:

    if active_provider is None:
        providers_dropdown = mo.ui.dropdown(options=data.providers_set,searchable=True)
        model_dropdown = mo.ui.dropdown(options=openrouter_data.models_dict,searchable=True)
    elif isinstance(active_provider,str):
        if active_provider not in data.providers_set:
            raise ValueError("active_provider no in providers_set")
        
        active_provider = active_provider.casefold()
        providers_dropdown = mo.ui.dropdown(options=data.providers_set,searchable=True,value=active_provider)
        model_dropdown = mo.ui.dropdown(options=data.get_models_by_a_provider_dict(active_provider),searchable=True)
    else:
        print("something wong")


    return div(*["Provider: ",providers_dropdown,"Models: ",model_dropdown],klass="flex bg-gray-900 w-fit justify-center items-center rounded-3xl border-2 border-solid px-5 py-1 m-auto")