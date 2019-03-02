'''
Types of messages:

voice
photo
text
doc

message = {
    'type': ____,
    'payload': ____,
    'delay': ____,
}
'''


class Task:
    
    def __init__(self, start, end, tips=None):
        self.start_messages = start
        self.end_messages = end
        self.tips = tips


tasks = [
    # Памятник Пушкину
    Task(
        [
            {
                'type': 'text',
                'payload': 'В качестве разминки вот вам заколдованный текст',
                'delay': 2,
            },
            {
                'type': 'doc',
                'payload': '', # ToDo вставить документ
                'delay': 0,
            },
        ],
        [
            {
                'type': 'text',
                'payload': 'Не очень удобно с телефона, правда? В любом случае, следущая остановка: Гнездинский переулок',
                'delay': 2,
            }
        ]
    ),
    # Гнездинский
    Task(
        [
            {
                'type': 'text',
                'payload': 'До прибытия на место назначения не вскрывать!',
                'delay': 2,
            },
            {
                'type': 'voice',
                'payload': '', # ToDo вставить описание переулка + задание
                'delay': 0
            },
        ],
        [
            {
                'type': 'text',
                'payload': 'Пока наше компетентное жюри оценивает задание, проследуем далее по переулку',
                'delay': 2,
            }
        ]
    ),
    # Гнездинский МинКульт
    Task(
        [
            {
                'type': 'text',
                'payload': 'Местные легенды гласят, что в этом переулке водится очень редкая и гордая птица. Найдите ее',
                'delay': 2,
            },
        ],
        [
            {

            },
        ]
    ),
]
