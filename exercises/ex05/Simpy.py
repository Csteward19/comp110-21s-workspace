"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730404260"


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
    
    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Produces a mask that compares values to a specific value."""
        mask1: list[bool] = []
        if isinstance(rhs, float):
            for val in self.values:
                if val == rhs:
                    mask1.append(True)
                else:
                    mask1.append(False)
        else:
            assert len(self.values) == len(rhs.values)
            for val in range(len(self.values)):
                if self.values[val] == rhs.values[val]:
                    mask1.append(True)
                else:
                    mask1.append(False)
        return mask1
    
    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Sees if a value is larger than a float and produces a mask."""
        mask1: list[bool] = []
        if isinstance(rhs, float):
            for val in self.values:
                if val > rhs:
                    mask1.append(True)
                else:
                    mask1.append(False)
        else:
             assert len(self.values) == len(rhs.values)
             for i in range(len(self.values)):
                if self.values[i] == rhs.values[i]:
                        mask1.append(True)
                else:
                    mask1.append(False)
        return mask1

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """This does subscription notation on values."""
        if isinstance(rhs, int):
            for val in range(len(self.values)):
                if val == rhs:
                    return self.values[val]
        else:
            empty_list: list[float] = []
            for sub in range(len(self.values)):
                if rhs[sub] is True:
                    empty_list.append(self.values[sub])
        return Simpy(empty_list)