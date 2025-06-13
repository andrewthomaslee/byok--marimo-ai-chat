import marimo as mo
from mohtml import div,p,a,h1,h2,h3,script,form,button,span
from pydantic import validate_call, Field, ValidationError
from typing import Annotated


@validate_call
def discord_sidebar(elms:list[div])->div:
    return (
        div(*elms,
           klass="fixed top-0 left-0 h-screen w-16 flex flex-col bg-gray-900 text-white shadow-lg"
           )
    )