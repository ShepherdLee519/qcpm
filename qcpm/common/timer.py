from time import *

class Timer:

    indent = 0

    """
        call:
        1.  with Timer(description):
                todo...
        2.  timer = Timer()
            timer.start(description)
            todo...
            timer.end()
    """
    def __init__(self, description=""):
        self.description = description
    
    def start(self, description=""):
        if description != "":
            self.description = description

        print('-' * (self.__class__.indent * 4) + \
            'Start Timer: [{}]'.format(self.description))
        self.start_time = time()

        self.__class__.indent += 1

    def end(self):
        self.__class__.indent -= 1
        print('-' * (self.__class__.indent * 4) + \
            'End Timer [{}]:  {}\n'.format(self.description, time() - self.start_time))

    # context management protocol
    # __enter__ and __exit__ 
    def __enter__(self):
        self.start()
    
    def __exit__(self, exec_type, exec_value, traceback):
        self.end()