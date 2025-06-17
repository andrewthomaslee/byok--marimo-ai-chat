import marimo

__generated_with = "0.13.15"
app = marimo.App(width="medium", css_file="./static/output.css")

with app.setup:
    # Initialization code that runs before all other cells
    import marimo as mo
    from elms import sidebar_item
    from mohtml import div,p,span
    from models import ICONS
    from funcs import extract_icon_name
    from OpenRouter import OpenRouter


@app.cell
def _():
    get_active_provider, set_active_provider = mo.state(None)
    return get_active_provider, set_active_provider


@app.cell
def _(get_active_provider):
    active_provider = "" if get_active_provider() is None else extract_icon_name(get_active_provider())
    return (active_provider,)


@app.cell
def _(active_provider, get_active_provider, set_active_provider):
    buttons = \
    [
        sidebar_item(icon,on_change=lambda v, i=icon: set_active_provider(i))
        if get_active_provider() != icon
        else sidebar_item(icon,on_change=lambda v, i=icon: set_active_provider(i),active=True)
        for icon in ICONS.list_providers()
    ]
    bar = mo.vstack(
        buttons,
        align="center",
        justify="center"
    )

    div(
        bar,
        div(p(active_provider,klass="text-xs text-gray-500"),
        klass="flex min-w-max h-10 items-center justify-center"
        ),
        klass="flex flex-col border-2 w-18 p-3 m-3 rounded-xl items-center justify-center bg-gray-900"
    )
    return


@app.cell
def _():
    openrouter_data = OpenRouter.model_validate(OpenRouter.get_openrouter_data())
    return (openrouter_data,)


@app.cell
def _(model_dropdown, provider_dropdown):
    choose_a_model = \
    mo.md\
    (
    text=\
    f"""
    - Pick a Provider: {provider_dropdown}
    - Choose a Model: {model_dropdown}
    """
    )
    return (choose_a_model,)


@app.cell
def _(choose_a_model):
    choose_a_model
    return


@app.cell
def _(provider_dropdown):
    provider_dropdown.value
    return


@app.cell
def _(model_dropdown):
    mo.stop(model_dropdown.value is None)
    print(model_dropdown.value)
    print(model_dropdown.value.pricing)
    return


@app.cell
def _(openrouter_data):
    provider_dropdown = mo.ui.dropdown(
        options=openrouter_data.providers_set,
        searchable=True,
    )
    return (provider_dropdown,)


@app.cell
def _(openrouter_data, provider_dropdown):
    picked_provider = provider_dropdown.value
    try:
        model_dropdown = mo.ui.dropdown(
            options=openrouter_data.get_models_by_provider_dict(picked_provider),
            searchable=True,
        )
    except KeyError:
        model_dropdown = mo.ui.dropdown(
            options=openrouter_data.models_dict,
            searchable=True,
        )
    return (model_dropdown,)


if __name__ == "__main__":
    app.run()
