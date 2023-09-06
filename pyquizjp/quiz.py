import ipywidgets as widgets
from IPython.display import display, HTML
import requests

class Quiz:
    def __init__(self, url=None, questions=None):
        self.questions = []
        if url:
            self.load_questions_from_url(url)
        elif questions:
            self.questions = questions
        self.user_responses = []
        self.current_question = 0
        self.question_text = HTML()
        self.choices_radio = widgets.RadioButtons(options=[], layout={'width': 'max-content'})
        self.submit_button = widgets.Button(description='Submit')
        self.submit_button.on_click(self.submit_response)

#    def display_question(self):
#        question = self.questions[self.current_question]
#        self.question_text.value = f'<strong>Question {self.current_question + 1}:</strong> {question["question"]}'
#        self.choices_radio.options = question['choices']
#        display(self.question_text, self.choices_radio, self.submit_button)

#    def submit_response(self, b):
#        user_response = self.choices_radio.value
#        self.user_responses.append(user_response)
#        self.current_question += 1
#        if self.current_question < len(self.questions):
#            self.display_question()
#        else:
#            result = self.calculate_result()
#            return result

#    def calculate_result(self):
#        correct_answers = sum(response == question['answer'] for response, question in zip(self.user_responses, self.questions))
#        total_questions = len(self.questions)

#        result = {
#            'correct_answers': correct_answers,
#            'total_questions': total_questions,
#            'incorrect_questions': []
#        }

 #       for i, (user_response, question) in enumerate(zip(self.user_responses, self.questions)):
 #           if user_response != question['answer']:
 #               result['incorrect_questions'].append({
 #                   'question_text': question['question'],
 #                   'correct_answer': question['answer'],
 #                   'user_response': user_response
 #               })

 #       return result

    def load_questions_from_url(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            if isinstance(data, list):
                self.questions = data
            else:
                print("Invalid data format from the URL. Expecting a list of questions.")
        except Exception as e:
            print(f"Error loading questions from URL: {e}")
