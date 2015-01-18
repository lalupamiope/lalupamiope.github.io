#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Todos los autores'
SITENAME = 'La Lupa Miope'
SITEURL = 'http://lalupamiope.github.io'

PATH = 'content'

TIMEZONE = 'America/Argentina/Buenos_Aires'

DEFAULT_LANG = 'es'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS =  (
    # ('Archives', 'archives.html'),
          ('TecnoVortex', 'http://tecnovortex.com/'),
          ('GeekHack', 'http://geekhack.org/'),
          ('Prelude', 'http://batsov.com/prelude/'),
          ('Ergoemacs', 'http://ergoemacs.org/'),
          ('Seminario Gargarella', 'http://seminariogargarella.blogspot.com.ar/'),)

# Social widget
SOCIAL = (('Twitter', 'http://twitter.com/eldiegoefe'),
          ('Github', 'https://github.com/eldiegoefe'),
          ('Facebook', 'http://www.facebook.com/eldiegoefe'),
          ('Flickr', 'https://www.flickr.com/photos/eldiegoefe/'),
          ('Instagram', 'http://instagram.com/eldiegoefe'),
          ('Google+', 'https://plus.google.com/+DiegoEfe'),
          ('Diaspora', 'https://www.joindiaspora.com/u/eldiegoefe'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

THEME = "/home/eldiegoefe/documentos/pelican-themes-elegant/pelican-elegant-lalupamiope"

# --------------------------------------------------------------------------

# TAG_CLOUD_STEPS = 4
# TAG_CLOUD_MAX_ITEMS = 100


FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'
DISQUS_SITENAME = "certezasdudosas"

# Instrucciones para la instalacion del plugin para videos de youtube
# en https://github.com/kura/pelican_youtube
PLUGIN_PATHS = ['/home/eldiegoefe/documentos/pelican-plugins']

LOAD_CONTENT_CACHE = False

# Direct_Templates lo requiere Elegant, esta habilitado mas abajo
# DIRECT_TEMPLATES = ('index', 'categories', 'archives')
# TYPOGRIFY = True

TWITTER_USERNAME = 'eldiegoefe'

# ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}.html'
# ARTICLE_SAVE_AS = '/home/eldiegoefe/documentos/eldiegoefe.github.io/output/{date:%Y}/{date:%m}/{slug}.html'
# ARTICLE_EXCLUDES = ('pages',)
# PAGE_URL = 'pages/{slug}.html'


# Elegant requiere los siguientes seteos

PLUGINS = ['sitemap', 'extract_toc', 'tipue_search', 'pelican_youtube']
# el plugin pelican_youtube lo tenia desde antes de Elegant

MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'headerid', 'toc']
DIRECT_TEMPLATES = (('index', 'tags', 'categories','archives', 'search', '404'))
STATIC_PATHS = ['theme/images', 'images']
TAG_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
AUTHOR_SAVE_AS = ''

# esto tambien es de Elegant...
# These are the optional configuration variables that you can define

RECENT_ARTICLES_COUNT = 20
COMMENTS_INTRO = u'Comentate algo...'
SITE_LICENSE = u'Podes usar el contenido de este blog si pones un link hacia http://lalupamiope.github.io/'
SITE_DESCRIPTION = u'Blog del Diego Efe'
EMAIL_SUBSCRIPTION_LABEL = u'Suscripción'
EMAIL_FIELD_PLACEHOLDER = u'¿dirección de e-mail?'
SUBSCRIBE_BUTTON_TITLE = u'Suscribirme'
# MAILCHIMP_FORM_ACTION = u'Esto es del mailchimp'

LANDING_PAGE_ABOUT = ({'title': 'La Lupa Miope', 'details': '<p>¡Cuidado, estamos compartiendo! En estas páginas hay textos, fotos y otras producciones que los arqueólogos digitales algún día se alegrarán de encontrar.</p>'})

# PROJECTS = [{
#     'name': 'Logpad + Duration',
#     'url': 'https://github.com/talha131/logpad-plus-duration#logpad--duration',
#     'description': 'Vim plugin to emulate Windows Notepad logging feature,'
#     ' and log duration of each entry'},
#     {'name': 'Elegant Theme for Pelican',
#     'url': 'http://oncrashreboot.com/pelican-elegant',
#     'description': 'A clean and distraction free theme, with search and a'
#     ' lot more unique features, using Jinja2 and Bootstrap'}]

RECENT_ARTICLES_COUNT = 10

# These are the optional article meta data variables that you can use

# subtitle
# summary
# disqus_identifier
# modified
# keywords

# info sobre sitemap. priorities y changefreqs tienen valores que usan
# los buscadores. mas info en:
# http://docs.getpelican.com/en/3.1.1/plugins.html#sitemap

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}
