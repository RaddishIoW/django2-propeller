Propeller for Django2
====================

Write Django as usual, and let ``django2-propeller`` make template output into code based on Google's Material Design Standards & Bootstrap.


[![Build Status](https://travis-ci.org/tfroehlich82/django-propeller.svg?branch=stable)](https://travis-ci.org/tfroehlich82/django-propeller)
[![Coverage Status](https://coveralls.io/repos/github/tfroehlich82/django-propeller/badge.svg?branch=stable)](https://coveralls.io/github/tfroehlich82/django-propeller?branch=stable)
[![Code Health](https://landscape.io/github/tfroehlich82/django-propeller/stable/landscape.svg?style=flat)](https://landscape.io/github/tfroehlich82/django-propeller/stable)
![PyPI version](http://img.shields.io/pypi/v/django-propeller.svg)
![PyPI downloads](http://img.shields.io/pypi/dm/django-propeller.svg)
[![Updates](https://pyup.io/repos/github/tfroehlich82/django-propeller/shield.svg)](https://pyup.io/repos/github/tfroehlich82/django-propeller/)
[![Python 3](https://pyup.io/repos/github/tfroehlich82/django-propeller/python-3-shield.svg)](https://pyup.io/repos/github/tfroehlich82/django-propeller/)


Requirements
------------

- Python 3.3, 3.4, 3.5, or 3.6
- Django >= 2.0


Installation
------------

1. Install using pip:
```
    pip install django2-propeller
```

2. Add to INSTALLED_APPS in your ``settings.py``:

   ```
   'django2_propeller',
   ```

3. In your templates, load the ``django2_propeller`` library and use the ``propeller_*`` tags:



Example template
----------------

```
    {% load propeller %}

    {# Display a form #}

    <form action="/url/to/submit/" method="post" class="form">
        {% csrf_token %}
        {% propeller_form form %}
        {% buttons %}
            <button type="submit" class="btn btn-primary">
                {% propeller_icon "star" %} Submit
            </button>
        {% endbuttons %}
    </form>
```


Documentation
-------------

The full documentation is at http://django-propeller.readthedocs.io/en/stable/ (currently for the previous version of django-propeller)


Demo application
----------------

The demo application provides a number of useful examples.

clone the repo:

    $ git clone https://github.com/RaddishIoW/django2-propeller.git

cd into the cloned directory:

    $ cd django2-propeller

run the testserver:

    $ python manage.py runserver

open your browser and browse to:

    http://127.0.0.1:8000


Bugs and suggestions
--------------------

If you have found a bug or if you have a request for additional functionality, please use the issue tracker on GitHub.

https://github.com/RaddishIoW/django2-propeller/issues


Further Information
-------------------

Propeller: http://propeller.in/

Bootstrap: http://getbootstrap.com/

Google Material Design: https://material.io/


License
-------

You can use this under MIT License. See [LICENSE](LICENSE) file for details.


Author
------

Originally developed and maintained by [Thorsten Fröhlich](https://github.com/tfroehlich82),
based on the idea of [django-bootstrap3](https://github.com/dyve/django-bootstrap3) from [Dylan Verheul](https://github.com/dyve).
This package is updated by [Adam Radestock](https://github.com/RaddishIoW) to work with Django 2
