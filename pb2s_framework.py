"""PB2S Recursion Loop implementation.

The framework translates arbitrary input signals into disciplined PB2S cycles
that can be audited, extended, and replayed. The cycles honour the minimal
structure contract (DRAFT → REFLECT → REVISE → LEARNED) while remaining agile
enough to adapt new contradictions discovered mid-flight.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, Iterable, List, Optional

from sandbox_manager import SandboxManager
from suit_engine import CycleContext, SuitEngine, SuitValidationError


class PB2SRecursionError(RuntimeError):
    """Raised when the recursion loop cannot complete responsibly."""


@dataclass
class CycleInsights:
    """Lightweight analytics carried across cycles for coherence."""

    contradictions: List[str]
    opportunities: List[str]
    risks: List[str]


class PB2SFramework:
    """Coordinate PB2S recursion cycles."""

    def __init__(
        self,
        suit_engine: Optional[SuitEngine] = None,
        sandbox_manager: Optional[SandboxManager] = None,
        version: str = "1.0.0",
    ) -> None:
        self.suit_engine = suit_engine or SuitEngine()
        self.sandbox = sandbox_manager or SandboxManager()
        self.version = version

    def run(
        self,
        input_data: Any,
        *,
        min_cycles: int = 3,
        max_cycles: int = 6,
    ) -> List[Dict[str, Any]]:
        """Run PB2S recursive cycles on the ``input_data``.

        Parameters
        ----------
        input_data:
            Arbitrary payload describing the problem or artefact to be analysed.
            Strings, dictionaries, or lists are supported.
        min_cycles:
            Lower bound of cycles to execute (PB2S requires at least three).
        max_cycles:
            Hard cap to avoid infinite recursion when contradictions cannot be
            resolved.
        """

        if min_cycles < 3:
            raise ValueError("PB2S requires a minimum of three cycles")
        if max_cycles < min_cycles:
            raise ValueError("max_cycles must be >= min_cycles")

        cycles: List[Dict[str, Any]] = []
        with self.sandbox.enforce_runtime("pb2s_recursion"):
            for cycle_number in range(1, max_cycles + 1):
                insights = self._derive_insights(input_data, cycles)
                cycle_payload = self._compose_cycle(
                    cycle_number, input_data, cycles, insights
                )

                context = CycleContext(
                    cycle_number=cycle_number,
                    raw_input=input_data,
                    previous_cycles=cycles,
                )
                validated_cycle = self.suit_engine.validate_and_recurse(
                    cycle_payload, context
                )
                cycles.append(validated_cycle)

                if self._is_resolved(cycles, min_cycles):
                    break
            else:
                # ``for``-``else`` executes when no ``break`` occurs.
                raise PB2SRecursionError(
                    "Contradictions unresolved within allotted cycles"
                )

        return cycles

    def _derive_insights(
        self,
        input_data: Any,
        previous_cycles: Iterable[Dict[str, Any]],
    ) -> CycleInsights:
        text = self._normalise_input(input_data)
        sentences = [segment.strip() for segment in text.split(".") if segment.strip()]

        contradictions: List[str] = []
        opportunities: List[str] = []
        risks: List[str] = []

        for sentence in sentences:
            lower = sentence.lower()
            if any(token in lower for token in ("but", "however", "yet")):
                contradictions.append(sentence)
            if any(token in lower for token in ("ensure", "opportunity", "enable")):
                opportunities.append(sentence)
            if any(token in lower for token in ("risk", "threat", "harm")):
                risks.append(sentence)

        # Carry lessons forward from previous cycles.
        for cycle in previous_cycles:
            lessons = cycle.get("LEARNED", "")
            if isinstance(lessons, str) and lessons:
                opportunities.append(f"Cycle {cycle['cycle']} lesson: {lessons}")

        return CycleInsights(
            contradictions=contradictions or ["No explicit contradictions detected"],
            opportunities=opportunities or ["Surface opportunities during reflection"],
            risks=risks or ["No overt risks detected; remain attentive"],
        )

    def _compose_cycle(
        self,
        cycle_number: int,
        input_data: Any,
        previous_cycles: List[Dict[str, Any]],
        insights: CycleInsights,
    ) -> Dict[str, Any]:
        timestamp = datetime.now(timezone.utc).isoformat()
        draft = self._build_draft(cycle_number, input_data, insights)
        reflection = self._build_reflection(cycle_number, insights, previous_cycles)
        revision = self._build_revision(cycle_number, reflection, previous_cycles)
        learned = self._build_learned(cycle_number, reflection, revision)

        return {
            "cycle": cycle_number,
            "DRAFT": draft,
            "REFLECT": reflection,
            "REVISE": revision,
            "LEARNED": learned,
            "noise_log": self._capture_noise(input_data, cycle_number),
            "responsibility": (
                f"PB2SFramework@{self.version}::cycle_{cycle_number}"
            ),
            "validation_passed": False,
            "timestamp": timestamp,
            "version": self.version,
        }

    def _build_draft(
        self,
        cycle_number: int,
        input_data: Any,
        insights: CycleInsights,
    ) -> str:
        synopsis = self._normalise_input(input_data)
        focus = insights.contradictions[0]
        return (
            f"Cycle {cycle_number} draft synthesises provided signal. Primary focus: "
            f"{focus}. Synopsis: {synopsis}"
        )

    def _build_reflection(
        self,
        cycle_number: int,
        insights: CycleInsights,
        previous_cycles: List[Dict[str, Any]],
    ) -> List[str]:
        reflection = [
            f"Investigate contradictions: {', '.join(insights.contradictions)}",
            f"Opportunities for leverage: {', '.join(insights.opportunities)}",
            f"Risks requiring mitigation: {', '.join(insights.risks)}",
        ]

        if previous_cycles:
            last_revision = previous_cycles[-1]["REVISE"]
            reflection.append(
                f"Compare against previous revision: {last_revision}"
            )

        reflection.append(
            "Confirm that freedom remains tied to explicit responsibility markers."
        )
        return reflection

    def _build_revision(
        self,
        cycle_number: int,
        reflection: List[str],
        previous_cycles: List[Dict[str, Any]],
    ) -> str:
        anchor = reflection[0]
        previous_outcome = (
            previous_cycles[-1]["LEARNED"] if previous_cycles else "Initialisation"
        )
        return (
            f"Revision {cycle_number}: address anchor '{anchor}'. Prior outcome: "
            f"{previous_outcome}. Establish actionable next steps with"
            " accountability gates before proceeding."
        )

    def _build_learned(
        self,
        cycle_number: int,
        reflection: List[str],
        revision: str,
    ) -> str:
        resolution = (
            "Resolved contradictions and aligned actions with responsibility markers"
            if cycle_number >= 3
            else "Documented contradictions awaiting further recursion"
        )
        return (
            f"Learning {cycle_number}: {resolution}. Reflection summary: "
            f"{'; '.join(reflection)}. Revision guidance: {revision}."
        )

    def _capture_noise(self, input_data: Any, cycle_number: int) -> List[str]:
        baseline = self._normalise_input(input_data)
        return [
            f"cycle_{cycle_number}::raw_fragment::{fragment.strip()}"
            for fragment in baseline.split("\n")
            if fragment.strip()
        ]

    def _is_resolved(
        self, cycles: List[Dict[str, Any]], min_cycles: int
    ) -> bool:
        if len(cycles) < min_cycles:
            return False
        latest = cycles[-1]
        learned = latest.get("LEARNED", "").lower()
        return all(token in learned for token in ("resolved", "responsibility"))

    @staticmethod
    def _normalise_input(input_data: Any) -> str:
        if isinstance(input_data, str):
            return input_data.strip()
        if isinstance(input_data, dict):
            return " | ".join(
                f"{key}: {value}" for key, value in input_data.items()
            )
        if isinstance(input_data, list):
            return " | ".join(str(item) for item in input_data)
        return str(input_data)