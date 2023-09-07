import json
import requests
from IPython.display import Markdown, display

class Quiz:
    def __init__(self):
        self.questions = []
        self.current_question_index = 0

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

    def display_question(self):
        if self.current_question_index < len(self.questions):
            question = self.questions[self.current_question_index]
            question_text = f"**Question {self.current_question_index + 1}:** {question['question']}\n"
            choices_text = "\n".join([f"{i + 1}. {choice}" for i, choice in enumerate(question['choices'])])
            display(Markdown(question_text + choices_text))
        else:
            print("Quiz is over.")

    def check_answer(self, user_answer):
        if self.current_question_index < len(self.questions):
            question = self.questions[self.current_question_index]
            correct_answer = question['answer']
            return user_answer == correct_answer
        else:
            return False

    def run_quiz(self):
        while self.current_question_index < len(self.questions):
            self.display_question()
            user_choice = input("Enter the number of your choice:\n")  # Get user's choice
            if user_choice.isdigit():
                user_choice = int(user_choice)
                if 1 <= user_choice <= len(self.questions[self.current_question_index]['choices']):
                    user_answer = self.questions[self.current_question_index]['choices'][user_choice - 1]
                    if self.check_answer(user_answer):
                        display(Markdown('<font color="green"><b>Correct!</b></font>'))
                    else:
                        correct_answer = self.questions[self.current_question_index]['answer']
                        display(Markdown(f'<font color="red"><b>Incorrect. The correct answer is: {correct_answer}</b></font>'))
                    self.current_question_index += 1
                else:
                    print("Invalid choice. Please select a valid choice.")
            else:
                print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    print("This module should not be run directly. Please import it and use it within your application.")
