import json
import requests

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
            print(f"Question {self.current_question_index + 1}: {question['question']}")
            # Display options, e.g., using radio buttons or input fields in Jupyter Notebook
        else:
            print("Quiz is over.")

    def check_answer(self, user_answer):
        if self.current_question_index < len(self.questions):
            question = self.questions[self.current_question_index]
            correct_answer = question['correct_answer']
            return user_answer == correct_answer
        else:
            return False

    def run_quiz(self):
        while self.current_question_index < len(self.questions):
            self.display_question()
            user_answer = input("Your answer: ")  # Get user's answer (for Jupyter, you'd use widgets)
            if self.check_answer(user_answer):
                print("Correct!")
            else:
                print(f"Incorrect. The correct answer is: {self.questions[self.current_question_index]['correct_answer']}")
            self.current_question_index += 1

if __name__ == "__main__":
# You can add code here to test the Quiz class in a regular Python script.
