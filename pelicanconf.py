#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Charles Sartori'
SITENAME = 'Charles Sartori'
SITEURL = 'http://charlessartori.com'
#SITEURL = 'http://localhost:8000'

PATH = 'content'

THEME = 'flex'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


# Social widget
SOCIAL = (('github', 'https://github.com/csarcom'),
          ('facebook', 'https://www.facebook.com/charlesmpsartori'),
          ('linkedin', 'https://br.linkedin.com/in/charlessartori'))

DEFAULT_PAGINATION = 1

DISQUS_SITENAME = 'charlessartori'

STATIC_PATHS = ['images', 'pdfs']
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = []

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
