# pelican-alchemy

pelican-alchemy is a functional, clean, responsive theme for the [Pelican](http://getpelican.com) static site generator. It is heavily inspired by [crowsfoot](http://github.com/porterjamesj/crowsfoot) and [clean-blog](https://github.com/BlackrockDigital/startbootstrap-clean-blog), and is powered by [Bootstrap](https://github.com/twbs/bootstrap) (v3.x).

## Features

- Core Pygments [styles](http://pygments.org/demo/)
- External analytics (Google Analytics, Gauges, Piwik)
- External comments (Disqus)
- realfavicongenerator [package](http://realfavicongenerator.net/blog/new-favicon-package-less-is-more/) support
- Font icons (Font Awesome)
- No external dependencies
- No JavaScript (excl. Analytics & Comments)
- Packaged webfonts
- Simple Jinja2 templates
- `sitemap.xml` support

## Installation

First:

    $ git clone git@github.com:nairobilug/pelican-alchemy.git

Then:

Point the `THEME` variable in your pelican config to the `alchemy` folder inside the repo (`/path/to/pelican-alchemy/alchemy`).

## Settings

Unless otherwise specified, settings that refer to paths can be either absolute or relative to the configuration file.

### SITESUBTITLE

Subtitle that appears in the header:

    SITESUBTITLE = 'A magical \u2728 Pelican theme'

### SITEIMAGE

Image that appears in the header:

    SITEIMAGE = '/images/profile.png'

You can also force the image size:

    SITEIMAGE = '/images/profile.svg width=200 height=200'

### DESCRIPTION

Index `<meta name="description" content="...">`:

    DESCRIPTION = 'A functional, clean, responsive theme for Pelican. Heavily ' \
                  'inspired by crowsfoot and clean-blog, powered by Bootstrap.'

### LINKS

A list of tuples (Title, URL) for menu links:

    LINKS = (
        ('Pelican', 'http://getpelican.com/'),
        ('Python.org', 'http://python.org/'),
        ('Jinja2', 'http://jinja.pocoo.org/'),
    )

### ICONS

A list of tuples (Icon, URL) for icon links:

    ICONS = (
        ('feed', '/feeds/all.atom.xml'),
        ('github', 'https://github.com/nairobilug/pelican-alchemy'),
    )

A [Font Awesome icon](http://fontawesome.io/icons/) without the `fa-` prefix.

### PYGMENTS_STYLE

You can choose one of the built-in Pygments styles for syntax highlighting.

By default the `default` style is used:

    PYGMENTS_STYLE = 'default'

The following styles are available:

- algol
- algol_nu
- autumn
- borland
- bw
- colorful
- default
- emacs
- friendly
- fruity
- igor
- lovelace
- manni
- monokai
- murphy
- native
- paraiso-dark
- paraiso-light
- pastie
- perldoc
- rrt
- tango
- trac
- vim
- vs
- xcode

For a demo of the different styles, click [here](http://pygments.org/demo/).

### HIDE_AUTHORS

Hide the author(s) of an article - useful for single author sites:

    HIDE_AUTHORS = True

### NEW_FAVICONS

Use a [realfavicongenerator](https://realfavicongenerator.net/blog/new-favicon-package-less-is-more/) favicon package:

    NEW_FAVICONS = True

### Other Settings

    DISQUS_SITENAME = '...'
    GAUGES = '...'
    GOOGLE_ANALYTICS = '...'
    PIWIK_URL = '...'
    PIWIK_SITE_ID = '...'

An RSS icon will also appear on header if `FEED_ALL_ATOM` is set.
