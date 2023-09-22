import json

with open("questions.json", 'r') as file:
    content = file.read()

data = json.loads(content)

# game interation with the user

for question in data:
    print(question["question"])
    for index, alternative in enumerate(question["alternatives"]):
        print(index + 1, '-', alternative)

    user_answer = int(input("What do you think? "))
    question["user_choice"] = user_answer

score = 0
# storing user choices
for index, question in enumerate(data):
    if question["user_choice"] == question["correct answer"]:
        score = score + 1
        result = " Correct answer! "
    else:
        result = " Wrong answer! "

    message = f'{index+1}{result} Your answer: {question["user_choice"]}, ' \
    f'Correct answer: {question["correct answer"]}'
    print(message)

print(score, "/", len(data))
