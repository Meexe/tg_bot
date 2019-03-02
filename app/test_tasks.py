from tasks import Task


test_tasks = [
    Task( # Test deafult behavior
        [
            {
                'type': 'text',
                'payload': 'TestTask1 - start',
                'delay': 2,
            },
        ],
        [
            {
                'type': 'text',
                'payload': 'TeskTask1 - end',
                'delay': 2,
            }
        ]
    ),
    Task( # Test multi message behavior
        [
            {
                'type': 'text',
                'payload': 'TestTask2 - start1',
                'delay': 2,
            },
            {
                'type': 'text',
                'payload': 'TestTask2 - start2',
                'delay': 2,
            },
            {
                'type': 'text',
                'payload': 'TestTask2 - start3',
                'delay': 2,
            },
        ],
        [
            {
                'type': 'text',
                'payload': 'TeskTask2 - end1',
                'delay': 2,
            },
            {
                'type': 'text',
                'payload': 'TeskTask2 - end2',
                'delay': 2,
            },
            {
                'type': 'text',
                'payload': 'TeskTask2 - end3',
                'delay': 2,
            },
        ]
    ),
    # Test other message types
]
