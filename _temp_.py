import marimo

__generated_with = "0.14.0"
app = marimo.App(width="medium", app_title="", css_file="./static/output.css")

with app.setup:
    # Initialization code that runs before all other cells
    import marimo as mo
    from mohtml import div,span,script,p
    from OpenRouter import OpenRouter
    from elms import openrouter_connection_bar


@app.cell
def _():
    data = OpenRouter.model_validate(OpenRouter.get_openrouter_data())
    return (data,)


@app.cell
def _(data):
    data.base_url
    return


@app.cell
def _():
    div(
        "test",
        klass="flex bg-gray-900 w-fit justify-center items-center rounded-3xl border-2 border-solid px-5 py-1 m-auto"
    )
    return


@app.cell
def _(data):
    data.providers_tuple
    return


if __name__ == "__main__":
    app.run()
