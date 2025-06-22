import marimo

__generated_with = "0.14.0"
app = marimo.App(width="medium", app_title="", css_file="./static/output.css")

with app.setup:
    # Initialization code that runs before all other cells
    import marimo as mo
    from mohtml import div,span,script,p
    from OpenRouter import OpenRouter
    from elms import connections_sidebar_elm, connection_button_elm, connection_buttons_tuple
    from models import ICONS,ACTIVECONNECTION


@app.cell
def _():
    # data = OpenRouter.model_validate(OpenRouter.get_openrouter_data())
    return


@app.cell
def _(getter):
    active_connection = getter()
    return (active_connection,)


@app.cell
def _(active_connection, setter):
    buttons = connection_buttons_tuple(active_connection,setter)
    return (buttons,)


@app.cell
def _():
    getter,setter = mo.state(ACTIVECONNECTION.OPENROUTER)
    return getter, setter


@app.cell
def _(buttons):
    bar = connections_sidebar_elm(buttons)
    return (bar,)


@app.cell
def _(bar):
    bar
    return


if __name__ == "__main__":
    app.run()
