from time import *

class Timer:
    def start(self, description=""):
        self.description = description

        print('Start Timer: ', description)
        self.start_time = time()

    def end(self):
        print('End Timer [{}]:  {}'.format(self.description, time() - self.start_time))