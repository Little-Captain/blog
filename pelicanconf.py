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

THEME = 'pelican-themes/tuxlite_tbs'
PLUGIN_PATHS = ["pelican-plugins"]
PLUGINS = ['pelican-toc']

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

# Blogroll
LINKS = (('Github', 'https://github.com/Little-Captain'),)

# Social widget
# SOCIAL = (('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# PAGINATED_DIRECT_TEMPLATES = ('categories', 'archives')

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

#pelican_toc插件配置
TOC = {
    'TOC_HEADERS' : '^h[3-6]',  # What headers should be included in the generated toc
                                # Expected format is a regular expression

    'TOC_RUN'     : 'true'      # Default value for toc generation, if it does not evaluate
                                # to 'true' no toc will be generated
}
