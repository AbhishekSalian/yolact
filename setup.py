#!/usr/bin/env python

from pathlib import Path
from configparser import ConfigParser

from setuptools import setup, find_packages


def get_path(file):
    return Path(__file__).parent / file


def packages_from_pipfile(section):
    pipfile_path = str(get_path('Pipfile'))
    parser = ConfigParser()
    parser.read(pipfile_path)

    result = []
    for k, v in parser[section].items():
        pkg = k if v == '"*"' else '{}=={}'.format(k, v)
        result.append(pkg)
    return result


with get_path('README.md').open() as f:
    readme = f.read()

setup(
    name='yolact',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=packages_from_pipfile('packages'),
    extras_require={
        'develop': packages_from_pipfile('dev-packages'),
    }
)
