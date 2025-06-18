import marimo as mo
from mohtml import div,p,a,h1,h2,h3,script,form,button,span
from pydantic import validate_call, Field, ValidationError, BaseModel
from typing import Annotated, Callable, Any
from models import ICONS


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


