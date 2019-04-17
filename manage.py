#!/usr/bin/env python
import os
import subprocess

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Shell
from redis import Redis
from rq import Connection, Queue, Worker

from app import create_app, db

app = create_app()
# app.app_context().push()

manager = Manager(app)
migrate = Migrate(app, db)
from app.models.bank import Bank_Branches
Bank_Branches.__init_mapper__()

def make_shell_context():
    return dict(app=app, db=db, Bank_Branches=Bank_Branches)


manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


@manager.command
def test():
    """Run the unit tests."""
    import unittest

    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


@manager.command
def recreate_db():
    """
    Recreates a local database. You probably should not use this on
    production.
    """
    db.drop_all()
    db.create_all()
    db.session.commit()


@manager.command
def format():
    """Runs the yapf and isort formatters over the project."""
    isort = 'isort -rc *.py app/'
    yapf = 'yapf -r -i *.py app/'

    print('Running {}'.format(isort))
    subprocess.call(isort, shell=True)

    print('Running {}'.format(yapf))
    subprocess.call(yapf, shell=True)

if __name__ == '__main__':
    manager.run()
