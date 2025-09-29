"""Plugin integration port."""

from __future__ import annotations

from typing import Callable, Dict


class PluginRegistry:
	"""Lightweight plugin manager honouring PB2S validation invariants."""

	def __init__(self) -> None:
		self._entrypoints: Dict[str, Callable[..., object]] = {}

	def register(self, name: str, handler: Callable[..., object]) -> None:
		if name in self._entrypoints:
			raise ValueError(f"Plugin '{name}' already registered")
		self._entrypoints[name] = handler

	def run(self, name: str, *args, **kwargs):
		try:
			handler = self._entrypoints[name]
		except KeyError as exc:
			raise KeyError(f"Plugin '{name}' is not registered") from exc
		return handler(*args, **kwargs)

	def available(self) -> Dict[str, Callable[..., object]]:
		return dict(self._entrypoints)


registry = PluginRegistry()