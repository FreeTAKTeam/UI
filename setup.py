from setuptools import setup

setup(
    name='FreeTAKServer-UI',
    version='1.0',
    packages=['app', 'app.base', 'app.home', 'tests'],
    url='https://github.com/FreeTAKTeam/FreeTakServer',
    license='Eclipse License',
    author='Ghost, C0rv0',
    author_email='avc',
    description='fawfwfa',
    install_requires = [
        "flask",
        "flask_login",
        "flask_migrate",
        "flask_wtf",
        "flask_sqlalchemy",
        "email_validator",
        "gunicorn"
    ],
    include_package_data=True
)
