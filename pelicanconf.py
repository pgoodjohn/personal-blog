#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Pietro Bongiovanni'
SITENAME = u'Software Engineering is hard'
SITEURL = ''

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
         ('My company\'s technical blog', 'https://medium.com/fixico'),
         ('Source Code', 'https://github.com/pgoodjohn/personal-blog'))

# Social widget
SOCIAL = (('GitHub', 'https://github.com/pgoodjohn'),
          ('Twitter', 'https://www.twitter.com/pietrogoodjohn'),
          ('Linkedin', 'https://www.linkedin.com/in/pietro-bongiovanni-2657a761/'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Theme and theme settings
THEME='pelican-sober'
PELICAN_SOBER_ABOUT = "My name is Pietro. I am a Software Engineer, a consultant and a student. I sometime write things and publish them."
PELICAN_SOBER_STICKY_SIDEBAR = True

# Theme info: https://github.com/fle/pelican-sober

