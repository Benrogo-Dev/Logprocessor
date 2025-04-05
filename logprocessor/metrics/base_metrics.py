"""
This script contains the base classes LogMetrics and
LogMetricsTransformer.

These classes are meant to be used as a base for custom
log formats (and cannot be used directly).

Example usage and documentation for processing custom
log formats can be found in example.py under the same
directory as this script.

Including typing (found in the .pyi files) for custom
formats is optional but encouraged. A typing example
can be found in example.pyi under the same directory
as this script.
"""

from abc import ABC, abstractmethod
from collections import defaultdict
from ..libs.fast_metric_merge import fast_merge

class LogMetrics(ABC):
    """LogMetrics base class.
    
    This class provides a standard way to create log metrics
    classes using inheritance.
    
    Log metrics subclass objects can be added with regular
    addition operations.
    """

    @property
    @abstractmethod
    def metrics_template(cls): ...
    
    def __init__(self, _metrics = None):
        if _metrics is None:
            self.metrics = {
                name: defaultdict(int) for name in self.metrics_template
            }
        else:
            self.metrics = _metrics
    
    def __add__(self, other):
        if other.__class__ is self.__class__:
            other_metrics = other.metrics
        elif other.__class__ is dict:
            other_metrics = other
        else:
            raise TypeError(
                f"objects of type '{other.__class__.__name__}' can not be added to a LogMetrics object. "
                "Only other LogMetrics objects of the same type or dictionary objects may be added."
            )
        results = self.metrics
        fast_merge(other_metrics, results)
        return type(self)(_metrics=results)
    
    def __repr__(self):
        return f"{self.__class__.__name__}({len(self.metrics)} metrics)"
    
    def to_dict(self):
        """Return metrics as nested dictionary objects"""
        return {key: dict(value) for key, value in self.metrics.items()}

class LogMetricsTransformer(ABC):
    """LogMetricsTransformer base class.
    
    This class simply serves as the base class for
    log metrics transformers.
    
    A LogMetrics class type must be defined for the
    `log_metrics` property and a callable `transform`
    function must be defined for single-line conversions.
    """
    
    @property
    @abstractmethod
    def log_metrics():
        """LogMetrics class type used in the bulk_transform
        function.
        """
    
    @abstractmethod
    def transform(self, line):
        """Format-specific log data transformation function.
        
        This function should be made to process a single
        line of the desired log format.
        """
    
    def bulk_transform(self, lines):
        """Bulk transform function.

        This uses the transform
        function to process each line in a given list and
        stores the metrics in an instance of the specified
        LogMetrics class.
        """
        metrics = self.log_metrics()
        for line in lines:
            metrics += self.transform(line)
        return metrics