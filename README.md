# Web dev from the browser
**I** 💚 **<u>marimo notebooks !</u>**

[docs](https://docs.marimo.io/)  -&-  [github](https://github.com/marimo-team/marimo)

**marimo** is just a `.py` file instead of the usual notebook extension `.ipynb`. This makes it possible to version with **git** and run as normal **python🐍** files!

Editing **marimo** is done in the bowser or in an IDE. To edit a **marimo notebook** run:
```sh
marimo edit index.py
```
Or download the [**VSCode Extension**](https://marketplace.visualstudio.com/items?itemName=marimo-team.vscode-marimo)

Since your system's browser is the IDE you never have to leave that *sweet* *sweet* **HTML** bby!

Create *views* and *plots* and *routes* and *widgets* and see how they will natively look right from your browser!

Dont like browser IDE? Since **marimo** is just a `.py` file, any IDE will do.

# Why marimo + Tailwind-CLI ?
I don't want a `package.json` file and a `node_modules` directory if the only package is for TailwindCSS. Using the standalone CLI is a much cleaner **feeling**. The vibes are right with just "**marimo**🟢 + **TailwindCSS CLI**🌀 + **FastAPI**🐍"

**marimo** encourages <u>functional programming</u> for maximal reusability. I enjoy programming in **cells** rather that **files**. But it is nice to have both options with **marimo**.

I can rapidly design a marimo page from my browser and add it as a route to FastAPI in no time! The work flow is sick. Not perfect, but at the time of writing this marimo is only at version `0.13.15` and it's already this damn good!

## TailwindCSS CLI Standalone (no-npm)
To install it, grab the executable for your platform from the [latest release](https://github.com/tailwindlabs/tailwindcss/releases/latest) on GitHub, making sure to give it executable permissions:

Example for Linux-x64
```sh
curl -sLO https://github.com/tailwindlabs/tailwindcss/releases/latest/download/tailwindcss-linux-x64
chmod +x tailwindcss-linux-x64
mv tailwindcss-linux-x64 tailwindcss
```

Now you can use it just like the npm-distributed CLI tool:

TailwindCSS CLI Commands
```sh
# Start a watcher
./tailwindcss -i ./static/input.css -o ./static/output.css --watch

# Compile and minify CSS for production
./tailwindcss -i ./static/input.css -o ./static/output.css --minify
```

## Development Environment
To get started with the development environment + hot reloading:
```sh
# Install packages
uv sync

# Activate the enviroment
source .venv/bin/activate

# Use FastAPI dev
fastapi dev main.py
```

### .bash_aliases
Add these to your `.bashrc` or `.bash_aliases` file to make life easier
```sh
#TailwindCSS
alias tw-dl="curl -sLO https://github.com/tailwindlabs/tailwindcss/releases/latest/download/tailwindcss-linux-x64 && chmod +x tailwindcss-linux-x64 && mv tailwindcss-linux-x64 tailwindcss"
alias tw-init="mkdir static && touch static/input.css && echo '@import \"tailwindcss\";' >> static/input.css"
alias tw-watch="./tailwindcss -i ./static/input.css -o ./static/output.css --watch"
alias tw-minify="./tailwindcss -i ./static/input.css -o ./static/output.css --minify"
```

### useful commands
To edit a marimo notebook in browser and in IDE at the same time add these flags:
```sh
marimo edit app.py --no-token --watch
```

### VSCode intellisense inside `.py` files
Use [tailwindcss.includelanguages](https://marketplace.visualstudio.com/items?itemName=bradlc.vscode-tailwindcss#tailwindcss.includelanguages) to add auto-complete and hover inside python files.
Add this to your settings via ui or json.
```json
{
  "tailwindCSS.includeLanguages": {
    "python": "html"
  }
}
```