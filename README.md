# pelican-alchemy

pelican-alchemy demo website!

## Fork / Clone the repo

If you haven't already, clone this repo (or your version of it), and:

    $ git submodule init
    $ git submodule update

Makefile provides a recipe to do the exact same thing: `make submodule`

## Generate the website

All dependencies are intalled automatically when you invoke Pelican via
Makefile recipes. New virtual environment is automatically created in `.venv`
directory.

To build demo pages execute:

    $ make html

This takes the Markdown files from the `content/` directory and generates static HTML pages inside the `output/` directory.

## Preview the website

You can serve the generated site so it can be previewed in your browser:

    $ make serve


## Publish updated demo to GitHub pages

The process is completely automated via Makefile recipe:

    $ make github

Required tools will be installed into `.venv` if missing.
