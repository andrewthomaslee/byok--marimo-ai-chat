import marimo as mo
from mohtml import div,p,a,h1,h2,h3,script,form,button,span
from pydantic import validate_call, Field, ValidationError, BaseModel
from typing import Annotated


def discord_sidebar(elms:list[div])->div:
    return (
        div(*elms,
           klass="fixed top-0 left-0 h-screen w-16 flex flex-col bg-gray-900 text-white shadow-lg"
           )
    )

class DiscordSidebar(mo.Html):
    """
    A Discord sidebar
    """
    def __init__(self,elms:list[str]=None):
        self.elms = [] if elms is None else elms
        _text = str(div(
            *self.elms,
            klass="fixed top-0 left-0 h-screen w-16 flex flex-col bg-gray-900 text-white shadow-lg"
        ))
        super().__init__(text=_text)

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self,text:str):
        self._text = text

    def _reset_text(self):
        self._text = str(div(
            *self.elms,
            klass="fixed top-0 left-0 h-screen w-16 flex flex-col bg-gray-900 text-white shadow-lg"
        ))

    @validate_call
    def add_elm(self,elm:str):
        self.elms.append(elm)
        self._reset_text()
        return None
         

