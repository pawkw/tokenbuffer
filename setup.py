from setuptools import find_packages, setup

with open('readme.md', 'r') as readme:
    long_description = readme.read()

setup(
    name = 'tokenbuffer',
    version = '0.1',
    description = 'A tokenizer with a handler suitable for making parsers.',
    package_dir = {"": "src"},
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    author = 'pawkw',
    author_email = 'pawkw@users.github.com',
    license = 'MIT',
    classifiers = [
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.10',
        'Operating System :: OS Independent'
    ],
    python_requires = '>=3.10'
)