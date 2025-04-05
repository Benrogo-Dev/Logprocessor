import pytest
from logprocessor.metrics.base_metrics import LogMetrics, LogMetricsTransformer

class ValidMetricsClass(LogMetrics):
    metrics_template = ["metric"]

class ValidMetricsTransformerClass(LogMetricsTransformer):
    log_metrics = ValidMetricsClass
    def transform(self, line):
        return {}

class MissingMetricsTransformerClass(LogMetricsTransformer):
    def transform(self, line):
        return {}

class MissingTransformTransformerClass(LogMetricsTransformer):
    log_metrics = ValidMetricsClass


# Test that valid LogMetricsTransformer
# subclasses do not raise exceptions on
# initialization.
def test_transformer_init():
    ValidMetricsTransformerClass()
    
# Test that an exception is thrown when
# log_metrics or transform() is not defined.
def test_missing_processor_definitions():
    with pytest.raises(TypeError):
        MissingMetricsTransformerClass()
    with pytest.raises(TypeError):
        MissingTransformTransformerClass()