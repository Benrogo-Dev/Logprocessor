import pytest
from logprocessor.metrics.base_metrics import LogMetrics

class ValidMetricsClass1(LogMetrics):
    metrics_template = ["metric"]

class ValidMetricsClass2(LogMetrics):
    metrics_template = ["othermetric"]

class InvalidMetricsClass(LogMetrics):
    ... # Missing metrics_template


# Test that valid LogMetrics subclasses do
# not raise exceptions on initialization.
def test_metrics_init():
    ValidMetricsClass1()

# Test that an exception is thrown
# when a metrics template is not defined.
def test_no_template():
    with pytest.raises(TypeError):
        InvalidMetricsClass()
    
# Test that invalid types cannot be
# added to LogMetrics objects.
def test_invalid_addition():
    new_metrics_1 = ValidMetricsClass1()
    new_metrics_2 = ValidMetricsClass2()
    with pytest.raises(TypeError):
        new_metrics_1 + 1
    with pytest.raises(TypeError):
        new_metrics_1 + new_metrics_2