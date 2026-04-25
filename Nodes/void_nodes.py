from dataclasses import dataclass
from typing import Any

from Type import Type
from .base_nodes import Void, Numeric, Node


@dataclass
class Print(Void):
    """Prints the value to console"""
    expression: Node

    def eval(self, env) -> None:
        print(self.expression.eval(env))


@dataclass
class Assignment(Void):
    """Checks for the only two types that can be assigned: float or bool"""
    id_name: str
    expression: Node
    line: int

    def eval(self, env) -> None:
        result = self.expression.eval(env)

        if isinstance(self.expression, Numeric):
            _type = Type.NUMBER
            value = float(result)
        else:
            _type = Type.BOOLEAN
            value = bool(result)

        if not env.set(self.id_name, _type, value):
            raise Exception(f"Line {self.line} - Variable '{self.id_name}' was not declared")


@dataclass
class Sequence(Void):
    """Allows for sequential assignments"""
    statements: list[Void]

    def eval(self, env) -> None:
        for stmt in self.statements:
            stmt.eval(env)