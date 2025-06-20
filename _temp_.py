import marimo

__generated_with = "0.14.0"
app = marimo.App(width="medium", app_title="", css_file="./static/output.css")

with app.setup:
    # Initialization code that runs before all other cells
    import marimo as mo
    from mohtml import div,span,script,p
    from OpenRouter import OpenRouter
    from elms import openrouter_connection_bar,openrouter_provider_dropdown,openrouter_models_dropdown, connection_button_elm, connection_buttons_tuple, connections_sidebar_elm
    from models import ICONS


@app.cell
def _():
    data = OpenRouter.model_validate(OpenRouter.get_openrouter_data())
    return (data,)


@app.cell
def _(data):
    try:
        provider_picker = openrouter_provider_dropdown(data)
    except Exception:
        pass
    return (provider_picker,)


@app.cell
def _(data, provider_picker):
    models_picker = openrouter_models_dropdown(data,provider_picker.value)
    return (models_picker,)


@app.cell
def _(models_picker, provider_picker):
    openrouter_connection_bar(provider_picker,models_picker)
    return


@app.cell
def _(models_picker):
    models_picker.value
    return


@app.cell
def _(data):
    data.models_tuple
    return


@app.cell
def _():
    button = connection_button_elm(ICONS.DISCORD,kwargs={"on_change":lambda _:print("Hello"),"on_click":lambda _:print("Goodbye")})
    return (button,)


@app.function
def run_this(_):
    print("this ran")


@app.cell
def _(button):
    button
    return


@app.cell
def _():
    getter,setter=mo.state(None)
    return getter, setter


@app.cell
def _():
    ICONS.connections_dict()
    return


@app.cell
def _(active_connection, setter):
    button_tuple = connection_buttons_tuple(active_connection,ICONS.connections_dict(),setter)
    return (button_tuple,)


@app.cell
def _(button_tuple):
    connections_sidebar_elm(button_tuple)
    return


@app.cell
def _(getter):
    getter()
    return


@app.cell
def _(getter):
    active_connection = getter()
    return (active_connection,)


@app.cell
def _(button_tuple):
    button_stack = mo.vstack(button_tuple,align="center",justify="center")
    button_stack
    return


if __name__ == "__main__":
    app.run()
