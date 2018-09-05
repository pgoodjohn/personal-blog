#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Pietro Bongiovanni'
SITENAME = u'Engineering life with Software'
SITEURL = 'https://blog.pietrobongiovanni.com'
GOOGLE_ANALYTICS = u'UA-78188164-4'

PATH = 'content'

TIMEZONE = 'Europe/Amsterdam'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('My website', 'https://pietrobongiovanni.com/'),
         ('Source Code', 'https://github.com/pgoodjohn/personal-blog'))

# Social widget
SOCIAL = (('GitHub', 'https://github.com/pgoodjohn'),
          ('Twitter', 'https://www.twitter.com/pietrogoodjohn'),
          ('Linkedin', 'https://www.linkedin.com/in/pietro-bongiovanni-2657a761/'))

DEFAULT_PAGINATION = 10

DEFAULT_METADATA = {
    'status': 'draft',
}

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False

# Theme and theme settings
THEME='themes/pelican-sober'
CSS_FILE = 'main.css'
PELICAN_SOBER_ABOUT = "Discussing hard topics in Software and how to use engineering principles to improve everyday life."
PELICAN_SOBER_STICKY_SIDEBAR = True

# Theme info: https://github.com/fle/pelican-sober

