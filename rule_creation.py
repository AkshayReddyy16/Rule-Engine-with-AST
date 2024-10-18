# rule_creation.py
import ast
from ast_nodes import Node

def create_rule(rule_string):
    """Create an AST from a rule string."""
    def parse_expression(expr):
        # This is a stub; you'll need to implement a proper parser.
        return Node("operand", value=expr.strip())

    expressions = rule_string.split("AND")  # Simplified parsing
    nodes = [parse_expression(exp.strip()) for exp in expressions]

    if len(nodes) == 1:
        return nodes[0]
    else:
        root = Node("operator", left=nodes[0], right=nodes[1])  # Simplified for two operands
        return root
