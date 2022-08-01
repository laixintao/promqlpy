# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['promqlpy']

package_data = \
{'': ['*']}

install_requires = \
['cffi>=1.15.1,<2.0.0']

setup_kwargs = {
    'name': 'promqlpy',
    'version': '0.1.0',
    'description': 'Python utils for parsing PromQL/MetricsQL.',
    'long_description': None,
    'author': 'laixintao',
    'author_email': 'laixintaoo@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}
from build import *
build(setup_kwargs)

setup(**setup_kwargs)
