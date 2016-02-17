from setuptools import setup

setup(
    # Application name:
    name="smugmugv2py",

    # Version number (initial):
    version="0.0.1",

    # Application author details:
    author="Andy Hawkins",
    author_email="andy@gently.org.uk",

    # Packages
    packages=["smugmugv2py"],

    # Include additional files into the package
    include_package_data=True,

    # Details
    url="https://github.com/adhawkins/smugmugv2py",

    #
    license="LICENSE.txt",
    description="A Python package for accessing the SmugMug v2 API.",

    long_description=open("README.md").read(),

    # Dependent packages (distributions)
    install_requires=[
        'rauth',
    ],
)
