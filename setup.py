from setuptools import setup

package = 'minimum_viable_pip_package'

setup(
    name=package,
    author='Brian M. Carlson',
    author_email='brian.m.carlson@gmail.com',
    version='0.0.2',
    url='https://github.com/brianc/minimum_viable_pip_package',
    package_dir={
        '': package
    }
)