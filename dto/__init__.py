"""
The :mod:`dtosmote` provides the implementation of
Delaunay Thetraedral Oversampling SMOTE algorithm.
"""

from .dto_smote import DTO
from ._version import __version__

__all__ = ['DTO', '__version__']