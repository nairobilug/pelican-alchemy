# Settings

Unless otherwise specified, settings that refer to paths can be either absolute or relative to the configuration file.

## SITESUBTITLE

Subtitle that appears in the header:

```python
SITESUBTITLE = 'A magical \u2728 Pelican theme'
```

## SITEIMAGE

Image that appears in the header:

```python
SITEIMAGE = '/images/profile.png'
```

You can also force the image size:

```python
SITEIMAGE = '/images/profile.svg width=200 height=200'
```

## DESCRIPTION

Index HTML head `<meta>` description:

```python
DESCRIPTION = 'A functional, clean, responsive theme for Pelican. Heavily ' \
              'inspired by crowsfoot and clean-blog, powered by Bootstrap.'
```

## LINKS

A list of tuples (Title, URL) for menu links:

```python
LINKS = (
    ('Pelican', 'http://getpelican.com/'),
    ('Python.org', 'http://python.org/'),
    ('Jinja2', 'http://jinja.pocoo.org/'),
)
```

## ICONS

A list of tuples (Icon, URL) for icon links:

```python
ICONS = (
    ('github', 'https://github.com/nairobilug/pelican-alchemy'),
)
```

Icon in (Icon, URL) is a Font Awesome [icon](http://fontawesome.io/icons/) without the `fa-` prefix.

## PYGMENTS_STYLE

You can choose one of the built-in Pygments styles for syntax highlighting.

By default the `default` style is used:

```python
PYGMENTS_STYLE = 'default'
```

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

For a demo of the different styles, see [link](http://pygments.org/demo/).

## HIDE_AUTHORS

Hide the author(s) of an article - useful for single author sites:

```python
HIDE_AUTHORS = True
```

## NEW_FAVICONS

Use a [realfavicongenerator](https://realfavicongenerator.net/blog/new-favicon-package-less-is-more/) favicon package:

```python
RFG_FAVICONS = True
```

---

```python
DISQUS_SITENAME = '...'
GAUGES = '...'
GOOGLE_ANALYTICS = '...'
PIWIK_URL = '...'
PIWIK_SITE_ID = '...'
```
