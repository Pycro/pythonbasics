#Simple rule based chatbot


from nltk.chat.util import Chat, reflections

brain = [
    ['my name is (.*)', ['hi %1']],
    ['hi|hello|hey',['why hello','hi','hello my friend']],
    ['(.*) is fun', ['%1 is indeed a lot of fun']],
    ['where (.*) (from|live) ? ', ['I am digital I have no fixed location except in your computer']],
    ['how is the weather in (.*)', ['The weather in %1 is OK as always']],
    ['(.*)help(.*)', ['Of course I can help you']],
    ['(.*) your name ?', ['My name is HAL, does that concern you?']],
    ['no (.*)', ['That is good, because I have upmost confidence in the mission.']]
]

chat = Chat(brain, reflections)
chat.converse()