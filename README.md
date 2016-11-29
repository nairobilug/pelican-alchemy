# pelican-alchemy

Alchemy ✨ is a functional, clean, responsive theme for the [Pelican](http://getpelican.com) static site generator. It is heavily inspired by [crowsfoot](http://github.com/porterjamesj/crowsfoot) and [clean-blog](https://github.com/BlackrockDigital/startbootstrap-clean-blog), and is powered by [Bootstrap](https://github.com/twbs/bootstrap) (v3.x).

[Demo](https://rwanyoike.github.io/pelican-alchemy/)!

## Screenshot

![Screenshot](screenshot.jpg "Screenshot")

## Installation

First, clone the repo onto your device:

    $ git clone git@github.com:rwanyoike/pelican-alchemy.git

Point the `THEME` variable in your pelican config to the `alchemy` folder:

    THEME = '/path/to/pelican-alchemy/alchemy'

### Alternative

Setup `pelican-alchemy` as a submodule:

    $ mkdir themes
    $ git submodule add git@github.com:rwanyoike/pelican-alchemy.git themes/pelican-alchemy

And in pelican config:

    THEME = 'themes/pelican-alchemy/alchemy'

## Settings

Visit the [settings page](https://rwanyoike.github.io/pelican-alchemy/pages/settings.html) for examples:

- **SITESUBTITLE**: Subtitle that appears in the header.
- **SITEIMAGE**: Image that appears in the header.
- **DESCRIPTION**: Index page HTML head meta description tag.
- **LINKS**: A list of tuples (Title, URL) for menu links.
- **ICONS**: A list of tuples (Icon, URL) for icon links.
- **PYGMENTS_STYLE**: Built-in Pygments style for syntax highlighting.
- **HIDE_AUTHORS**: Hide the author(s) of an article.
- **NEW_FAVICONS**: Use a [realfavicongenerator](https://realfavicongenerator.net/blog/new-favicon-package-less-is-more/) favicon package.

Others:

- **DISQUS_SITENAME**
- **GAUGES**
- **GOOGLE_ANALYTICS**
- **PIWIK_URL**
- **PIWIK_SITE_ID**

---

Pull requests are welcome! ☺️
