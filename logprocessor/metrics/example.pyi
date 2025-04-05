"""
Example typing for custom log formats.

This file is OPTIONAL but use is encouraged
because it makes autocompletion in things
like VS Code work a lot better.

These files are very simple and can just
be copy-pasted for the most part unless you
have added custom functions to your subclasses.

If you DO have custom functions, please see
the mypy Type hints cheat sheet at
https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
"""

from .base_metrics import LogMetrics, LogMetricsTransformer


class ExampleMetrics(LogMetrics):
    metrics_template: list[str]


class BareMetricsTransformer(LogMetricsTransformer):
    log_metrics: type[ExampleMetrics]
    def transform(self, line: str) -> dict[str, dict[str | tuple, int]]: ...
