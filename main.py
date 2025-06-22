import marimo

__generated_with = "0.14.0"
app = marimo.App(
    width="full",
    app_title="frfropen.ai",
    css_file="./static/output.css",
)

with app.setup:
    # Initialization code that runs before all other cells
    import marimo as mo
    from models import ICONS, ACTIVECONNECTION
    from elms import (
    connection_buttons_tuple,
    connections_sidebar_elm,
    openrouter_connection_bar,
    openrouter_provider_dropdown,
    openrouter_models_dropdown
    )

    from OpenRouter import OpenRouter


@app.cell
def _():
    active_connection_getter, active_connection_setter = mo.state(ACTIVECONNECTION.OPENROUTER)
    return active_connection_getter, active_connection_setter


@app.cell
def _(active_connection_getter):
    active_connection = active_connection_getter()
    return (active_connection,)


@app.cell
def _(active_connection, active_connection_setter):
    connection_buttons = connection_buttons_tuple(active_connection,active_connection_setter)
    return (connection_buttons,)


@app.cell
def _(connection_buttons):
    connections_sidebar = connections_sidebar_elm(connection_buttons)
    connections_sidebar
    return


if __name__ == "__main__":
    app.run()
