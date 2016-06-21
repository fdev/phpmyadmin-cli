import os
from setuptools import setup, find_packages

description = "A phpMyAdmin command-line interface."
cur_dir = os.path.dirname(__file__)
try:
	long_description = open(os.path.join(cur_dir, 'README.md')).read()
except:
	long_description = description

setup(
	name = "phpmyadmin-cli",
	version = "1.0",
	url = 'http://github.com/fdev/phpmyadmin-cli/',
	license = 'GPL2',
	description = description,
	long_description = long_description,
	author = 'Folkert de Vries',
	author_email = 'phpmyadmin-cli@fdev.nl',
	packages = find_packages('src'),
	package_dir = {'': 'src'},
	install_requires = ['requests', 'PTable'],
	entry_points="""
	[console_scripts]
	phpmyadmin-cli = phpmyadmincli:main
	""",
	classifiers=[
		'Development Status :: 4 - Beta',
		'Environment :: Console',
		'Intended Audience :: Developers',
		'Intended Audience :: System Administrators',
		'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
		'Operating System :: MacOS :: MacOS X',
		'Operating System :: Unix',
		'Operating System :: POSIX',
		'Programming Language :: Python',
		'Topic :: Database :: Front-Ends',
	]
)
