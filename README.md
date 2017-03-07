# pelican-alchemy

Alchemy ✨ is a functional, clean, responsive theme for the [Pelican](http://getpelican.com) static site generator. Inspired by [crowsfoot](http://github.com/porterjamesj/crowsfoot) and [clean-blog](https://github.com/BlackrockDigital/startbootstrap-clean-blog).

## Screenshot

![Screenshot](screenshot.jpg "Screenshot")

## Features

- Powered by [Bootstap 4](http://v4-alpha.getbootstrap.com/)
- [Favicon Generator](http://realfavicongenerator.net/) support
- [Font Awesome](http://fontawesome.io/) icons
- [Pygments](http://pygments.org/) syntax highlighting styles
- `sitemap.xml` support
- External analytics (Google Analytics, Gauges, Piwik)
- External comments (Disqus)

## Installation

Clone the repo:

    $ git clone https://github.com/nairobilug/pelican-alchemy

Set the `THEME` variable in your Pelican config:

    THEME = '/PATH_TO_REPO/alchemy'

### As a submodule

In your Pelican site:

    $ mkdir themes
    $ git submodule add https://github.com/nairobilug/pelican-alchemy themes/pelican-alchemy

And Pelican config:

    THEME = 'themes/pelican-alchemy/alchemy'

## Settings

Visit the [Settings wiki](https://github.com/nairobilug/pelican-alchemy/wiki/Settings) for examples:

- **SITESUBTITLE**: Subtitle that appears in the header.
- **SITEIMAGE**: Image that appears in the header.
- **DESCRIPTION**: Index HTML head `<meta>` description.
- **LINKS**: A list of tuples (Title, URL) for menu links.
- **ICONS**: A list of tuples (Icon, URL) for icon links.
- **PYGMENTS_STYLE**: Built-in Pygments style for syntax highlighting.
- **HIDE_AUTHORS**: Hide the author(s) of an article - useful for single author sites.
- **RFG_FAVICONS**: Use a Favicon Generator package.

Misc settings:

- **DISQUS_SITENAME**
- **GAUGES**
- **GOOGLE_ANALYTICS**
- **PIWIK_URL**
- **PIWIK_SITE_ID**

Example [pelicanconf.py](https://github.com/nairobilug/pelican-alchemy/blob/demo/pelicanconf.py) (demo website).

## Tips & Tricks

[https://github.com/nairobilug/pelican-alchemy/wiki/Tips](https://github.com/nairobilug/pelican-alchemy/wiki/Tips)
