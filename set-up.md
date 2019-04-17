# Setting up

## Add Environment Variables

* `DATABASE_URL`: set to a database uri

## Install the dependencies

```
$ pip install -r requirements.txt
```

## Running the app

```
$ source env/bin/activate
$ gunicorn manage:app --worker-class=gevent --workers 4
```