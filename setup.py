import pathlib
from setuptools import setup

CURRENT_DIRECTORY = pathlib.Path(__file__).parent

README = (CURRENT_DIRECTORY / "README.md").read_text()

setup(
    name="python-netdiscover",
    version="1.0",
    description="python-netdiscover is a simple wrapper for the netdiscover reconnaissance tool",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/MrSuicideParrot/python-netdiscover",
    author="André Cirne",
    author_email="ancirne@gmail.com",
    license="GPL-3",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Intended Audience :: System Administrators",
        "Topic :: System :: Monitoring",
        "Topic :: System :: Networking",
        "Topic :: System :: Networking :: Firewalls",
        "Topic :: System :: Networking :: Monitoring",
    ],
    keywords="network, netdiscover, arpscanner, sysadmin",
    packages=['netdiscover'],
    include_package_data=True,
)
