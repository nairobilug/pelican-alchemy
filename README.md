# pelican-alchemy

pelican-alchemy demo website!

## Fork / Clone the repo

If you haven't already, clone this repo (or your version of it), and:

    $ git submodule init
    $ git submodule update

## Install Pelican & friends

Use `pip` to install the list of dependencies (including Pelican) into your virtual environment:

    $ pip install -r requirements.txt

## Generate the website

Now that the dependencies exists, we can build:

    $ make html

This takes the Markdown files from the `content/` directory and generates static HTML pages inside the `output/` directory.

## Preview the website

You can serve the generated site so it can be previewed in your browser:

    $ make serve
