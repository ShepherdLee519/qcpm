from abc import abstractmethod
from qcpm.searcher.searcher import Searcher

class KMP(Searcher):
    def __init__(self):
        self.i = 0
        self.j = 0

    # 获取next数组
    def get_next(self, T):
        i = 0
        j = -1
        next_val = [-1] * len(T)

        while i < len(T)-1:
            if j == -1 or T[i] == T[j]:
                i += 1
                j += 1
                # next_val[i] = j
                if i < len(T) and T[i] != T[j]:
                    next_val[i] = j
                else:
                    next_val[i] = next_val[j]
            else:
                j = next_val[j]

        return next_val

    # KMP算法
    def kmp(self, S, T):
        next = self.get_next(T)

        while self.i < len(S) and self.j < len(T):
            if self.j == -1 or S[self.i] == T[self.j]:
                self.i += 1
                self.j += 1
            else:
                self.j = next[self.j]

        if self.j == len(T):
            ans = self.i - self.j
            self.i = self.i - len(T) + 1
            self.j = 0

            return ans
        else:
            return -1
    
    def reset(self):
        self.i = 0
        self.j = 0
    
    def apply(self, haystack, needle):
        self.reset()        

        while True:
            ans = self.kmp(haystack, needle)

            if ans != -1:
                yield ans
            else:
                return