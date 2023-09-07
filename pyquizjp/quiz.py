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
            for i, choice in enumerate(question['choices']):
                print(f"{i + 1}. {choice}")
        else:
            print("The quiz is over.")

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
            user_choice = input("Enter the number of your choice: ")  # Get user's choice
            if user_choice.isdigit():
                user_choice = int(user_choice)
                if 1 <= user_choice <= len(self.questions[self.current_question_index]['choices']):
                    user_answer = self.questions[self.current_question_index]['choices'][user_choice - 1]
                    if self.check_answer(user_answer):
                        print("Correct!")
                    else:
                        print(f"Incorrect. The correct answer is: {self.questions[self.current_question_index]['answer']}")
                    self.current_question_index += 1
                else:
                    print("Invalid choice. Please select a valid choice.")
            else:
                print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    print("This module should not be run directly. Please import it and use it within your application.")
