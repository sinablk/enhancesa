try:
    from importlib.metadata import version, PackageNotFoundError
except ImportError:   # pragma: no cover
    from importlib_metadata import version, PackageNotFoundError


try:
    __version__ = version(__name__)
except PackageNotFoundError:
    __version__ = 'unknown'

# Import enhancesa objects
from .diag_plots import diag_plots
from .bootstrap import bootstrap
from .subset_selection import SubsetSelect



