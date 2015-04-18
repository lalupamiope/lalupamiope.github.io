#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'La Lupa Miope Somos Todos'
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
          ('Google', 'http://www.google.com/'),
          ('Yahoo', 'http://www.yahoo.com/'),
          )

# Social widget
SOCIAL = (('Twitter', 'http://twitter.com/LaLupaMiope'),
          ('Google+', 'https://plus.google.com/u/1/118107966922479036447'),
)

DEFAULT_PAGINATION = 10

# Seteos para modificar cuando pruebo el blog con un servidor en localhost
# Los posts con fecha futura se toman como drafts
# WITH_FUTURE_DATES = False
# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = "../pelican-elegant-lalupamiope"

# --------------------------------------------------------------------------

# TAG_CLOUD_STEPS = 4
# TAG_CLOUD_MAX_ITEMS = 100


FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'
DISQUS_SITENAME = "lalupamiope"

# Instrucciones para la instalacion del plugin para videos de youtube
# en https://github.com/kura/pelican_youtube
PLUGIN_PATHS = ['../pelican-plugins']

LOAD_CONTENT_CACHE = False

# Direct_Templates lo requiere Elegant, esta habilitado mas abajo
# DIRECT_TEMPLATES = ('index', 'categories', 'archives')
# TYPOGRIFY = True

TWITTER_USERNAME = 'lalupamiope'

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
SITE_LICENSE = u'Se puede usar el contenido de este blog poniendo un link hacia nosotros: http://lalupamiope.github.io/'
SITE_DESCRIPTION = u'Arqueología Digital'
EMAIL_SUBSCRIPTION_LABEL = u'Suscripción'
EMAIL_FIELD_PLACEHOLDER = u'¿dirección de e-mail?'
SUBSCRIBE_BUTTON_TITLE = u'Suscribirme'
# MAILCHIMP_FORM_ACTION = u'Esto es del mailchimp'

LANDING_PAGE_ABOUT = ({'title': 'La Lupa Miope', 'details': '<p>La lupa miope o lupa Keyser (/ˈlupa ˈkaɪzər/) es una lente convergente de prospección utilizada en arqueología para examinar desde una gran cercanía piezas de interés paleontológico, de allí la denominación. Se comenzó a utilizar en el siglo XIX pero hay registros que inducen a considerar que ya existían antecesores de este instrumento durante el Renacimiento temprano, según se puede deducir de los cuadernos de notas de investigadores de aquel período histórico.</p> <p>La <i>lupa miope</i> no debe ser manipulada por cualquier persona sin la adecuada preparación. Si se utiliza por fuera de sus especificaciones técnicas puede alterar los resultados que ofrece, aunque es improbable que le ocasione desperfectos, siendo un noble instrumento que apenas requiere de una limpieza ocasional. De todos modos, si se opera con una velocidad excesiva neutraliza sus ventajas para advertir aquello que las herramientas más comunes suelen pasar por alto, y por ello mismo se desnaturalizaría su especificidad. Por otra parte, si es demasiado lento el ritmo con que su óptica escudriña los objetos de interés, el peligro radica en que provoca tedio en quien la opera, poniendo en duda la continuidad de la investigación en curso.</p> <p> En este sitio web somos especialistas en el uso de la <i>lupa miope</i>, con la que exploramos montañas de material en la web para encontrar textos y otros objetos singulares que cotidianamente son sepultados en las redes digitales por toneladas de ruido informático. Estas obras que se pierden bajo innumerables capas sedimentarias de hiperproducción cultural contemporánea son las que recuperamos y ponemos a disposición de nuestros visitantes, ya sean piezas de humor, artículos científicos u otras formas del arte. La <i>lupa miope</i> es un minucioso inventario de nuestros descubrimientos, en la senda de los más completos catálogos de vasijas precolombinas, caftanes de terciopelo turco y talismanes caldeos. Nuestra labor de recuperación requiere de concentración y una total entrega, análogas a las imperativas en un paleontólogo que anhela el descubrimiento. Por ello solicitamos que valore nuestra labor con su atenta, silenciosa y periódica visita.</p>'})

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
