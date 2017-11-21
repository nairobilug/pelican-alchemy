# Pelican Alchemy

**Alchemy** ✨ is a functional, clean, responsive theme for the [Pelican](http://getpelican.com) static site generator.

Inspired by [crowsfoot](http://github.com/porterjamesj/crowsfoot) and [clean-blog](https://github.com/BlackrockDigital/startbootstrap-clean-blog), it features:

- Built with [Bootstap 4](http://v4-alpha.getbootstrap.com/) (v4-alpha)
- [Favicon Generator](http://realfavicongenerator.net/) support
- [Font Awesome](http://fontawesome.io/) icons
- [Pygments](http://pygments.org/) syntax highlighting styles
- `sitemap.xml` support
- External analytics (Google Analytics, Gauges, Piwik)
- External comments (Disqus)

![Screenshot](screenshot.jpg "Screenshot")

## Installation

Clone the repo:

```shell
$ git clone https://github.com/nairobilug/pelican-alchemy
```

Set the `THEME` variable in your Pelican config:

```python
THEME = '/PATH_TO_REPO/alchemy'
```

### As a Submodule

In your Pelican site:

```shell
$ mkdir themes
$ git submodule add https://github.com/nairobilug/pelican-alchemy themes/pelican-alchemy
```

And in Pelican config:

```python
THEME = 'themes/pelican-alchemy/alchemy'
```

## Usage

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

### Tips & Tricks

[https://github.com/nairobilug/pelican-alchemy/wiki/Tips](https://github.com/nairobilug/pelican-alchemy/wiki/Tips)

## Maintainers

- [@nairobilug](https://github.com/nairobilug)

## Contribute

Feel free to dive in. [Open an issue](https://github.com/nairobilug/pelican-alchemy/issues/new) or submit a PR.

**Alchemy** follows the [Contributor Covenant](CODE_OF_CONDUCT.md) code of conduct.

## License

[MIT](LICENSE) © 2017 Nairobi GNU/Linux Users Group
