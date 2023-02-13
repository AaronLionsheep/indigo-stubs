import os

from setuptools import setup, find_packages


def list_packages(src_path=""):
    for root, _, _ in os.walk(os.path.join(src_path, "indigo-stubs")):
        yield ".".join(os.path.relpath(root, src_path).split(os.path.sep))


setup(
    name='indigo-stubs',
    version='3.0.0',
    url='https://github.com/mypackage.git',
    author='Author Name',
    author_email='author@gmail.com',
    description='Description of my package',
    install_requires=[],
    packages=list(list_packages()),
    package_data={"": ["*.pyi"]},
)
