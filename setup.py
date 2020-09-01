from setuptools import setup
setup(
    name = 'randomstring',
    version = '1.0',
    packages = ['randomstring'],
    entry_points = {
        'console_scripts': [
            'randomstring = randomstring.main:main'
        ]
    })