import marimo

__generated_with = "0.13.15"
app = marimo.App(width="medium")

with app.setup:
    # Initialization code that runs before all other cells
    import marimo as mo
    from elms import discord_sidebar
    from mohtml import div


@app.cell
def _():
    my_elm = \
    """<div class="fixed top-0 left-0 h-screen w-16 flex flex-col bg-gray-900 text-white shadow-lg">
    <p>Hello World</p>
    </div>
    """
    return (my_elm,)


@app.cell
def _(my_elm):
    mo.Html(my_elm)
    return


if __name__ == "__main__":
    app.run()