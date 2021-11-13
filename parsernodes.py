from abc import ABC, abstractmethod
from typing import Union
from dataclasses import dataclass
from visitor import NodeVisitor

class Node:
    def accept(self, visitor: NodeVisitor):
        ...

@dataclass
class ValueNode(Node):
    value_type: str
    value: str
    def accept(self, visitor: NodeVisitor):
        return visitor.visitValueNode(self)

@dataclass
class DefinitionNode(Node):
    variable: str
    value: ValueNode 
    def accept(self, visitor: NodeVisitor):
        return visitor.visitDefinitionNode(self)

@dataclass
class ArgNode:
    type: str
    value: str
    def accept(self, visitor: NodeVisitor):
        return visitor.visitArgNode(self)

@dataclass
class FunctionCallNode(Node):
    name: str
    args: list[ArgNode]
    def accept(self, visitor: NodeVisitor):
        return visitor.visitFunctionCallNode(self)

@dataclass
class ExperimentNode(Node):
    title: str
    statements: list[Union[DefinitionNode, FunctionCallNode]]
    def accept(self, visitor: NodeVisitor):
        return visitor.visitExperimentNode(self)

@dataclass
class PaperNode(Node):
    title: str 
    experiments: list[ExperimentNode] 
    def accept(self, visitor: NodeVisitor):
        return visitor.visitPaperNode(self)

@dataclass
class StartNode(Node):
    papers: list[PaperNode]
    def accept(self, visitor: NodeVisitor):
        return visitor.visitStartNode(self)
