import marimo

__generated_with = "0.13.15"
app = marimo.App(
    width="medium",
    css_file="./static/output.css",
    html_head_file="",
)

with app.setup:
    import marimo as mo
    from mohtml import div, p, h1, bootstrap_css, h5, i, a, script,img
    from typing import Literal, Union


@app.cell
def _():
    txt = "The quick brown fox jumped over the lazy dog. 🐶"
    return (txt,)


@app.cell
def _():
    style = "text-red-800 text-shadow-cyan-500 font-extrabold text-center text-shadow-md"
    return (style,)


@app.cell
def _(style, txt):
    div(txt,klass=style)
    return


@app.cell
def _():
    my_elms = ["A","B","C","D","E"]
    return


@app.cell
def _():
    my_str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return


@app.function
def side_bar(elms:list)->div:
    return (
        div(*elms,
           klass="fixed top-0 left-0 h-screen w-16 flex flex-col bg-gray-900 text-white shadow-lg"
           )
    )


@app.cell
def _():
    my_icons = \
    {
        "error" : "material-symbols:error",
        "null" : "oui:token-null",
        "missing" : "grommet-icons:document-missing",
        "sparks" : "mingcute:ai-line",
        "discord" : "ic:baseline-discord",
        "fancy" : "file-icons:fancy",
    }
    return (my_icons,)


@app.cell
def _(my_icons):
    def fetch_icon(icon:str,klass:str="my-icon",*,kwargs:dict=None)->mo.icon:
        icon = my_icons.get(icon,my_icons["missing"])
        elm = mo.icon(icon_name=icon) if kwargs is None else mo.icon(icon_name=icon,**kwargs)
        return div(elm,klass=klass)
    return (fetch_icon,)


@app.cell
def _(fetch_icon, my_icons):
    side_icon_list = [
        fetch_icon(i,"side-bar-icon",kwargs={'size':25})
        for i in my_icons.keys()
    ]

    side_bar(side_icon_list)
    return


if __name__ == "__main__":
    app.run()
