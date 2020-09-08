# enhancesa

[![Tests](https://github.com/sinablk/enhancesa/workflows/Tests/badge.svg)](https://github.com/sinablk/enhancesa/actions?workflow=Tests)
[![Documentation Status](https://readthedocs.org/projects/enhancesa/badge/?version=latest)](https://enhancesa.readthedocs.io/en/latest/?badge=latest)
[![Codecov](https://codecov.io/gh/sinablk/enhancesa/branch/master/graph/badge.svg)](https://codecov.io/gh/enhancesa/enhancesa)
[![pypi version](https://img.shields.io/pypi/v/enhancesa.svg)](https://pypi.org/project/enhancesa/)
[![git tag](https://img.shields.io/github/tag-pre/sinablk/enhancesa.svg?label=git%20tag)](https://github.com/sinablk/enhancesa/releases)
[![dependencies](https://img.shields.io/librariesio/github/sinablk/enhancesa.svg)](https://libraries.io/github/sinablk/enhancesa)

Enhancesa is a collection of tools for more simplified statistical analysis in Python. It primarily aids in manual analysis and prediction tasks that use packages like [Statsmodels](https://www.statsmodels.org/stable/index.html) and [Scikit-learn](https://scikit-learn.org/stable/index.html) in their workflow.

For example, Enhancesa provides answers to questions like: Which subset of features gives me the lowest error rate in an ordinary least squares model? What are estimates of population mean and standard deviation using bootstrap resampling? And etc.

### Motivation

Enhancesa is a result of solutions to exercises in the book [Introduction to Statistical Learning](https://www-bcf.usc.edu/~gareth/ISL/) by the Tibshirani et al. When going through the exercises, I found Python, unlike R, lacking in providing convenient functionalities. _At this stage_, this package is simply a collection of functions I used in my solutions to exercises in the book.

### Installation

Enhancesa can be installed from the [PyPI](https://pypi.org/project/enhancesa/) package repository.

```
$ pip install enhancesa
```

### Quick glimpse

```python
>>> import numpy as np
>>> import enhancesa as esa
>>> # Create some dummy data
>>> x = np.random.normal(size=100)
>>> # Compute test statistics with bootstrap resampling
>>> esa.bootstrap(x, iters=1000)
Estimated mean: -0.025309
Estimated SE: 0.095531
dtype: float64
```

Find out more about the full set of features in the [documentation](https://enhancesa.readthedocs.io/en/latest/?badge=latest).

### License

This package is licensed under an [MIT](https://github.com/sinablk/enhancesa/blob/master/LICENSE.txt) license.
