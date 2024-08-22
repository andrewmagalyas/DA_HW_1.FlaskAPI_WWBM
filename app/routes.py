from flask import jsonify, request, render_template
from flask_restful import Resource
from app import app, api
from app.models import QuestionBank
from app.utils import validate_answer


question_bank = QuestionBank('questions.json')

@app.route('/')
def home():
    return jsonify({"message": "Welcome to Who Wants to Be a Millionaire API!"})

@app.route('/play')
def play():
    return render_template('index.html')

class Questions(Resource):
    def get(self):
        return jsonify(question_bank.get_all_questions())

class Answer(Resource):
    def post(self):
        data = request.get_json()
        question_id = data.get('question_id')
        user_answer = data.get('answer')

        question = question_bank.get_question(question_id)
        if not question:
            return {'error': 'Question not found'}, 404

        result = validate_answer(question, user_answer)
        return result

api.add_resource(Questions, '/questions')
api.add_resource(Answer, '/answer')

