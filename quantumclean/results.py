"""Validation result models used by validators and schemas."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class ValidationResult:
    column: str
    validator: str
    total: int
    failed_indices: List[int] = field(default_factory=list)

    @property
    def failed(self) -> int:
        return len(self.failed_indices)

    @property
    def passed(self) -> int:
        return self.total - self.failed

    @property
    def is_valid(self) -> bool:
        return self.failed == 0

    @property
    def pass_rate(self) -> float:
        if self.total == 0:
            return 1.0
        return self.passed / self.total

    def to_dict(self) -> Dict[str, object]:
        return {
            "column": self.column,
            "validator": self.validator,
            "total": self.total,
            "passed": self.passed,
            "failed": self.failed,
            "pass_rate": round(self.pass_rate, 4),
            "failed_indices": list(self.failed_indices),
        }


@dataclass
class SchemaResult:
    results: List[ValidationResult] = field(default_factory=list)

    @property
    def is_valid(self) -> bool:
        return all(r.is_valid for r in self.results)

    @property
    def pass_rate(self) -> float:
        total = sum(r.total for r in self.results)
        if total == 0:
            return 1.0
        passed = sum(r.passed for r in self.results)
        return passed / total

    def failures(self) -> List[ValidationResult]:
        return [r for r in self.results if not r.is_valid]

    def to_dict(self) -> Dict[str, object]:
        return {
            "is_valid": self.is_valid,
            "pass_rate": round(self.pass_rate, 4),
            "results": [r.to_dict() for r in self.results],
        }

    def summary(self) -> str:
        status = "PASS" if self.is_valid else "FAIL"
        return (
            f"Schema validation: {status} "
            f"({len(self.results) - len(self.failures())}/{len(self.results)} checks passed)"
        )
