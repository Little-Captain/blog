#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# python --version : 3.6.5

AUTHOR = 'Little Captain'
SITENAME = "Little Captain's Blog"
SITEURL = 'http://littlecaptain.net'

PATH = 'articles'
TIMEZONE = 'Asia/Shanghai'
DATE_FORMATS = {'zh':'%Y-%m-%d %H:%M'}
DEFAULT_LANG = 'en'

THEME = 'pelican-themes/html5-dopetrope'
PLUGIN_PATHS = ["pelican-plugins"]
PLUGINS = []

USE_FOLDER_AS_CATEGORY = False

SITELOGO = 'assets/images/avatar.jpg'
FAVICON = 'assets/images/avatar.jpg'
SITELOGO_SIZE = 14

STATIC_PATHS = ['assets']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Github', 'https://github.com/Little-Captain'),)

# Social widget
# SOCIAL = (('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# PAGINATED_DIRECT_TEMPLATES = ('categories', 'archives')

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
