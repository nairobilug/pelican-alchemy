## Bootstrap Classes

To have Bootstrap classes set for rendered html (`.table`, `.img-fluid` etc), use the [Bootstrapify](https://github.com/ingwinlu/pelican-bootstrapify) Pelican plugin.

In your Pelican site:

```bash
mkdir plugins
git submodule add https://github.com/ingwinlu/pelican-bootstrapify plugins/pelican-bootstrapify
```

And in Pelican config:

```python
# http://docs.getpelican.com/en/stable/plugins.html#how-to-use-plugins
PLUGIN_PATHS = ['plugins']
PLUGINS = ['pelican-bootstrapify']

BOOTSTRAPIFY = {
    'table': ['table', 'table-striped', 'table-hover'],
    'img': ['img-fluid'],
    'blockquote': ['blockquote'],
}
```

Use `BOOTSTRAPIFY` to pass a `{'css-selector': ['list-of-classes']}` dict to the plugin. Bootstrapify will append `list-of-classes` to all tags that match `css-selector`.

## Favicons

To use the `RFG_FAVICONS` setting, visit [Favicon Generator](http://realfavicongenerator.net/) to generate a favicon package and download it.

In your Pelican site:

```
mkdir content/extras
unzip <PATH_TO_PACKAGE>.zip -d content/extras
```

And in Pelican config:

```python
# https://github.com/getpelican/pelican/wiki/Tips-n-Tricks#second-solution-using-static_paths
STATIC_PATHS = ['extras', 'images']
EXTRA_PATH_METADATA = {
    'extras/android-chrome-192x192.png': {'path': 'android-chrome-192x192.png'},
    'extras/apple-touch-icon.png': {'path': 'apple-touch-icon.png'},
    'extras/browserconfig.xml': {'path': 'browserconfig.xml'},
    ...
}

RFG_FAVICONS = True
```

`EXTRA_PATH_METADATA` should correspond with the favicon package:

```bash
unzip -l <PATH_TO_PACKAGE>.zip
```

## Use `sitemap.xml`

There is a `sitemap.html` Jinja2 template that can be used to [generate a sitemap](https://github.com/getpelican/pelican/wiki/Tips-n-Tricks#generate-sitemapxml).

In your Pelican config:

```python
# Default value is ['index', 'tags', 'categories', 'authors', 'archives']
DIRECT_TEMPLATES = ['index', 'tags', 'categories', 'authors', 'archives', 'sitemap']
SITEMAP_SAVE_AS = 'sitemap.xml'
```