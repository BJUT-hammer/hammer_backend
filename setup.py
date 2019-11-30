from setuptools import setup, find_packages


setup(
    name='hammer-api',
    version='1.0',
    description='Hammer Api',
    packages=find_packages(),
    install_requires=[
        'Django==1.11.23',
        'djangorestframework',
        'requests',
        'pytest',
        'pytest-django',
        'mysqlclient',
        'django-rest-swagger',
        'django-extensions',
        'netifaces',
        'ipaddress',
        'supervisor',
        'gunicorn',
        'django-filter==1.1.0',
        'pytz',
        'django-jsonfield',
    ],
    classifiers=[
        'Programming Language :: Python',
    ],
)
