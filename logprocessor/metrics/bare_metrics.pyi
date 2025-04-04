from .base_metrics import LogMetrics, LogMetricsTransformer

class BareMetrics(LogMetrics):
    metrics_template: list[str]

class BareMetricsTransformer(LogMetricsTransformer):
    log_metrics: type[BareMetrics]
    def transform(self, line: str) -> dict[str, dict[str | tuple, int]]: ...