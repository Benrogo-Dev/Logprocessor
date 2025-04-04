from .base_metrics import LogMetrics, LogMetricsTransformer
from user_agents import parse as parse_agent # type: ignore
import orjson

class BareMetrics(LogMetrics):
    """Bare proxy log metrics"""

    metrics_template = [
        "ip_metrics",
        "host_metrics",
        "source_metrics",
        "status_metrics",
        "bare_version_metrics",
        "user_browser_metrics",
        "user_os_metrics",
        "user_device_metrics",
        "bytes_in",
        "bytes_out",
        "total_requests"
    ]

class BareMetricsTransformer(LogMetricsTransformer):
    """Bare proxy log metrics transformer"""

    log_metrics = BareMetrics

    def transform(self, line):
        line_json = orjson.loads(line)
        
        backend_id = line_json.get("backend_id", "UNKNOWN")
        
        user_agent = parse_agent(line_json.get("user_agent", ""))
        user_browser = (
            user_agent.browser.family or "UNKNOWN",
            user_agent.browser.version_string or "UNKNOWN"
        )
        user_os = (
            user_agent.os.family or "UNKNOWN",
            user_agent.os.version or "UNKNOWN"
        )
        user_device = (
            user_agent.device.brand or "UNKNOWN",
            user_agent.device.model or "UNKNOWN"
        )
        
        return {
            "ip_metrics": {line_json.get("ip", "UNKNOWN"): 1},
            "host_metrics": {line_json.get("host", "UNKNOWN"): 1},
            "source_metrics": {line_json.get("source_site", "DIRECT"): 1},
            "status_metrics": {line_json.get("status", 0): 1},
            "bare_version_metrics": {line_json.get("bare_version", 0): 1},
            "user_browser_metrics": {user_browser: 1},
            "user_os_metrics": {user_os: 1},
            "user_device_metrics": {user_device: 1},
            "bytes_in": {backend_id: line_json.get("bytes_in", 0)},
            "bytes_out": {backend_id: line_json.get("bytes_out", 0)},
            "total_requests": {backend_id: 1}
        }