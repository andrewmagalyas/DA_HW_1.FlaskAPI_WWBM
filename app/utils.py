def validate_answer(question, user_answer):
    is_correct = user_answer == question['correct_answer']
    return {
        'correct': is_correct,
        'correct_answer': question['correct_answer']
    }