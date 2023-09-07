import json
import requests
import ipywidgets as widgets
from IPython.display import display, HTML

class Quiz:
    def __init__(self):
        self.questions = []
        self.current_question_index = 0
        self.user_choices = []
        self.output = widgets.Output()

    def load_from_json(self, json_data):
        # Load questions from a JSON object
        self.questions = json.loads(json_data)

    def load_from_url(self, url):
        # Load questions from a URL
        response = requests.get(url)
        if response.status_code == 200:
            self.questions = response.json()
        else:
            raise Exception(f"Failed to load questions from {url}")

    def create_question_widget(self):
        question = self.questions[self.current_question_index]
        question_text = f"<b>Question {self.current_question_index + 1}:</b> {question['question']}"

        choice_widgets = [widgets.RadioButtons(options=question['choices'], description=f"Choice {i+1}:") for i in range(len(question['choices']))]
        submit_button = widgets.Button(description="Submit")
        submit_button.on_click(self.submit_answer)

        question_html = HTML(value=question_text)
        return widgets.VBox([question_html] + choice_widgets + [submit_button])

    def display_question(self):
        question_widget = self.create_question_widget()
        with self.output:
            display(question_widget)

    def submit_answer(self, button):
        question = self.questions[self.current_question_index]
        user_choice = None
        for i, choice in enumerate(question['choices']):
            if self.user_choices[i].value:
                user_choice = choice
                break
        
        if user_choice is not None:
            if user_choice == question['answer']:
                self.output.clear_output()
                with self.output:
                    display(HTML('<font color="green"><b>Correct!</b></font>'))
            else:
                correct_answer = question['answer']
                self.output.clear_output()
                with self.output:
                    display(HTML(f'<font color="red"><b>Incorrect. The correct answer is: {correct_answer}</b></font>'))
            self.current_question_index += 1
            self.user_choices = []
            if self.current_question_index < len(self.questions):
                self.display_question()
            else:
                self.output.clear_output()
                with self.output:
                    display(HTML('<b>Quiz is over.</b>'))

    def run_quiz(self):
        if len(self.questions) == 0:
            print("No questions to display. Load questions first.")
            return

        self.display_question()
        display(self.output)

if __name__ == "__main__":
    print("This module should not be run directly. Please import it and use it within your application.")
