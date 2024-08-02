from setuptools import find_packages, setup

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in lms/__init__.py
from lms import __version__ as version

setup(
	name="xrm",
	version=version,
	description="xrm App",
	author="Apper",
	author_email="",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires,
)
