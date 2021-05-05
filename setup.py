from setuptools import setup, find_packages

setup(
  name='box-maker',
  version='0.1',
  install_requires=[
    'Click',
  ],
  packages=find_packages(
    where='src',
  ),
  package_dir={"": "src"},
  include_package_data=True,
  entry_points='''
    [console_scripts]
    box-maker=box_maker.scripts.cli:entry
    box-maker-test=box_maker.scripts.cli:test
  ''',
)
