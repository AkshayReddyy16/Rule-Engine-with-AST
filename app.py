# app.py
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from database import init_db, Rule, db
from rule_evaluation import evaluate_condition

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rules.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)  # Enable CORS for all routes

init_db(app)  # Initialize the database

@app.route('/')
def home():
    return render_template('index.html')  # Render the UI

@app.route('/add_rule', methods=['POST'])
def add_rule():
    if not request.is_json:
        return jsonify({"error": "Invalid JSON format"}), 400

    data = request.json
    description = data.get('description')
    condition = data.get('condition')

    if not description or not condition:
        return jsonify({"error": "Missing 'description' or 'condition' in JSON"}), 400

    new_rule = Rule(description=description, condition=condition)
    db.session.add(new_rule)
    db.session.commit()
    
    return jsonify({"message": "Rule added successfully"}), 201

@app.route('/delete_rule/<int:rule_id>', methods=['DELETE'])
def delete_rule(rule_id):
    rule = Rule.query.get(rule_id)
    if not rule:
        return jsonify({"error": "Rule not found"}), 404

    db.session.delete(rule)
    db.session.commit()
    
    return jsonify({"message": "Rule deleted successfully"}), 200

@app.route('/evaluate_rule', methods=['POST'])
def evaluate_rule_api():
    if not request.is_json:
        return jsonify({"error": "Invalid JSON format"}), 400

    data = request.json

    if 'data' not in data:
        return jsonify({"error": "Missing 'data' key in JSON"}), 400
    user_data = data['data']
    
    rules = Rule.query.all()
    results = []

    for rule in rules:
        evaluation_result = evaluate_condition(rule.condition, user_data)
        results.append({
            "rule_id": rule.id,
            "description": rule.description,
            "evaluation_result": evaluation_result
        })

    return jsonify({"results": results}), 200

@app.route('/rules', methods=['GET'])
def get_rules():
    rules = Rule.query.all()
    rules_list = [{"id": rule.id, "description": rule.description, "condition": rule.condition} for rule in rules]
    return jsonify({"rules": rules_list}), 200

if __name__ == '__main__':
    app.run(debug=True)
