# tests/test_rule_engine.py
import unittest
from rule_evaluation import evaluate_condition  # Ensure this import is correct

class RuleEngineTestCase(unittest.TestCase):
    def test_evaluate_condition(self):
        user_data = {"age": 35, "department": "Sales"}

        # Evaluate the first condition
        result = evaluate_condition("age > 30", user_data)
        print(f"Result of 'age > 30': {result}")
        self.assertTrue(result)  # Should be True

        # Evaluate the second condition
        result = evaluate_condition("age < 30", user_data)
        print(f"Result of 'age < 30': {result}")
        self.assertFalse(result)  # Should be False

        # Evaluate the third condition
        result = evaluate_condition('department == "Sales"', user_data)  # Change here
        print(f"Result of 'department == \"Sales\"': {result}")
        self.assertTrue(result)  # Should be True

        # Evaluate the fourth condition
        result = evaluate_condition('department == "Marketing"', user_data)  # Change here
        print(f"Result of 'department == \"Marketing\"': {result}")
        self.assertFalse(result)  # Should be False

if __name__ == '__main__':
    unittest.main()
