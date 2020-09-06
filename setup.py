import io
import os
import re

from setuptools import setup, find_packages


# Utility function to read a given filename.
# This is handy to read the content of any file
# into setup.py, e.g. the README file.
def read(filename):
    filename = os.path.join(os.path.dirname(__file__), filename)
    text_type = type(u"")
    with io.open(filename, mode="r", encoding='utf-8') as fd:
        return re.sub(text_type(r':[a-z]+:`~?(.*?)`'), text_type(r'``\1``'), fd.read())


# A short way to read the contents of README.md
# and then feed into long_description
with open('README.md', 'r') as f:
    long_description = f.read()


# Version info -- read without importing
_locals = {}
with open('enhancesa/_version.py') as fp:
    exec(fp.read(), _locals)
version = _locals["__version__"]


setup(    
    # Metadata used by PyPI.
    name='enhancesa',
    version=version,
    description='Tools for statistical analysis',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/sinablk/enhancesa',
    author='Sina Balkhi',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Framework :: IPython',
        'Framework :: Jupyter',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Education',
        'Topic :: Scientific/Engineering :: Visualization',
    ],
    keywords='statistics mathematics plotting diagnostics analysis',

    # Will show on PyPI page.
    project_urls={
        'Documentation': 'https://enhancesa.readthedocs.io/en/latest/?badge=latest',
        'Source': 'https://github.com/sinablk/enhancesa/',
        'Tracker': 'https://github.com/sinablk/enhancesa/issues',
    },

    # Find package folders.
    packages=find_packages(include=['enhancesa', 'enhancesa.*']),

    # Dependencies
    install_requires=[
        'matplotlib>=3.0.2',
        'statsmodels>=0.9.0',
        'seaborn>=0.9.0',
        'numpy>=1.15.4',
        'pandas>=0.24.0',
        'tqdm>=4.28.1'
    ],

    # Specify which Python versions are supported.
    python_requires='>=3.6',

    # Gets the package data from MANIFEST.in.
    include_package_data=True,

    # Can the package be safely installed and run from a zip file?
    zip_safe=False,

    # What are data file?
    data_files=[('', ['LICENSE.txt', 'setup.cfg'])],

    # Integrate test runs into setuptools with the pytest-runner plugin.
    # Alias created in setup.cfg
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
)
