import shlex
from configparser import ConfigParser

import setuptools
from pkg_resources import parse_version

# note: all settings are in settings.ini; edit there, not here
config = ConfigParser(delimiters=['='])
config.read('settings.ini', encoding="utf-8")
cfg = config['DEFAULT']


requirements = shlex.split(cfg.get('requirements', ''))