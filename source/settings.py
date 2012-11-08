"""Settings for pelican."""
AUTHOR = 'John Kitchin'
SITENAME = 'dft-book'
SITEURL = 'http://jkitchin.github.com/dft-book'

# This can also be the absolute path to a theme that you downloaded
# i.e. './themes/anothertheme/'
THEME = 'notmyidea'

# The folder ``images`` should be copied into the folder ``static`` when
# generating the output.
STATIC_PATHS = ['images', ]

# See http://pelican.notmyidea.org/en/latest/settings.html#timezone
TIMEZONE = 'UTC'

MARKUP = ('rst', 'md', 'html')

# Pelican will take the ``Date`` metadata and put the articles into folders
# like ``/posts/2012/02/`` when generating the output.
#ARTICLE_PERMALINK_STRUCTURE = '/%Y/%m/'

# I like to put everything into the category ``Blog``, which also appears on
# the main menu. Tags will not appear on the menu.
DEFAULT_CATEGORY = 'Blog'

# I like to have ``Archives`` in the main menu.
MENUITEMS = (
    ('Archives', '{0}/archives.html'.format(SITEURL)),
    ('dft-book', 'http://github.com/jkitchin/dft-book')
)

WITH_PAGINATION = True
DEFAULT_PAGINATION = 10
REVERSE_ARCHIVE_ORDER = True

# Uncomment what ever you want to use
GOOGLE_ANALYTICS = 'UA-35927456-1'
DISQUS_SITENAME = 'dftbook'
GITHUB_URL = 'http://github.com/jkitchin/dft-book'
#TWITTER_USERNAME = 'username'