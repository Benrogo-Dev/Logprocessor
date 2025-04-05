"""
Example metrics format and transformer.

This gives some examples of how to use LogMetrics
and LogMetricsTransformer as base classes for
your own custom log formats.

Please see "example.pyi" for an example of
how to use typing for your own formats.
"""

from .base_metrics import LogMetrics, LogMetricsTransformer
import orjson


class ExampleMetrics(LogMetrics):
    """Example metrics

    metrics_template should be a list of
    the names of the metrics you wish to
    count.
    """

    metrics_template = [
        "metric_name_1",
        "metric_name_2"
    ]


class BareMetricsTransformer(LogMetricsTransformer):
    """Example log metrics transformer

    LogMetricsTransformer classes are meant
    to take the lines of a log file and convert
    them into values that can be added to a
    LogMetrics object.

    ANY logic that can be implemented in Python
    can be used to extract the values from each
    line of a log, meaning you can add support
    for any format you can think of!
    """

    log_metrics = ExampleMetrics

    def transform(self, line):
        line_json = orjson.loads(line)

        # In this example, a JSON-based log format is
        # used. Each line would look something like this:
        # {"field_1": "item_1", "field_2": "item_2"}
        # This may look complicated, but all it does is
        # count the number of times field_x is set to item_x.
        # For example, {"field_1": "item_1"}
        # would be converted to {"metric_name_1": {"item_1": 1}}
        # These counters do not have to be incremented by 1.
        # For example, you could get the name from one field
        # and the value from another, such as:
        # {"server_id": "srv-01", "bytes_in": 123}
        # which could be converted to:
        # {"server_bytes_in": {"srv-01": 123}}
        return {
            "metric_name_1": {line_json.get("field_2", "UNKNOWN"): 1},
            "metric_name_2": {line_json.get("field_2", "UNKNOWN"): 1},
        }
