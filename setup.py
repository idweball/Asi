from setuptools import setup, find_packages

PACKAGE = "Asi"
NAME = "Asi"
DESCRIPTION = "Ansible Api Warpper"
AUTHOR = "loveshell"
AUTHOR_EMAIL = "idweball@gmail.com"
URL = "https://github.com/idweball/Asi"
VERSION = "1.1.3"

setup(
	name=NAME,
	version=VERSION,
	description=DESCRIPTION,
	long_description=open("README.md").read(),
	long_description_content_type="text/markdown",
	author=AUTHOR,
	author_email=AUTHOR_EMAIL,
	license="BSD",
	url=URL,
	packages=find_packages(),
	zip_safe=False,
	install_requires=["ansible>=2.7"]
)
