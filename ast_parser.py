import ast
import operator as op

# Mapping operators for evaluation
operators = {
    'Add': op.add,
    'Sub': op.sub,
    'Mult': op.mul,
    'Div': op.truediv,
    'Gt': op.gt,
    'Lt': op.lt,
    'Eq': op.eq
}

def eval_expr(expr, user_data):
    """Safely evaluate an expression using user_data."""
    node = ast.parse(expr, mode='eval')

    def _eval(node):
        if isinstance(node, ast.Num):  # Number
            return node.n
        elif isinstance(node, ast.Name):  # Variable
            return user_data.get(node.id, 0)
        elif isinstance(node, ast.BinOp):  # Binary operation
            left = _eval(node.left)
            right = _eval(node.right)
            return operators[type(node.op).__name__](left, right)
        elif isinstance(node, ast.Compare):  # Comparison
            left = _eval(node.left)
            return all(operators[type(op).__name__](left, _eval(comp)) for op, comp in zip(node.ops, node.comparators))

    return _eval(node.body)
