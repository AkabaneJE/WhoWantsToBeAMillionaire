from QuestionMaster import QuestionMaster
from question_list import questions
from Question import Question

question_bank =[Question(question["question"], question["answer"])
                for question in questions]

question_master = QuestionMaster(q_list=question_bank)
question_master.start_quiz()



