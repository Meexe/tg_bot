from tasks import tasks
from test_tasks import test_tasks
from simple_settings import settings


class Quest:

    def __init__(self):
        self.task = None
        if settings.test:
            self.gen = (task for task in test_tasks)
        else:
            self.gen = (task for task in tasks)

    def start_task(self):
        # try:
        #     self.task = next(self.gen)
        # except StopIteration:
        #     return quest_over_message  
        self.task = next(self.gen)
        return self.task.start_messages

    def end_task(self):
        return self.task.end_messages
