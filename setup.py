from setuptools import setup

setup(
    name='Data Structures',
    package_dir={'': 'src'},
    extras_require={'test': ['pytest', 'pytest-watch', 'tox']}
    )
