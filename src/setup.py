#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup, find_packages
except ImportError as ie:
    import ez_setup
    ez_setup.use_setuptools()
    from setuptools import setup, find_packages

# Startup
appname = "luminescence"
appversion = "0.3"

setup(
    name = appname,
    version = appversion,
    author = "Pedro Matiello",
    packages = find_packages(),
    author_email = "pmatiello@gmail.com",
    description = "Luminescence is an application for generating HTML presentations from Markdown sources.",
    license = "MIT",
    keywords = "",
    url = "https://github.com/pmatiello/luminescence",
    long_description = "Luminescence is an application for generating HTML presentations from Markdown sources.",
    install_requires = ['markdown2', 'pyyaml'],
    include_package_data = True,
    package_data = {
        'luminescence':['resource/*'],
    },
    entry_points = {
        'console_scripts': [
            "luminescence = luminescence.ui.cli:luminescence"
        ]
    },
    zip_safe = False,
)
