# rule_combination.py
from ast_nodes import Node  # Import the Node class
from rule_creation import create_rule

def combine_rules(rule_strings):
    """Combine multiple rule strings into a single AST."""
    combined_node = None
    
    for rule in rule_strings:
        current_node = create_rule(rule)
        if combined_node is None:
            combined_node = current_node
        else:
            combined_node = Node("operator", left=combined_node, right=current_node)  # Assuming AND for combination

    return combined_node
