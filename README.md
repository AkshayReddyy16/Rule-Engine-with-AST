# Rule Engine with AST - Internship Program Submission

## Objective
The goal of this project is to develop a 3-tier rule engine application with a simple UI, API, and backend. The application determines user eligibility based on attributes such as age, department, income, spend, etc. The rules governing eligibility are represented using an Abstract Syntax Tree (AST), which allows dynamic creation, combination, and modification of these rules.

---

## Table of Contents
1. [Project Overview](#project-overview)
2. [Technologies Used](#technologies-used)
3. [Setup and Installation](#setup-and-installation)
4. [Running the Application](#running-the-application)
5. [API Endpoints](#api-endpoints)
6. [Database Setup](#database-setup)
7. [Testing](#testing)
8. [Bonus Features](#bonus-features)
9. [Security and Performance](#security-and-performance)
10. [Contributing](#contributing)
11. [License](#license)

---

## Project Overview
The rule engine allows users to define and modify rules dynamically using an AST structure. The application can:
- Create and store conditional rules based on user attributes.
- Combine rules into a single AST.
- Evaluate these rules against user-provided data.
- Store and retrieve rules from a MySQL database.
---
Sample rules:
- rule1 = "((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)"
- rule2 = "((age > 30 AND department = 'Marketing')) AND (salary > 20000 OR experience > 5)"


## Technologies Used
- **Backend Framework**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript (if applicable)
- **Database**: MySQL (using Docker for containerized setup)
- **Other Libraries**:
  - SQLAlchemy (ORM)
  - Werkzeug (for API)
  - Jinja2 (for templating)

---

## Setup and Installation

###  Clone the Repository
```bash
git clone https://github.com/AkshayReddyy16/Rule-Engine-with-AST.git
cd Rule-Engine-with-AST
Marketing')) AND (salary > 20000 OR experience > 5)"
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
##  Database Setup Using Docker
1. Pull and run MySQL using Docker:
```bash
docker run --name mysql-container \
  -e MYSQL_ROOT_PASSWORD=rootpassword \
  -e MYSQL_DATABASE=mydatabase \
  -e MYSQL_USER=myuser \
  -e MYSQL_PASSWORD=mypassword \
  -p 3306:3306 \
  -d mysql:latest
```
2. Connect to the MySQL container:
   ```bash
   winpty docker exec -it mysql-container mysql -u root -p
  ```
```
3. Create the necessary tables by running the SQL script provided in db_setup.sql.
##  Set up Environment Variables
Create a .env file and set the following:
```env
DATABASE_URI=mysql+pymysql://myuser:mypassword@localhost/mydatabase
FLASK_APP=app.py
FLASK_ENV=development
```
### Running the Application
To run the Flask application:
```bash
flask run
```
The application should now be available at http://127.0.0.1:5000.

# Rule Engine API Endpoints

Here are the primary API endpoints for the rule engine:

## Create Rule

- **Endpoint:** `/create_rule`
- **Method:** POST
- **Description:** Accepts a string representing a rule and returns an AST.

## Combine Rules

- **Endpoint:** `/combine_rules`
- **Method:** POST
- **Description:** Combines a list of rules into a single AST.

## Evaluate Rule

- **Endpoint:** `/evaluate_rule`
- **Method:** POST
- **Description:** Evaluates the rule against user data and returns a boolean.
## Database Setup

A MySQL database is used to store rules and metadata. 

## Database Structure

- Tables are structured to store the Abstract Syntax Tree (AST) and associated rules for dynamic evaluation.

## Deployment

- The database can be deployed using Docker as detailed in the Setup and Installation section.
# Testing

You can test the API endpoints by sending requests via tools like Postman or cURL. Sample test cases include:

- Testing `create_rule` with different rule strings.
- Testing `combine_rules` to check the efficiency of combining multiple rules.
- Evaluating rules against various user data inputs to ensure correct behavior.
## Bonus Features

- **Error Handling:** The system validates rule strings and ensures they follow correct syntax.
- **User-Defined Functions:** Extendable to allow user-defined functions for advanced rule conditions.
- **Performance:** Optimized rule evaluation by minimizing redundant checks during AST traversal.
## Security and Performance

- **Security:** The application uses parameterized queries to prevent SQL injection and has input validation for rule creation.
- **Performance:** Rule evaluation is designed to be efficient, minimizing redundant evaluations and combining rules using a most-frequent-operator heuristic.
## Contributing

- 1. Fork the repository.
- 2. Create a new branch: 
  ```bash
  git checkout -b feature-branch
```
```
3. Commit your changes:
```bash
git commit -m 'Add new feature'
```
4. Push to the branch:
```bash
git push origin feature-branch
```
5. Open a pull request.






