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
    connections_sidebar,
    openrouter_model_picker_bar,
    openrouter_provider_dropdown,
    openrouter_models_dropdown,
    display_active_connection_ui
    )
    from OpenRouter import OpenRouter


@app.cell
def _():
    OpenRouterData = OpenRouter.model_validate(OpenRouter.get_openrouter_data())
    return (OpenRouterData,)


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
    connections_sidebar_elm = connections_sidebar(connection_buttons)
    connections_sidebar_elm
    return


@app.cell
def _(active_connection, dd):
    display_active_connection_ui(active_connection,dd)
    return


@app.cell
def _(OpenRouterData):
    openrouter_provider_dropdown_elm = openrouter_provider_dropdown(OpenRouterData)
    return (openrouter_provider_dropdown_elm,)


@app.cell
def _(OpenRouterData, openrouter_provider_dropdown_elm):
    openrouter_models_dropdown_elm = openrouter_models_dropdown(OpenRouterData,openrouter_provider_dropdown_elm.value)
    return (openrouter_models_dropdown_elm,)


@app.cell
def _(openrouter_models_dropdown_elm, openrouter_provider_dropdown_elm):
    openrouter_model_picker_bar_elm = openrouter_model_picker_bar(openrouter_provider_dropdown_elm,openrouter_models_dropdown_elm)
    return (openrouter_model_picker_bar_elm,)


@app.cell
def _(openrouter_model_picker_bar_elm):
    dd = {
        ACTIVECONNECTION.OPENROUTER:openrouter_model_picker_bar_elm
    }
    return (dd,)


if __name__ == "__main__":
    app.run()
