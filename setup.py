from setuptools import setup

setup(
    name='FreeTAKServer-UI',
    version='2.1.1.2',
    packages=['FreeTAKServer-UI', 'FreeTAKServer-UI.app', 'FreeTAKServer-UI.app.base', 'FreeTAKServer-UI.app.home', 'FreeTAKServer-UI.tests'],
    url='https://github.com/FreeTAKTeam/FreeTakServer',
    license='Eclipse License',
    author='Ghost, C0rv0',
    author_email='freetakteam@gmail.com',
    description='an optional UI for FreeTAKServer',
    install_requires = [
        "flask",
        "flask_login",
        "flask_migrate",
        "flask_wtf",
        "WTForms",
        "sqlalchemy",
        "flask_sqlalchemy",
        "email_validator",
        "gunicorn",
        "python-decouple",
        "sqlalchemy-utils",
        "requests",
        "eventlet"
    ],
    include_package_data=True
)
