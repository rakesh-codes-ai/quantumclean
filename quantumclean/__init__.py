"""Public package API for QuantumClean."""

from .backends import DuckDBBackend, PandasBackend, SparkBackend, get_backend
from .detectors import IsolationForestDetector, StatisticalOutlierDetector
from .lineage import LineageEvent, LineageTracker
from .schema import Schema
from .scoring import QualityScore, QualityScorer
from .sla import QualitySLA, SLABreach, SLAReport
from .validators import (
    BaseValidator,
    CategoricalValidator,
    EmailValidator,
    NotNullValidator,
    RangeValidator,
    RegexValidator,
    UniqueValidator,
)

__version__ = "1.0.0"

__all__ = [
    "Schema",
    "BaseValidator",
    "NotNullValidator",
    "UniqueValidator",
    "EmailValidator",
    "RangeValidator",
    "RegexValidator",
    "CategoricalValidator",
    "QualityScore",
    "QualityScorer",
    "QualitySLA",
    "SLABreach",
    "SLAReport",
    "LineageEvent",
    "LineageTracker",
    "PandasBackend",
    "DuckDBBackend",
    "SparkBackend",
    "get_backend",
    "StatisticalOutlierDetector",
    "IsolationForestDetector",
    "__version__",
]
