import random

messages = [
    'It is decidely so.',
    'Yes definitely.',
    'Reply hazy try again.',
    'Ask again later.',
    'Concentrate and ask again.',
    'My reply is no.',
    'Outlook not so good.',
    'Very doubtful.'
    ]

while True:
    print('Please type a question and I will give you an answer (or nothing to quit)')
    question = input()
    if question.strip() == '':
        break
    print(random.choice(messages))

print('Thank you for playing')
