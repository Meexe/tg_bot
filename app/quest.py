from tasks import tasks
from test_tasks import test_tasks
from simple_settings import settings


class Quest:

    def __init__(self):
        self.task = None
        self.chat_id = 0
        if settings.test:
            self.gen = (task for task in test_tasks)
        else:
            self.gen = (task for task in tasks)

    def start_task(self):
        try:
            self.task = next(self.gen)
        except StopIteration:
            return list()  
        return self.task.start_messages

    def end_task(self):
        return self.task.end_messages
