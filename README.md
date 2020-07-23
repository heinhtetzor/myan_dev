# myan_dev

INSTALL PYTHON3 in your machine.
MAKE SURE pip is also installed.

Check if it's installed already --
$: python --version
$: pip --version

CREATE a new folder.

Go inside folder using Terminal.

CREATE new virtual env
$: python3 -m venv venv

CLONE THIS REPO inside the folder

RUN THIS to install all requirements
$: pip install -r myandev/requirements.txt

GO TO myandev/settings.py to update Database Configurations

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db_name',
        'USER': 'name',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
    }
}

RUN this to migrate (creating tables in database)
$: python manage.py migrate

Check Your Database

CREATE admin account using this command
$: python manage.py createsuperuser

RUN this to initiate sevrer
$: python manage.py runserver

ACCESS the site at 
http://localhost:8000
