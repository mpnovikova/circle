This project contains two different implementations of the LineServer problem

    http://127.0.0.1:5000/lines/<line_id> 
uses caching mechanism to facilitate support of the large files and many concurrent users

    http://127.0.0.1:5000/basic_lines/<line_id>
is the naive implementation which places the entire file into memory upon reading. This implementation was performing 
better for me on smaller files such as odyssey.txt ~ 600kB

#### Prerequisites

* [Python 3.7](https://www.python.org/downloads/)
* [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/)
* [git](https://git-scm.com/downloads)
* [flask](http://flask.pocoo.org/)

To install requirements in a virtual environment begin by running

    $ virtualenv venv

Followed by installing requirements:

    $ pip install -r src/requirements.txt

This is a Flask application which comes with some built-in commands.   
To start this application, run 

    $ export FLASK_APP=src/app.py
    $ export FLASK_ENV=development
    $ python -m flask run
     * Running on http://127.0.0.1:5000/

To execute unit tests, run

    $ python manage.py test