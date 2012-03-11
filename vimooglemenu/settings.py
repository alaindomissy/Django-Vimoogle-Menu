# Django settings for project vimooglemenu.
# inspired from http://rdegges.com/the-perfect-django-settings-file


import sys
import os
from os.path import abspath, basename, dirname, join, normpath





########## PATH CONFIGURATION
################################################################################
# Absolute filesystem path to this Django project directory.

#DJANGO_ROOT = dirname(dirname(abspath(__file__)))
DJANGO_ROOT = dirname(abspath(__file__))                           # currently /home/picturep/sites/djangovimooglemenu/vimooglemenu

# Site name.
SITE_NAME = basename(DJANGO_ROOT)                                  # currently vimooglemenu

# Absolute filesystem path to the top-level project folder.
SITE_ROOT = dirname(DJANGO_ROOT)                                   # currently /home/picturep/sites/djangovimooglemenu/

# Add all necessary filesystem paths to our system path so that we can use
# python import statements.
sys.path.append(SITE_ROOT)

# Added by AD
sys.path.append(DJANGO_ROOT)

#sys.path.append(normpath(join(DJANGO_ROOT, 'apps')))             # not yet organised with all apps folder inside an apps folder
#sys.path.append(normpath(join(DJANGO_ROOT, 'libs')))

########## END PATH CONFIGURATION




#from helpers import gen_secret_key

# Absolute filesystem path to the secret file which holds this project's
# SECRET_KEY. Will be auto-generated the first time this file is interpreted.
#SECRET_FILE = normpath(join(SITE_ROOT, 'deploy', 'SECRET'))






########## DEBUG CONFIGURATION
################################################################################
# Disable debugging by default.

DEBUG = True

TEMPLATE_DEBUG = DEBUG

########## END DEBUG CONFIGURATION





########## MANAGER CONFIGURATION
################################################################################
# Admin and managers for this project. These people receive private site alerts.

ADMINS = ( ('Your Name', 'your_email@example.com'), )

MANAGERS = ADMINS

########## END MANAGER CONFIGURATION


########## DATABASES CONFIGURATION
################################################################################ 
DATABASES = {
   'default': {
        'ENGINE':   'django.db.backends.sqlite3',  # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME':     'vimooglemenu.db',               # Or path to database file if using sqlite3.
        'USER':     '',                            # Not used with sqlite3.
        'PASSWORD': '',                            # Not used with sqlite3.
        'HOST':     '',                            # Set to empty string for localhost. Not used with sqlite3.
        'PORT':     '',                            # Set to empty string for default. Not used with sqlite3.
   },
}
#DEPRECATED
#DATABASE_ENGINE = 'sqlite3'     # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
#DATABASE_NAME = 'vimooglemenu.db' # Or path to database file if using sqlite3.
#DATABASE_USER = ''             # Not used with sqlite3.
#DATABASE_PASSWORD = ''         # Not used with sqlite3.
#DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
#DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.
########## END DATABASES CONFIGURATION



########## GENERAL CONFIGURATION
################################################################################ 

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Tijuana'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

########## END GENERAL CONFIGURATION






########## MEDIA CONFIGURATION
################################################################################
# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = '/home/picturep/sites/djangovimooglemenu/vimooglemenu/media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'
########## END MEDIA CONFIGURATION






########## STATIC FILE CONFIGURATION
################################################################################

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"                              
STATIC_ROOT = os.path.join(os.path.dirname(__file__), 'static')         # currently  '/home/user/python/vimooglemenu/static'
#STATIC_ROOT = normpath(join(DJANGO_ROOT, 'static')),


# URL prefix for static files.
STATIC_URL = '/static/'
# URL prefix for admin static files -- CSS, JS and images.
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Always use forward slashes. Use absolute paths
    #normpath(join(DJANGO_ROOT, 'assets')),                               # currently '/home/user/python/vimooglemenu/assets'
     #         '/home/user/python/vimooglemenu/vimooglemenu/assets/'
     #         '/home/user/python/vimooglemenu/vimooglemenu/homepage/static/',
    ('css',   '/home/user/python/vimooglemenu/vimooglemenu/homepage/static/css/'   ),   # /static/css/style.css will be loaded from indicated directory
    ('js',    '/home/user/python/vimooglemenu/vimooglemenu/homepage/static/js/'   ),    # /static/js/jquery.js will be loaded from ...
    ('images','/home/user/python/vimooglemenu/vimooglemenu/homepage/static/images/')    # /static/images/dot.png   will be loaded from...
)

# List of finder classes that know how to find static files in various locations.
STATICFILES_FINDERS = (
	#'django.contrib.staticfiles.finders.FileSystemFinder',
	'django.contrib.staticfiles.finders.AppDirectoriesFinder',
	#'django.contrib.staticfiles.finders.DefaultStorageFinder',
)


########## END STATIC FILE CONFIGURATION




########## TEMPLATE CONFIGURATION
################################################################################

# AD ADDED:
TEMPLATE_CONTEXT_PROCESSORS = ( 
                               "django.contrib.auth.context_processors.auth",
                               "django.core.context_processors.debug",
                               "django.core.context_processors.i18n",
                               "django.core.context_processors.media",
                               "django.core.context_processors.static",
                               "django.core.context_processors.request",
                               "django.contrib.messages.context_processors.messages")
                                                   
# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
                                'djaml.app_directories',
                                'djaml.filesystem', 
                                'django.template.loaders.app_directories.load_template_source',                          
                                'django.template.loaders.filesystem.load_template_source',
                               #'django.template.loaders.eggs.load_template_source',
)

# Directories to search when loading templates.
TEMPLATE_DIRS = (
    #'/home/user/python/vimooglemenu/templates/', 
    #'/home/user/python/vimooglemenu/homepage/templates/',
)

########## END TEMPLATE CONFIGURATION



########## MIDDLEWARE CONFIGURATION
################################################################################
MIDDLEWARE_CLASSES = (
    #'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    #'django.contrib.messages.middleware.MessageMiddleware',
    
    'pipeline.middleware.MinifyHTMLMiddleware',
    
)
########## END MIDDLEWARE CONFIGURATION





INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    #'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Admin panel and documentation.
    'django.contrib.admin',
    'django.contrib.admindocs',
      
  	# South migration tool.
	  #'south',

	  # Celery task queue.
   	#djcelery',
   	
   	'pipeline',
   	
   	'vimooglemenu.homepage'
)
    
########## CELERY CONFIGURATION
#import djcelery
#djcelery.setup_loader()
########## END CELERY CONFIGURATION



########## URL CONFIGURATION
################################################################################

# obsoleted
#ROOT_URLCONF = 'vimooglemenu.urls'

ROOT_URLCONF = '%s.urls' % SITE_NAME

########## END URL CONFIGURATION





########## KEY CONFIGURATION
################################################################################


# Make this unique, and don't share it with anybody.

SECRET_KEY = '4k&25fo3=6+5jws8+k6r96b_+3+*019vup_v%wi@mwv8l_*656' 


# Try to load the SECRET_KEY from our SECRET_FILE. If that fails, then generate
# a random SECRET_KEY and save it into our SECRET_FILE for future loading. If
# everything fails, then just raise an exception.

#  try:
#  	SECRET_KEY = open(SECRET_FILE).read().strip()
#  except IOError:
#  	try:
#  		with open(SECRET_FILE, 'w') as f:
#  			f.write(gen_secret_key(50))
#  	except IOError:
#  		raise Exception('Cannot open file `%s` for writing.' % SECRET_FILE)
		
########## END KEY CONFIGURATION



# integration of pipeline with staticfiles
# either of these alternatives changes the method used by staticfiles collectstatic to save copy of static files to compress first
#STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'     # the default StaticFilesStorage  not StaticFileStorage
STATICFILES_STORAGE = 'pipeline.storage.PipelineStorage'          # replacement   bug?
#STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'   # replacement with caching
#PIPELINE_STORAGE    = 'pipeline.storage.PipelineFinderStorage'


PIPELINE_CSS = {
    'colors': {
        'source_filenames': (
          'css/vimooglemenu.css',
        ),
        'output_filename': 'css/vimooglemenupipelined.css',
        'extra_context': {
            'media': 'screen,projection',
        },
    },
}

# Whether pipeline is used. When False, the source-files will be used instead
#PIPELINE = not DEBUG;     # the default
PIPELINE = True

# Compressor class to be applied to CSS files. # If empty or None, CSS files wont be compressed.
#PIPELINE_CSS_COMPRESSOR = 'pipeline.compressors.yui.YUICompressor'   # the default
PIPELINE_CSS_COMPRESSOR = None

# Compressor class to be applied to JS files. # If empty or None, JS files wont be compressed.
# PIPELINE_JS_COMPRESSOR = 'pipeline.compressors.yui.YUICompressor'   # the default
PIPELINE_JS_COMPRESSOR = None


#In order to use YUI Compressor, you need to install YUI Compressor (see Installation for more details).

#PIPELINE_TEMPLATE_NAMESPACE
#Object name where all of your compiled templates will be added, from within your browser. 
#To access them with your own JavaScript namespace, change it to the object of your choice.
# Defaults to "window.JST"

#PIPELINE_TEMPLATE_EXT
#The extension for which Pipeline will consider the file as a Javascript templates. 
#To use a different extension, like .mustache, set this settings to .mustache.
#Defaults to ".jst"

#PIPELINE_TEMPLATE_FUNC
#JavaScript function that compiles your JavaScript templates. 
#Pipeline doesnt bundle a javascript template library, but the default settings is to use the underscore template function.
#Defaults to "_.template"



PIPELINE_COMPILERS = (
  'pipeline.compilers.sass.SASSCompiler',
)
# Command line to execute for sass program.
PIPELINE_SASS_BINARY= '/home/user/.gem/ruby/1.9.1/bin/sass'       #Defaults to '/usr/local/bin/sass'.

#Additional arguments to use when sass is called.
#PIPELINE_SASS_ARGUMENTS=' -t nested'                              #Defaults to ''.







