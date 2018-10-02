This project contains two different implementations of the LineServer problem:
* LineService uses caching mechanism to facilitate support of the large files and many concurrent users;
* LineServiceBasic is the naive implementation which places the entire file into memory upon reading. This 
      implementation was performing better for me on smaller files such as odyssey.txt ~ 600kB

    GET http://127.0.0.1:5000/lines/<line_id> 


#### Test Conditions
File `odyssey.txt` ~ 600kB. 

Load testing with Siege

    $ siege -c 5 -b -f test_urls.txt -r 5000

#### Test Results for odyssey.txt
##### CACHED
    Transactions:		       25000 hits
    Availability:		      100.00 %
    Elapsed time:		       46.63 secs
    Data transferred:	        1.42 MB
    Response time:		        0.01 secs
    Transaction rate:	      536.14 trans/sec
    Throughput:		        0.03 MB/sec
    Concurrency:		        4.97
    Successful transactions:       25000
    Failed transactions:	           0
    Longest transaction:	       19.81
    Shortest transaction:	        0.00

##### BASIC
    Transactions:		       25000 hits
    Availability:		      100.00 %
    Elapsed time:		       44.71 secs
    Data transferred:	        1.42 MB
    Response time:		        0.01 secs
    Transaction rate:	      559.16 trans/sec
    Throughput:		        0.03 MB/sec
    Concurrency:		        4.96
    Successful transactions:       25000
    Failed transactions:	           0
    Longest transaction:	       20.18
    Shortest transaction:	        0.00


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