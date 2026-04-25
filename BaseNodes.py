from typing import Any

class Node:
    """Base class for all AST nodes."""
    def eval(self, env) -> Any:
        raise NotImplementedError

class Numeric(Node):
    pass

class Logic(Node):
    pass

class Void(Node):
    pass