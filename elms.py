import marimo as mo
from mohtml import div,p,a,h1,h2,h3,script,form,button,span
from pydantic import validate_call, Field, ValidationError, BaseModel
from typing import Annotated, Callable, Any
from models import ICONS


@validate_call
def sidebar_item(icon:ICONS,on_change:Callable[[Any],None],active:bool=False,tooltip:str=None)->div:

    if active:
        style = "sidebar-icon-active"
    else:
        style = "sidebar-icon"
        
    icon = str(div(mo.icon(icon,size=23).text,klass=style))
    
    return div(
        mo.ui.run_button(
            kind='neutral',
            tooltip=tooltip,
            label=icon,
            on_change=on_change,
            full_width=True,
            keyboard_shortcut=None
            ),
            klass="w-10 my-2"
        )