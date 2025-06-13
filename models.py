import marimo

__generated_with = "0.13.15"
app = marimo.App(width="medium", css_file="./static/output.css")

with app.setup:
    # Initialization code that runs before all other cells
    import marimo as mo
    from mohtml import div
    from enum import Enum
    from pydantic import BaseModel, ConfigDict, Field, field_validator, ValidationError


@app.class_definition
class ICONS(Enum):
    """
    An enumeration of icon identifiers.
    Each member is a string and can be used directly.
    """
    # Use ALL_CAPS for member names by convention
    DISCORD = 'ic:baseline-discord'
    HOME = 'material-symbols:home-rounded'
    SETTINGS = 'ic:baseline-settings'
    SPARKLE = 'mingcute:ai-line'
    GEMINI = 'material-icon-theme:gemini-ai'
    FILE_UP = 'lucide:file-up'
    FILE = 'akar-icons:file'
    PLUS = 'entypo:plus'
    DOTS = 'tabler:dots'
    SEARCH = 'radix-icons:magnifying-glass'
    ARROW_UP = 'eva:arrow-up-fill'
    ARROW_DOWN = 'eva:arrow-down-fill'
    ARROW_LEFT = 'eva:arrow-left-fill'
    ARROW_RIGHT = 'eva:arrow-right-fill'
    CONTROLS = 'oui:controls-horizontal'
    NOTE_PIN_FILLED = 'fluent:note-pin-20-filled'
    NOTE_PIN_EMPTY = 'fluent:note-pin-20-regular'
    PIN_FILLED = 'fluent:pin-32-filled'
    PIN_EMPTY = 'fluent:pin-32-regular'
    COPY_FILLED = 'si:copy-duotone'
    COPY_EMPTY = 'si:copy-line'
    COLLAPSE = 'gravity-ui:chevrons-collapse-vertical'
    EXPAND = 'gravity-ui:chevrons-expand-vertical'
    FULLSCREEN = 'majesticons:arrows-expand-full'
    EXIT_FULLSCREEN = 'majesticons:arrows-collapse-full'
    REDO = 'pepicons-pop:arrows-spin'
    SHARE_EMPTY = 'basil:share-outline'
    SHARE_FILLED = 'basil:share-solid'
    GITHUB = 'mingcute:github-fill'
    SAVE = 'fluent:save-32-filled'
    TRASH_EMPTY = 'mingcute:delete-line'
    TRASH_FILLED = 'mingcute:delete-fill'
    LOADING = 'svg-spinners:gooey-balls-2'
    SPINNING = 'svg-spinners:ring-resize'
    DOTS_BOUNCE = 'svg-spinners:3-dots-bounce'
    COFFEE_HALF = 'line-md:coffee-half-empty-twotone-loop'
    COFFEE_FULL = 'line-md:coffee-twotone-loop'
    SUN = 'line-md:sunny-filled'
    MOON = 'line-md:moon-simple-twotone'

    def __str__(self):
        # This makes print(Icon.DISCORD) show the string value directly
        return self.value

    @classmethod
    def list(self):
        return self._member_names_

    @classmethod
    def dict(self):
        return self._member_map_

    @classmethod
    def show_all_icons(self, style:str="text-xl m-auto p-auto" ):
        stack=list()
        for name,icon in self.dict().items():
            pair = div(*[name," - ",mo.icon(icon)],klass=style)
            stack.append(pair)

        return mo.vstack(stack)


@app.cell
def _():
    ICONS.show_all_icons()
    return


if __name__ == "__main__":
    app.run()
