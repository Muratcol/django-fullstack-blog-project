# Django Fullstack Blog Project

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/Muratcol/django-fullstack-blog-project.git
$ cd django-fullstack-blog-project
```

Then install the dependencies:

```sh
$ pip install -r requirements.txt
```

Once `pip` has finished downloading the dependencies:
```sh
$ python manage.py runserver
```
And navigate to `http://localhost:8000`.


## Static Files

When you interact with the application, deploy every CSS/JS files to
```sh
STATIC_ROOT = os.path.join(BASE_DIR, 'static_files')
```
With this command:

```sh
$ python manage.py collectstatic
```
### Email Configurations

If you're planning to use reset password feature of the project,

Go to: `django-fullstack-blog-project/doviz_uygulamasi/settings.py/`

Then write your own gmail and password to settings:
 
 
```sh
EMAIL_HOST_USER = os.environ.get('DB_USER')
EMAIL_HOST_PASSWORD = os.environ.get('DB_PASS')
```

### Media Root

Profile pictures that users upload to their profiles, will located to:

`MEDIA_ROOT = os.path.join(BASE_DIR, 'media')`

You can also configure path with:

`django-fullstack-blog-project/doviz_uygulamasi/settings.py/`

## Tests

To run the tests, `cd` into the directory where `manage.py` is:
```sh
$ python manage.py test
```
