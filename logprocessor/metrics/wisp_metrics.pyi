from .base_metrics import LogMetrics, LogMetricsTransformer

class WispMetrics(LogMetrics):
    metrics_template: list[str]

class WispMetricsTransformer(LogMetricsTransformer):
    log_metrics: type[WispMetrics]
    def transform(self, line: str) -> dict[str, dict[str | tuple, int]]: ...