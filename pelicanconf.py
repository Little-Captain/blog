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

THEME = 'pelican-themes/clean-blog'
PLUGIN_PATHS = ["pelican-plugins"]
PLUGINS = []

USE_FOLDER_AS_CATEGORY = True

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

# DISPLAY_PAGES_ON_MENU = True
# DISPLAY_CATEGORIES_ON_MENU = True
# DISPLAY_CATEGORIES_ON_SUBMENU = False
# DISPLAY_CATEGORIES_ON_POSTINFO = False
# DISPLAY_AUTHOR_ON_POSTINFO = False
# DISPLAY_SEARCH_FORM = False
# PAGES_SORT_ATTRIBUTE = 'Title'
# GITHUB_URL = None
# TAG_SAVE_AS = ''
# AUTHOR_SAVE_AS = ''
# DIRECT_TEMPLATES = ('index', 'categories', 'archives', 'search', 'tipue_search')
# TIPUE_SEARCH_SAVE_AS = 'tipue_search.json'
HEADER_COVER = 'assets/images/header_cover.jpg'
GITHUB_URL = 'https://github.com/Little-Captain'

COLOR_SCHEME_CSS = 'monokai.css'

# Blogroll
# LINKS = (('Github', 'https://github.com/Little-Captain'),)

# Social widget
# SOCIAL = (('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# PAGINATED_DIRECT_TEMPLATES = ('categories', 'archives')

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
