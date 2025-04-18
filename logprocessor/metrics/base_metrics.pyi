import abc
from abc import ABC, abstractmethod
from typing import DefaultDict, Self, Iterable, Any


class LogMetrics(ABC, metaclass=abc.ABCMeta):
    @property
    @abstractmethod
    def metrics_template(self) -> list[str]: ...
    metrics: dict[str, DefaultDict[Any, int]]

    def __init__(
        self,
        _metrics: dict[str, DefaultDict[Any, int]] | None = None
    ) -> None: ...
    def __add__(self, other: dict | Self) -> Self: ...
    def to_dict(self) -> dict[str, dict[str, int]]: ...


class LogMetricsTransformer(ABC, metaclass=abc.ABCMeta):
    @property
    @abstractmethod
    def log_metrics(self) -> type[LogMetrics]: ...
    @abstractmethod
    def transform(self, line: str) -> dict[str, dict[Any, int]]: ...
    def bulk_transform(self, lines: Iterable[str]) -> LogMetrics: ...
