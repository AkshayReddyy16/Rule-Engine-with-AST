import ast
import operator

def evaluate_condition(condition, user_data):
    # Create a safe environment for evaluation
    safe_dict = {key: value for key, value in user_data.items()}
    
    # Parse the condition using AST
    try:
        tree = ast.parse(condition, mode='eval')
        compiled = compile(tree, filename='<ast>', mode='eval')
        result = eval(compiled, {"__builtins__": None}, safe_dict)
        return result
    except Exception as e:
        print(f"Error evaluating condition '{condition}': {str(e)}")
        return False
