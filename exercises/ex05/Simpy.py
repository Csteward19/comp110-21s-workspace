"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "YOUR PID HERE"


class Simpy:
    values: list[float]

    # TODO: Your constructor and methods will go here.
    def __init__(self, values: list[float]):
        self.values = values
    
    def __repr__(self):
        return f"{self.values}"
    
    def fill(self, fill_values: float, numb_times: int) -> None:
        if len(self.values) > 0:
            for val in range(0, len(self.values)):
                self.values.pop()
    
        i = 0
        while i < numb_times:
            self.values.append(fill_values)
            i += 1

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        assert step != 0.0
        if len(self.values) > 0:
            for val in range(0, len(self.values)):
                self.values.pop()
        i: float = 0.0
        while i < (stop - start) / step:
            self.values.append(start + (i * step))
            i += 1

    def sum(self) -> float:
        answer: float = 0.0
        for val in self.values:
            answer += val
        return answer

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        answer = Simpy([])
        if isinstance(rhs, float):
            for i in self.values:
                answer.values.append(i + rhs)
        else:
            assert len(rhs.values) == len(self.values)
            i = 0
            while i < len(self.values):
                answer.values.append(rhs.values[i] + self.values[i])
                i += 1
        return answer

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        answer = Simpy([])
        if isinstance(rhs, float):
            for i in self.values:
                answer.values.append(i ** rhs)
        else:
            assert len(rhs.values) == len(self.values)
            i = 0
            while i < len(self.values):
                answer.values.append(self.values[i] ** rhs.values[i])
                i += 1
        return answer

    def __mod__(self, rhs: Union[float, Simpy]) -> Simpy:
        answer = Simpy([])
        if isinstance(rhs, float):
            for i in self.values:
                answer.values.append(i % rhs)
        else:
            assert len(rhs.values) == len(self.values)
            i = 0
            while i < len(self.values):
                answer.values.append(rhs.values[i] % self.values[i])
                i += 1
        return answer

    