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
                'payload': 'Ваше путешествие начинается здесь',
                'delay': 2,
            },
            {
                'type': 'text',
                'payload': 'Картинка с памятником Пушкина', # ToDo вставить документ
                'delay': 5,
            },
            {
                'type': 'text',
                'payload': 'Ваше первое задание: найти со мной общий язык',
                'delay': 2,
            },
            {
                'type': 'text',
                'payload': '0JLQsdC70LjQt9C4INCi0LLQtdGA0YHQutC+0LPQviDQuCDQod' \
                           'GC0YDQsNGB0YLQvdC+0LPQviwK0JIg0LzQtdGC0YDQviDQt9C0' \
                           '0LXRgdGMINCf0YPRiNC60LjQvdGB0LrQsNGPINCy0YXQvtC0Lg' \
                           'rQmCDQsiDQutCw0LzQvdC1INC90LDRiCDQv9C+0Y3RgiDRgdGD' \
                           '0YDQvtCy0L4K0J3QsCDQv9C10YDQtdC60YDQtdGB0YLQstC1IN' \
                           'C30LTQtdGB0Ywg0LLQsNGBINC20LTQtdGCLg==',
                'delay': 0,
            },
        ],
        [
            {
                'type': 'text',
                'payload': 'Славное начало квеста!'
                'delay': 2,
            }
        ]
    ),
    Task(
        [
            {
                'type': 'text',
                'payload': 'А может небольшой постик в инсту на память?',
                'delay': 0,
            },
        ],
        [
            {
                'type': 'text',
                'payload': '',
                'delay
            }
        ],
    # Гнездинский
    Task(
        [
            {
                'type': 'text',
                'payload': 'Пора посетить Гнездинский переулок',
                'delay': 50,
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
