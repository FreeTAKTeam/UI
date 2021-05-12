from setuptools import setup

setup(
    name='FreeTAKServer-UI',
    version='0.1.7.9',
    packages=['app', 'app.base', 'app.home', 'tests'],
    url='https://github.com/FreeTAKTeam/FreeTakServer',
    license='Eclipse License',
    author='Ghost, C0rv0',
    author_email='your.email@domain.com',
    description='an optional UI for FreeTAKServer',
    install_requires = [
        "flask",
        "flask_login",
        "flask_migrate",
        "flask_wtf",
        "flask_sqlalchemy",
        "email_validator",
        "gunicorn",
        "python-decouple",
        "sqlalchemy-utils"
    ],
    include_package_data=True
)
