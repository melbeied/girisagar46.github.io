#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Sagar Giri'
SITEURL = u'http://localhost:8000'
SITENAME = u"Sagar Giri's Blog"
SITETITLE = AUTHOR
SITESUBTITLE = '<pre>$ cd /pub && more beer</pre>'
SITEDESCRIPTION = u's programming, pelican, python, computer science, logic, algorithm'
PATH = 'content'

TIMEZONE = 'Asia/Kathmandu'

DEFAULT_LANG = u'en'
OG_LOCALE = 'en_US'
LOCALE = 'en_US'
DATE_FORMATS = {
    'en': '%B %d, %Y',
}

USE_FOLDER_AS_CATEGORY = False
COPYRIGHT_YEAR = 2017
DEFAULT_PAGINATION = 7

# Theme Settings
SITELOGO = '/images/sagar.jpg'
FAVICON = '/images/favicon.png'
THEME = 'themes/Flex'
BROWSER_COLOR = '#333333'
PYGMENTS_STYLE = 'monokai'


# Feed generation is usually not desired when developing
FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Main Menu
MAIN_MENU = True
MENUITEMS = (('Blog', '/'),('Archives', '/archives'),('Categories', '/categories'),('Tags', '/tags'),)

# Blogroll
# LINKS = (('Blog', '/'),)

# Social widget
SOCIAL = (('linkedin', 'www.linkedin.com/in/girisagar46'),
          ('github', 'https://github.com/girisagar46'),
          ('twitter', 'https://twitter.com/sagargiri46'),
          ('stack-overflow', 'http://stackoverflow.com/story/girisagar46.github.io'),
          )

# Plugins
# See: http://docs.getpelican.com/en/latest/plugins.html
PLUGIN_PATHS = ['./plugins']
PLUGINS = ['sitemap', 'post_stats', 'share_post', 'feed_summary']

# Sitemap Settings
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.6,
        'indexes': 0.6,
        'pages': 0.5,
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly',
    }
}

STATIC_PATHS = ['images', 'extras']

EXTRA_PATH_METADATA = {
    'extras/custom.css': {'path': 'static/custom.css'},
    # 'extra/CNAME': {'path': 'CNAME'},
    # 'extra/robots.txt': {'path': 'robots.txt'}
}

CUSTOM_CSS = 'static/custom.css'
HOME_HIDE_TAGS = True
USE_LESS = False
FEED_USE_SUMMARY = True

GOOGLE_ANALYTICS = 'UA-73000395-1'
DISQUS_SITENAME = 'girisagar46-github-io'

# Formatting for URLS
ARTICLE_URL = '{slug}'
PAGE_URL = 'pages/{slug}'
CATEGORY_URL = 'category/{slug}'
TAG_URL = 'tag/{slug}'
AUTHOR_SAVE_AS = False
AUTHORS_SAVE_AS = False
