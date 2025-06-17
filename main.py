import marimo

__generated_with = "0.13.15"
app = marimo.App(width="medium", css_file="./static/output.css")

with app.setup:
    # Initialization code that runs before all other cells
    import marimo as mo
    from elms import discord_sidebar,sidebar_item
    from mohtml import div
    from models import ICONS
    import time


@app.function
def output_test(_):
    print(time.time())


@app.cell
def _():
    get_state, set_state = mo.state(None)
    buttons = \
    [
        sidebar_item(i,on_change=lambda v, i=i: set_state(i))
        for i in ICONS.list_providers()
    ]
    bar = mo.vstack(
        buttons,
        align="center",
    )
    return bar, get_state


@app.cell
def _(get_state):
    get_state()
    return


@app.cell
def _():
    ICONS.list_providers()
    return


@app.cell
def _(bar):
    div(
        bar,
        klass="fixed right-0 top-1/2 -translate-y-1/2 flex flex-col items-center gap-4 py-4 px-3 bg-gray-900 shadow-lg rounded-l-xl w-auto h-auto overflow-visible z-50 transition-all duration-300"
    )
    return


@app.cell
def _(bar):
    bar
    return


if __name__ == "__main__":
    app.run()
