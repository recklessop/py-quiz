import requests
from google.colab import widgets
from IPython.display import display, clear_output, HTML  # Use IPython's HTML widget

class Quiz:
    def __init__(self, url=None, questions=None):
        self.questions = []
        if url:
            self.load_questions_from_url(url)
        elif questions:
            self.questions = questions
        self.user_responses = []
        self.current_question = 0
        self.question_text = HTML()  # Use HTML widget here
        self.choices_radio = widgets.RadioButtons(options=[], layout={'width': 'max-content'})
        self.submit_button = widgets.Button(description='Submit')
        self.submit_button.on_click(self.submit_response)
        self.result_text = HTML()  # Use HTML widget here
        self.display_question()

    def display_question(self):
        question = self.questions[self.current_question]
        self.question_text.value = f'<strong>Question {self.current_question + 1}:</strong> {question["question"]}'
        self.choices_radio.options = question['choices']
        display(self.question_text, self.choices_radio, self.submit_button)

    def submit_response(self, b):
        user_response = self.choices_radio.value
        self.user_responses.append(user_response)
        self.current_question += 1
        if self.current_question < len(self.questions):
            clear_output(wait=True)
            self.display_question()
        else:
            clear_output(wait=True)
            self.display_result()

    def display_result(self):
        correct_answers = sum(response == question['answer'] for response, question in zip(self.user_responses, self.questions))
        total_questions = len(self.questions)
        result_text = f'You got {correct_answers} out of {total_questions} questions correct!'
        self.result_text.value = result_text
        display(self.result_text)

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
