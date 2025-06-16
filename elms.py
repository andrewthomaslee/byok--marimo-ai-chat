import marimo as mo
from mohtml import div,p,a,h1,h2,h3,script,form,button,span
from pydantic import validate_call, Field, ValidationError, BaseModel
from typing import Annotated, Callable, Any
from models import ICONS



def discord_sidebar(elms:list)->div:
    return (
        div(mo.vstack(elms),
           klass="fixed top-0 left-0 h-screen w-16 flex flex-col bg-gray-900 text-white shadow-lg"
           )
    )


@validate_call
def sidebar_item(icon:ICONS,tooltip:str=None,on_change:Callable=None,func:Callable=None)->div:

    icon = str(div(mo.icon(icon).text,klass="sidebar-icon"))
    
    return div(
        div(
        mo.ui.button(
            on_click=func,
            value=None,
            kind='neutral',
            tooltip=tooltip,
            label=icon,
            on_change=on_change,
            full_width=True,
            keyboard_shortcut=None
            ),
            klass="max-w-0.5 max-h-0.5"
        ),
        klass="w-12 h-12"
    )