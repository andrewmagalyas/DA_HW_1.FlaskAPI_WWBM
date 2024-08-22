import json

class QuestionBank:
    def __init__(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            self.questions = json.load(file)

    def get_question(self, question_id):
        return next((q for q in self.questions if q['id'] == question_id), None)

    def get_all_questions(self):
        return self.questions