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
    from elms import sidebar_item, openrouter_connection_bar, connections_sidebar_elm, connection_button_elm
    from mohtml import div,p,span,img
    from models import ICONS
    from funcs import pick_a_connection
    from OpenRouter import OpenRouter


@app.cell
def _():
    get_active_provider, set_active_provider = mo.state(None)
    return get_active_provider, set_active_provider


@app.cell
def _(get_active_provider):
    type(get_active_provider)
    return


@app.cell
def _(set_active_provider):
    type(set_active_provider)
    return


@app.cell
def _(get_active_provider):
    active_provider = get_active_provider()
    return (active_provider,)


@app.cell
def _(active_provider, get_active_provider, set_active_provider):
    buttons = \
    [
        sidebar_item(icon,on_change=lambda v, s=slug: set_active_provider(s))
        if get_active_provider() != slug
        else sidebar_item(icon,on_change=lambda v, s=slug: set_active_provider(s),active=True)
        for slug,icon in ICONS.connections_dict().items()
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
    return (buttons,)


@app.cell
def _(buttons):
    connections_sidebar_elm(sidebar_buttons=tuple(buttons))
    return


@app.cell
def _(choose_a_model):
    choose_a_model
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
def _(model_dropdown, provider_dropdown):
    mo.stop(model_dropdown.value is None)
    mo.md(
        f"""
        Provider:
        {provider_dropdown.value}\n
        Model:
        {model_dropdown.value.description}\n
        Pricing:
        {model_dropdown.value.pricing}\n
        """
    )
    return


@app.cell
def _(openrouter_data):
    provider_dropdown = mo.ui.dropdown(
        options=openrouter_data.providers_tuple,
        searchable=True,
    )
    return (provider_dropdown,)


@app.cell
def _(openrouter_data, provider_dropdown):
    picked_provider = provider_dropdown.value
    try:
        model_dropdown = mo.ui.dropdown(
            options=openrouter_data.get_models_by_a_provider_dict(picked_provider),
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
