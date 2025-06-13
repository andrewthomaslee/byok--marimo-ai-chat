import marimo

__generated_with = "0.13.15"
app = marimo.App(
    width="medium",
    app_title="Widgets",
    css_file="./static/output.css",
)

with app.setup:
    # Initialization code that runs before all other cells
    #Imports
    import marimo as mo
    import anywidget
    import traitlets
    from pathlib import Path
    import models
    from mohtml import div,button
    from typing import Literal

    #Setup
    ROOT_DIR = Path(__file__).parent


@app.cell
def _():
    Discord = mo.icon(models.ICONS.DISCORD)
    return (Discord,)


@app.cell
def _(Discord):
    my_button =div(
        mo.ui.button(
            full_width=False,
            label=Discord.text,
            tooltip="This is a tooltip",
            kind="success"
        ),klass="sidebar-icon"
    )
    return (my_button,)


@app.cell
def _(Discord):
    tabs = mo.ui.tabs({
        Discord.text: mo.md("Hello, Alice! 👋"),
        "Alice says": mo.md("Hello, Bob! 👋")
    })
    tabs
    return


@app.cell
def _(my_button):
    discord = mo.icon(models.ICONS.DISCORD).text
    search = mo.icon(models.ICONS.SEARCH,size=28).text
    bu = mo.ui.button(label=mo.icon(models.ICONS.DISCORD).text)
    elms = [discord,search,bu,my_button]
    return (elms,)


@app.function
def SideBar(elms):
    return div(
        *elms,
        klass="fixed top-1/2 right-4 -translate-y-1/2 h-fit p-2 bg-gray-700/50 rounded-2xl flex flex-col backdrop-blur-sm"
    )


@app.cell
def _(elms):
    SideBar(elms)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
