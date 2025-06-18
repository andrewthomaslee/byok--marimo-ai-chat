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
    OPENAI = 'ri:openai-fill'
    ANTHROPIC = 'ri:anthropic-fill'
    GOOGLE = 'ri:google-fill'
    META = 'ri:meta-fill'
    XAI = 'ri:twitter-x-fill'
    NVIDIA = 'bi:nvidia'
    OLLAMA = 'simple-icons:ollama'
    BEDROCK = '''<svg fill="currentColor" fill-rule="evenodd" height="24" style="flex:none;line-height:1" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><title>Bedrock</title><path d="M13.05 15.513h3.08c.214 0 .389.177.389.394v1.82a1.704 1.704 0 011.296 1.661c0 .943-.755 1.708-1.685 1.708-.931 0-1.686-.765-1.686-1.708 0-.807.554-1.484 1.297-1.662v-1.425h-2.69v4.663a.395.395 0 01-.188.338l-2.69 1.641a.385.385 0 01-.405-.002l-4.926-3.086a.395.395 0 01-.185-.336V16.3L2.196 14.87A.395.395 0 012 14.555L2 14.528V9.406c0-.14.073-.27.192-.34l2.465-1.462V4.448c0-.129.062-.249.165-.322l.021-.014L9.77 1.058a.385.385 0 01.407 0l2.69 1.675a.395.395 0 01.185.336V7.6h3.856V5.683a1.704 1.704 0 01-1.296-1.662c0-.943.755-1.708 1.685-1.708.931 0 1.685.765 1.685 1.708 0 .807-.553 1.484-1.296 1.662v2.311a.391.391 0 01-.389.394h-4.245v1.806h6.624a1.69 1.69 0 011.64-1.313c.93 0 1.685.764 1.685 1.707 0 .943-.754 1.708-1.685 1.708a1.69 1.69 0 01-1.64-1.314H13.05v1.937h4.953l.915 1.18a1.66 1.66 0 01.84-.227c.931 0 1.685.764 1.685 1.707 0 .943-.754 1.708-1.685 1.708-.93 0-1.685-.765-1.685-1.708 0-.346.102-.668.276-.937l-.724-.935H13.05v1.806zM9.973 1.856L7.93 3.122V6.09h-.778V3.604L5.435 4.669v2.945l2.11 1.36L9.712 7.61V5.334h.778V7.83c0 .136-.07.263-.184.335L7.963 9.638v2.081l1.422 1.009-.446.646-1.406-.998-1.53 1.005-.423-.66 1.605-1.055v-1.99L5.038 8.29l-2.26 1.34v1.676l1.972-1.189.398.677-2.37 1.429V14.3l2.166 1.258 2.27-1.368.397.677-2.176 1.311V19.3l1.876 1.175 2.365-1.426.398.678-2.017 1.216 1.918 1.201 2.298-1.403v-5.78l-4.758 2.893-.4-.675 5.158-3.136V3.289L9.972 1.856zM16.13 18.47a.913.913 0 00-.908.92c0 .507.406.918.908.918a.913.913 0 00.907-.919.913.913 0 00-.907-.92zm3.63-3.81a.913.913 0 00-.908.92c0 .508.406.92.907.92a.913.913 0 00.908-.92.913.913 0 00-.908-.92zm1.555-4.99a.913.913 0 00-.908.92c0 .507.407.918.908.918a.913.913 0 00.907-.919.913.913 0 00-.907-.92zM17.296 3.1a.913.913 0 00-.907.92c0 .508.406.92.907.92a.913.913 0 00.908-.92.913.913 0 00-.908-.92z"></path></svg>'''
    OPENROUTER = '''<svg width="22" height="22" viewBox="0 0 512 512" xmlns="http://www.w3.org/2000/svg" fill="currentColor" stroke="currentColor"><g clip-path="url(#clip0_205_3)"><path d="M3 248.945C18 248.945 76 236 106 219C136 202 136 202 198 158C276.497 102.293 332 120.945 423 120.945" stroke-width="90"/><path d="M511 121.5L357.25 210.268L357.25 32.7324L511 121.5Z" /><path d="M0 249C15 249 73 261.945 103 278.945C133 295.945 133 295.945 195 339.945C273.497 395.652 329 377 420 377" stroke-width="90"/><path d="M508 376.445L354.25 287.678L354.25 465.213L508 376.445Z" /></g></svg>'''
    AWS = 'bxl:aws'

    def __str__(self):
        # This makes print(ICONS.DISCORD) show the string value directly
        return self.value

    @classmethod
    def list(self):
        return self._member_names_

    @classmethod
    def dict(self):
        return self._member_map_

    @classmethod
    def show_all_icons(self, style:str="text-xl m-auto p-auto")->mo.vstack:
        """
        Displays all enum icons in a mo.vstack object
        """
        stack=list()
        for name,icon in self.dict().items():
            if icon.value[0] == '<':
                pair = div(*[name," : ",icon],klass="flex inline"+style)
            else:
                pair = div(*[name," - ",mo.icon(icon)],klass=style)
            stack.append(pair)

        return mo.vstack(stack)
    
    @classmethod
    def providers_dict(self)->dict:
        """
        A tuple of available provider icons
        """
        return {
            "OpenAI":self.OPENAI,
            "Anthropic":self.ANTHROPIC,
            "Google":self.GOOGLE,
            "Meta-llama":self.META,
            "X-AI":self.XAI,
            "Nvidia":self.NVIDIA,
            "Ollama":self.OLLAMA,
        }
    
    @classmethod
    def connections_dict(self)->dict:
        """
        A tuple of available connection icons
        """
        return {
            "OpenRouter":self.OPENROUTER,
            "OpenAI":self.OPENAI,
            "Anthropic":self.ANTHROPIC,
            "Google":self.GOOGLE,
            "X-AI":self.XAI,
            "Bedrock":self.BEDROCK,
        }

    @classmethod
    def _OPENROUTER(self,size:int|str=23)->str:
        """
        OpenRouter logo svg with sizing options
        Args:
            size (int|str): size of icon
        """
        text = \
            f"""
            <svg
            width="{size}"
            height="{size}"
            viewBox="0 0 512 512"
            xmlns="http://www.w3.org/2000/svg"
            fill="currentColor"
            stroke="currentColor"
            >
            <g clip-path="url(#clip0_205_3)">
                <path
                d="M3 248.945C18 248.945 76 236 106 219C136 202 136 202 198 158C276.497 102.293 332 120.945 423 120.945"
                stroke-width="90"
                />
                <path d="M511 121.5L357.25 210.268L357.25 32.7324L511 121.5Z" />
                <path
                d="M0 249C15 249 73 261.945 103 278.945C133 295.945 133 295.945 195 339.945C273.497 395.652 329 377 420 377"
                stroke-width="90"
                />
                <path d="M508 376.445L354.25 287.678L354.25 465.213L508 376.445Z" />
            </g>
            </svg>
            """
        return text
    
    @classmethod
    def _BEDROCK(self,size:int|str=23)->str:
        """
        Amazon Bedrock logo svg with sizing options
        Args:
            size (int|str): size of icon
        """
        text = f'''<svg fill="currentColor" fill-rule="evenodd" height="{size}" style="flex:none;line-height:1" viewBox="0 0 24 24" width="{size}" xmlns="http://www.w3.org/2000/svg"><title>Bedrock</title><path d="M13.05 15.513h3.08c.214 0 .389.177.389.394v1.82a1.704 1.704 0 011.296 1.661c0 .943-.755 1.708-1.685 1.708-.931 0-1.686-.765-1.686-1.708 0-.807.554-1.484 1.297-1.662v-1.425h-2.69v4.663a.395.395 0 01-.188.338l-2.69 1.641a.385.385 0 01-.405-.002l-4.926-3.086a.395.395 0 01-.185-.336V16.3L2.196 14.87A.395.395 0 012 14.555L2 14.528V9.406c0-.14.073-.27.192-.34l2.465-1.462V4.448c0-.129.062-.249.165-.322l.021-.014L9.77 1.058a.385.385 0 01.407 0l2.69 1.675a.395.395 0 01.185.336V7.6h3.856V5.683a1.704 1.704 0 01-1.296-1.662c0-.943.755-1.708 1.685-1.708.931 0 1.685.765 1.685 1.708 0 .807-.553 1.484-1.296 1.662v2.311a.391.391 0 01-.389.394h-4.245v1.806h6.624a1.69 1.69 0 011.64-1.313c.93 0 1.685.764 1.685 1.707 0 .943-.754 1.708-1.685 1.708a1.69 1.69 0 01-1.64-1.314H13.05v1.937h4.953l.915 1.18a1.66 1.66 0 01.84-.227c.931 0 1.685.764 1.685 1.707 0 .943-.754 1.708-1.685 1.708-.93 0-1.685-.765-1.685-1.708 0-.346.102-.668.276-.937l-.724-.935H13.05v1.806zM9.973 1.856L7.93 3.122V6.09h-.778V3.604L5.435 4.669v2.945l2.11 1.36L9.712 7.61V5.334h.778V7.83c0 .136-.07.263-.184.335L7.963 9.638v2.081l1.422 1.009-.446.646-1.406-.998-1.53 1.005-.423-.66 1.605-1.055v-1.99L5.038 8.29l-2.26 1.34v1.676l1.972-1.189.398.677-2.37 1.429V14.3l2.166 1.258 2.27-1.368.397.677-2.176 1.311V19.3l1.876 1.175 2.365-1.426.398.678-2.017 1.216 1.918 1.201 2.298-1.403v-5.78l-4.758 2.893-.4-.675 5.158-3.136V3.289L9.972 1.856zM16.13 18.47a.913.913 0 00-.908.92c0 .507.406.918.908.918a.913.913 0 00.907-.919.913.913 0 00-.907-.92zm3.63-3.81a.913.913 0 00-.908.92c0 .508.406.92.907.92a.913.913 0 00.908-.92.913.913 0 00-.908-.92zm1.555-4.99a.913.913 0 00-.908.92c0 .507.407.918.908.918a.913.913 0 00.907-.919.913.913 0 00-.907-.92zM17.296 3.1a.913.913 0 00-.907.92c0 .508.406.92.907.92a.913.913 0 00.908-.92.913.913 0 00-.908-.92z"></path></svg>'''
        return text

@app.cell
def _():
    ICONS.show_all_icons()
    return


if __name__ == "__main__":
    app.run()
