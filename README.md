# [pyGhana](http://pythonghana.org/)

    This is the source code for the http://pythonghana.org/ website.

# Running the site locally

## Requirments

* [Python 3.5](https://python.org)
* [Django - python web framework](https://www.djangoproject.com/)
* [Virtualenvwrapper](https://virtualenvwrapper.readthedocs.io)

## Installation

* [Follow the guide here](https://help.github.com/articles/fork-a-repo) on how to clone or fork a repo
* [Follow the guide here](http://simononsoftware.com/virtualenv-tutorial/) on how to create virtualenv
* Create a virtualenv (example _myvenv_) and activate it (see Code below).

  ```
  source virtualenvwrapper.sh

  mkvirtualenv myvenv --python=/usr/bin/python3.5

  (myvenv) $ pip install -r requirements.txt

  (myvenv) $ python manage.py migrate

  (myvenv) $ python manage.py makemigrations

  (myvenv) $ python manage.py runserver
  ```

* Copy the IP address provided once your server has completed building the site. (It will say something like >> Serving at 127.0.0.1....).
* Open the address in the browser
* `Note`: It is important that when you create your virtualenv, do not create it in the same folder as the code you downloaded.

# Contributing

Read our [Contributing Guide](./CONTRIBUTING.md) on how to contribute to the project.
