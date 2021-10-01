from abc import ABCMeta, abstractmethod

class Searcher(metaclass=ABCMeta):
    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def apply(self, haystack, needle):
        pass

    @abstractmethod
    def __repr__(self):
        pass