# Rule Engine with AST - Internship Program Submission

## Objective
The goal of this project is to develop a 3-tier rule engine application with a simple UI, API, and backend. The application determines user eligibility based on attributes such as age, department, income, spend, etc. The rules governing eligibility are represented using an Abstract Syntax Tree (AST), which allows dynamic creation, combination, and modification of these rules.

---

## Table of Contents
1. [Objective](#objective)
2. [Data Structure](#data-structure)
3. [Data Storage](#data-storage)
4. [API Design](#api-design)
5. [Test Cases](#test-cases)
6. [Bonus Features](#bonus-features)
7. [Non-Functional Requirements](#non-functional-requirements)
8. [How to Run the Application](#how-to-run-the-application)
9. [GitHub Usage](#github-usage)
10. [Contribution](#contribution)
11. [License](#license)

---

## 1.Project Overview
The rule engine allows users to define and modify rules dynamically using an AST structure. The application can:
- Create and store conditional rules based on user attributes.
- Combine rules into a single AST.
- Evaluate these rules against user-provided data.
- Store and retrieve rules from a MySQL database.
---
## Technologies Used
- **Backend Framework**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript (if applicable)
- **Database**: flask_sqlalchemy
- **Other Libraries**:
  - SQLAlchemy (ORM)
  - Werkzeug (for API)
  - Jinja2 (for templating)
## 2. Data Structure
The application uses a `Node` structure to represent the AST:

```python
class Node:
    def __init__(self, node_type, left=None, right=None, value=None):
        self.type = node_type  # "operator" or "operand"
        self.left = left       # Reference to left child Node
        self.right = right     # Reference to right child Node
        self.value = value     # Optional value for operand nodes
```


## 3. Data Storage
The application employs SQLite as the database to store rules and application metadata. Below is the schema:
```sql
CREATE TABLE rules (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    rule_string TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
```
sample rules
```sql
INSERT INTO rules (rule_string) VALUES
    ("((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)"),
    ("((age > 30 AND department = 'Marketing')) AND (salary > 20000 OR experience > 5)");
```

---
## 4. API Design

The following API functions are provided:

### 1. Create Rule
- **Function:** `create_rule(rule_string)`
- **Description:** Takes a rule string and returns a Node object representing the Abstract Syntax Tree (AST).
  
### 2. Combine Rules
- **Function:** `combine_rules(rules)`
- **Description:** Combines a list of rule strings into a single AST, optimizing for efficiency.

### 3. Evaluate Rule
- **Function:** `evaluate_rule(json_data)`
- **Description:** Evaluates the AST against provided attribute data, returning `True` or `False` based on the evaluation result.
  
## 5. Test Cases

1. **Create Individual Rules:** 
   - Create individual rules from the examples using `create_rule` and verify their AST representation.

2. **Combine Rules:** 
   - Combine the example rules using `combine_rules` and ensure the resulting AST reflects the combined logic.

3. **Evaluate Rules:** 
   - Implement sample JSON data and test `evaluate_rule` for different scenarios.

4. **Explore Additional Rules:** 
   - Explore combining additional rules and test the functionality.

## 6. Bonus Features

- **Error Handling:** 
  - Implements error handling for invalid rule strings or data formats.

- **Validations:** 
  - Ensures attributes are validated against a defined catalog.

- **Rule Modification:** 
  - Allows modification of existing rules.

- **User-Defined Functions:** 
  - Support for advanced conditions (planned for future enhancements).
## 7. Non-Functional Requirements

- **Security:** 
  - Implement security measures, including protection against SQL injection.

- **Performance:** 
  - Optimize rule evaluation with caching mechanisms.

- **Scalability:** 
  - Design the application to scale with increased loads.

## 8. Setup and Installation

###  Clone the Repository
```bash
git clone https://github.com/AkshayReddyy16/Rule-Engine-with-AST.git
cd Rule-Engine-with-AST
```
###  Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate      # For Windows
```
### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
### 4. Run the Application:
```bash
python app.py  # Replace with the main script of the application
```
### 5. Access the API: Use tools like Postman or cURL to test the API endpoints
The application should now be available at http://127.0.0.1:5000.

### Rule Engine API Endpoints

Here are the primary API endpoints for the rule engine:

### Create Rule

- **Endpoint:** `/create_rule`
- **Method:** POST
- **Description:** Accepts a string representing a rule and returns an AST.

### Combine Rules

- **Endpoint:** `/combine_rules`
- **Method:** POST
- **Description:** Combines a list of rules into a single AST.
## 9. GitHub Usage
This project is hosted on GitHub. You can find the codebase at [https://github.com/AkshayReddyy16/Rule-Engine-with-AST](https://github.com/AkshayReddyy16/Rule-Engine-with-AST). 

To contribute to the project, please fork the repository and submit a pull request with your changes. Ensure your code is well-documented and adheres to the project's coding standards.

## 10. Contribution
Contributions are welcome! If you'd like to contribute to this project, please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with descriptive messages.
4. Push your changes to your forked repository.
5. Submit a pull request to the main repository for review.

For larger changes, consider opening an issue first to discuss your ideas or improvements with the maintainers.




