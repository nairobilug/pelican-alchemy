# -*- coding: utf-8 -*-

from __future__ import unicode_literals

AUTHOR = 'Alchemy'
SITENAME = 'pelican-alchemy'
SITEURL = ''  # Intentionally left blank, see ./publishconf.py

PATH = 'content'

TIMEZONE = 'Africa/Nairobi'
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

ARTICLE_URL = 'posts/{slug}.html'
ARTICLE_SAVE_AS = ARTICLE_URL
ARTICLE_LANG_URL = 'posts/{slug}-{lang}.html'
ARTICLE_LANG_SAVE_AS = ARTICLE_LANG_URL

PLUGIN_PATHS = ['plugins']
PLUGINS = ['bootstrapify']

# Theme settings --------------------------------------------------------------

THEME = 'themes/pelican-alchemy/alchemy'

SITESUBTITLE = 'A magical \u2728 Pelican theme'
SITEIMAGE = '/images/profile.jpg width=200 height=200'
DESCRIPTION = 'A functional, clean, responsive theme for Pelican. Heavily ' \
              'inspired by crowsfoot and clean-blog, powered by Bootstrap.'

LINKS = (
    ('Pelican', 'http://getpelican.com/'),
    ('Python.org', 'http://python.org/'),
    ('Jinja2', 'http://jinja.pocoo.org/'),
)

ICONS = (
    # Note feed has it's domain hard-coded (cheap workaround)
    ('feed', 'https://rwanyoike.github.io/pelican-alchemy/feeds/all.atom.xml'),
    ('github', 'https://github.com/rwanyoike/pelican-alchemy'),
)

# Default value is ['index', 'tags', 'categories', 'authors', 'archives']
DIRECT_TEMPLATES = ['index', 'tags', 'categories', 'authors', 'archives', 'sitemap']
SITEMAP_SAVE_AS = 'sitemap.xml'
