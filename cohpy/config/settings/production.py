from .base import *

# TODO in production environment need to create .env file containing
# SECRET_KEY, can put explicit path into the following
# https://github.com/joke2k/django-environ

environ.Env.read_env("/home/web/dev/cohpy.org") # reading .env file

SECRET_KEY = env('SECRET_KEY')