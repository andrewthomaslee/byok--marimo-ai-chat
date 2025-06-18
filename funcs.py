import marimo

__generated_with = "0.13.15"
app = marimo.App(width="medium")

with app.setup:
    # Initialization code that runs before all other cells
    import marimo as mo
    from pydantic import validate_call
    from models import ICONS
    from mohtml import script


@app.function
@validate_call
def extract_icon_name(icon: ICONS)->str:
    """
    Extracts the icon name using string splitting.
    """
    s = icon.__repr__()
    return s.split('.')[1].split(':')[0].casefold()


if __name__ == "__main__":
    app.run()


@app.function
@validate_call
def datastar_cdn(version:str="v1.0.0-beta.11")->script:
    return script(
        src=f"https://cdn.jsdelivr.net/gh/starfederation/datastar@{version}/bundles/datastar.js",
        integrity="sha512-TylZ8io+J3IUeE8+InEGsRUp3VJ/ZhL3Hi09H9RXZPJg5p+mYYDWhQmDpPQcXg02U99BQ50/6QvJRDi4nBGUKg==",
        crossorigin="anonymous"
    )