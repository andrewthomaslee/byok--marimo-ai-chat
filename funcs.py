import marimo

__generated_with = "0.13.15"
app = marimo.App(width="medium")

with app.setup:
    # Initialization code that runs before all other cells
    import marimo as mo
    from pydantic import validate_call
    from models import ICONS


@app.function
@validate_call
def extract_icon_name(icon: ICONS)->str:
    """
    Extracts the icon name using string splitting.
    """
    s = icon.__repr__()
    return s.split('.')[1].split(':')[0]


if __name__ == "__main__":
    app.run()
