try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'Backing up folders as zip archives without doing the work yourself.',
	'author': 'Sunny Lam',
	'url': 'URL to get it at',
	'download_url': 'Where to download it',
	'author_email': 'sunny.lam@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['zipfile, os'],
	'scripts': [],
	'name': 'Rapid Backup to Zip'
}

setup(**config)