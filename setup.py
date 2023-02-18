from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in notice_board/__init__.py
from notice_board import __version__ as version

setup(
	name="notice_board",
	version=version,
	description="Notice Board of GNDEC.",
	author="Kumar Abhinav",
	author_email="sdc@gndec.ac.in",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
