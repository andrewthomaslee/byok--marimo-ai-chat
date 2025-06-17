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


@app.cell
def _():
    get_active_provider, set_active_provider = mo.state(None)
    return get_active_provider, set_active_provider


@app.cell
def _(get_active_provider):
    active_provider = "" if get_active_provider() is None else extract_icon_name(get_active_provider()).lower().title()
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


if __name__ == "__main__":
    app.run()
