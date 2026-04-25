from dataclasses import dataclass
from typing import Any

from .base_nodes import Node, Logic

@dataclass
class Boolean(Logic):
    value: bool

    def eval(self, env) -> bool:
        return self.value


@dataclass
class Not(Logic):
    right: Node

    def eval(self, env) -> bool:
        return not bool(self.right.eval(env))


@dataclass
class BinaryLogicOp(Logic):
    left: Node
    right: Node

    @staticmethod
    def operation(left: Any, right: Any) -> bool:
        raise NotImplementedError

    def eval(self, env) -> bool:
        return self.operation(self.left.eval(env), self.right.eval(env))


class Lesser(BinaryLogicOp):
    @staticmethod
    def operation(left: Any, right: Any) -> bool:
        return float(left) < float(right)


class LesserEqual(BinaryLogicOp):
    @staticmethod
    def operation(left: Any, right: Any) -> bool:
        return float(left) <= float(right)


class Larger(BinaryLogicOp):
    @staticmethod
    def operation(left: Any, right: Any) -> bool:
        return float(left) > float(right)


class LargerEqual(BinaryLogicOp):
    @staticmethod
    def operation(left: Any, right: Any) -> bool:
        return float(left) >= float(right)


class Equal(BinaryLogicOp):
    @staticmethod
    def operation(left: Any, right: Any) -> bool:
        return left == right


class NotEqual(BinaryLogicOp):
    @staticmethod
    def operation(left: Any, right: Any) -> bool:
        return left != right


class And(BinaryLogicOp):
    @staticmethod
    def operation(left: Any, right: Any) -> bool:
        return bool(left) and bool(right)


class Or(BinaryLogicOp):
    @staticmethod
    def operation(left: Any, right: Any) -> bool:
        return bool(left) or bool(right)