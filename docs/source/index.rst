.. enhancesa documentation master file, created by
   sphinx-quickstart on Wed Mar  6 19:30:32 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to enhancesa's documentation!
=====================================

.. image:: https://github.com/sinablk/enhancesa/workflows/Tests/badge.svg
    :target: https://github.com/sinablk/enhancesa/actions?workflow=Tests
    :alt: build
.. image:: https://img.shields.io/librariesio/github/sinablk/enhancesa.svg
    :target: https://libraries.io/github/sinablk/enhancesa
    :alt: dependencies
.. image:: https://codecov.io/gh/sinablk/enhancesa/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/sinablk/enhancesa
    :alt: codecov
.. image:: https://img.shields.io/pypi/v/enhancesa.svg
    :target: https://pypi.org/project/enhancesa/
    :alt: pypi-version
.. image:: https://img.shields.io/pypi/pyversions/enhancesa.svg
    :alt: python-versions


Enhancesa is a collection of tools for more simplified statistical
analysis in Python. It primarily aids in manual analysis and prediction tasks
that use packages like `Statsmodels <https://www.statsmodels.org/stable/index.html>`_
and `Scikit-learn <https://scikit-learn.org/stable/index.html>`_ in their workflow. 

For example, Enhancesa provides answers to questions like: Which subset of
features gives me the lowest error rate in an ordinary least squares model?
What are estimates of population mean and standard deviation using bootstrap
resampling? And etc.


.. toctree::
   :maxdepth: 1
   :caption: Contents:
   :name: mastertoc

   guide
   module_ref
   license
   

Installation
^^^^^^^^^^^^

Enhancesa can be installed from the `PyPI <https://pypi.org/project/enhancesa/>`_
package repository.

.. code:: bash

    $ pip install enhancesa

Alternatively, you can download it from the `source on Github. <https://github.com/sinablk/enhancesa>`_


Quick glimpse
^^^^^^^^^^^^^
.. code-block:: python

    >>> import numpy as np
    >>> import enhancesa as esa
    >>> # Create some dummy data
    >>> x = np.random.normal(size=100)
    >>> # Compute test statistics with bootstrap resampling
    >>> esa.bootstrap(x, iters=1000)
    Estimated mean: -0.025309
    Estimated SE: 0.095531
    dtype: float64


Upcoming features
^^^^^^^^^^^^^^^^^

* Partial least squares (PLS) regression
* Principal components regression (PCR)
* Subset selection plots
* Additional test statistics in bootstrap resampling


License
^^^^^^^
This package is licensed under an `MIT <https://opensource.org/licenses/MIT>`_ license.
