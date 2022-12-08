#HaiVi v0.0.1

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot(
                'HaiVi',
                storage_adapter='chatterbot.storage.SQLStorageAdapter',
                logic_adapters=[
                    'chatterbot.logic.MathematicalEvaluation',
                    'chatterbot.logic.TimeLogicAdapter',
                    ],
                database_uri='sqlite:///database.sqlite3'
                )

print('Type to begin :)')

while True:
    try:
        user_input = input()
        bot_res=bot.get_response(user_input)
        print(bot_res)

    except(KeyboardInterrupt, EOFError,SystemExit):
        break


trener = ListTrainer(bot)

trener.train([
    'How are you?',
    'I am good',
    'That is good to hear',
    'Thank you',
    'You are welcome'

    
    ])

