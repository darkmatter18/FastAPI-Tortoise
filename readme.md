# FasAPI Tortoise
### Includes
#### - FastAPI
#### - TortoiseORM
#### - Aerich
#### - User model + JWT auth
#### - Registration + password reset emails
#### - Logging to files
#### - Celery
#### - Alpine Dockerfile
#### - Docker-compose files
#### - NGINX + certbot

# Installation
#### Copy template.config.py -> config.py and fill
#### Register all app in config.applications (django style). The search for models will occur along the path app.applications.APP_NAME.models
#### Generate SECRET_KEY (`openssl rand -hex 32`)
#### You can also generate certificates with a script from a turnip (#TODO guide)
