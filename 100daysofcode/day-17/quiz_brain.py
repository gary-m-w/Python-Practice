class QuizBrain:
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_q = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_q.text} (True/False): ")
        self.check_answer(user_answer, current_q.answer)

    def check_answer(self, answer, correct_answer):
        answer = answer
        correct = correct_answer
        if answer.lower() == correct.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("No, that's wrong.")
        print(f"The correct answer was: {correct}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print('\n')
