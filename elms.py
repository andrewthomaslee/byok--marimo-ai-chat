import marimo as mo
from mohtml import div,p,a,h1,h2,h3,script,form,button,span
from pydantic import validate_call, Field, ValidationError, BaseModel
from typing import Annotated, Callable, Any
from models import ICONS


@validate_call
def sidebar_item(icon:ICONS|str,on_change:Callable[[Any],None],active:bool=False,tooltip:str=None,keyboard_shortcut:str=None)->div:

    if active:
        style = "sidebar-icon-active"
    else:
        style = "sidebar-icon"

    if isinstance(icon,str) and active:
        icon = str(div(icon,span("",klass="sidebar-indicator"),klass=style))
    elif isinstance(icon,ICONS) and active:
        icon = str(div(mo.icon(icon,size=23).text,span("",klass="sidebar-indicator"),klass=style))
    elif isinstance(icon,str) and not active:
        icon = str(div(icon,klass=style))
    elif isinstance(icon,ICONS) and not active:
        icon = str(div(mo.icon(icon,size=23).text,klass=style))
    
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
def openrouter_logo(width:int=25,height:int=25)->str:
    text = \
        f"""
        <svg
        width="{width}"
        height="{height}"
        viewBox="0 0 512 512"
        xmlns="http://www.w3.org/2000/svg"
        fill="currentColor"
        stroke="currentColor"
        >
        <g clip-path="url(#clip0_205_3)">
            <path
            d="M3 248.945C18 248.945 76 236 106 219C136 202 136 202 198 158C276.497 102.293 332 120.945 423 120.945"
            stroke-width="90"
            />
            <path d="M511 121.5L357.25 210.268L357.25 32.7324L511 121.5Z" />
            <path
            d="M0 249C15 249 73 261.945 103 278.945C133 295.945 133 295.945 195 339.945C273.497 395.652 329 377 420 377"
            stroke-width="90"
            />
            <path d="M508 376.445L354.25 287.678L354.25 465.213L508 376.445Z" />
        </g>
        </svg>
        """
    return text