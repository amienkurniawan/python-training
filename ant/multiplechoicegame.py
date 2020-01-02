from Question import Question

question_prompts = [
    "what color of apple? \n(a) Red \n(b) Blue \n(c) Orange",
    "what color of Banana? \n(a) Red \n(b) Yellow \n(c) Orange",
    "what color of Orange? \n(a) Red \n(b) Blue \n(c) Orange",
]

Questions = [
    Question(question_prompts[0],"a"),
    Question(question_prompts[1],"b"),
    Question(question_prompts[2],"c")
]

def run_test(Questions):
    score = 0
    for question in Questions:
        answer = input(question.prompts)
        if answer == question.answer:
            score += 1
    print("you got"+ str(score) +"/"+str(len(Questions)) + "Correct")

run_test(Questions)