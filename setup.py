from setuptools import setup, find_packages
import os
import sys
import io
import path

version = '0.1.7'

# Read the readme file contents into variable
if sys.argv[-1] == 'publish' or sys.argv[-1] == 'publishtest':
    os.system('pandoc README.md -f markdown -t rst -s -o README.txt')

readme_file = io.open('README.txt', encoding='utf-8')

# Fallback long_description in case errors with readme file.
long_description = "Welcome to Pyleoclim. Please reference the README file in the package for information"
with readme_file:
    long_description = readme_file.read()

# Publish the package to the live server
if sys.argv[-1] == 'publish':
    # Register the tarball, upload it, and trash the temp readme rst file
    os.system('python setup.py register -r pypi')
    os.system('python setup.py sdist upload -r pypi')
    os.remove('README.txt')
    sys.exit()

# Publish the package to the test server
elif sys.argv[-1] == 'publishtest':
    # Create dist tarball, register it to test site, upload tarball, and remove temp readme file
    os.system('python setup.py register upload -r pypitest')
    os.system('python setup.py sdist upload -r pypitest')
    # Trash the temp rst readme file
    os.remove('README.txt')
    sys.exit()

setup(
    name = 'Pyleoclim',
    packages = find_packages(),
    version = version,
    license = 'GNU Public',
    description = 'A Python package for paleoclimate data analysis',
    long_description=long_description,
    author = 'Deborah Khider',
    author_email = 'dkhider@gmail.com',
    url = 'https://github.com/LinkedEarth/Pyleoclim_util/Pyleoclim',
    download_url = 'https://github.com/LinkedEarth/Pyleoclim_util/Pyleoclim/tarball/0.1',
    keywords = ['Paleoclimate, Data Analysis'],
    classifiers = [],
    install_requires = [
    "LiPD>=0.1.2.7",
    "pandas>=0.18.1",
    "numpy>=1.11.0",
    "matplotlib>=1.5.1",
    ]
)