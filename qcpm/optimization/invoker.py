import pkgutil
import json

from qcpm.optimization.pattern import ReductionPattern, CommutationPattern


class Invoker:
    def __init__(self, name):
        self.data = pkgutil.get_data(__package__, f'/rules/{name}.json')
        self.rules = json.loads(self.data.decode())

        self.patterns = [] # should set by subclass

        self.min_size = len(min(self.rules, key=lambda rule:len(rule['src']))['src'])
        self.max_size = len(max(self.rules, key=lambda rule:len(rule['src']))['src'])

    def __call__(self, ops):
        if len(ops) < self.min_size:
            return

        for pattern in self.patterns:
            pattern.map(ops)


class Reducer(Invoker):
    def __init__(self, name):
        super().__init__(name)

        self.patterns = [ ReductionPattern(**rule) for rule in self.rules ]


class Commutator(Invoker):
    def __init__(self):
        super().__init__('commutation')

        self.patterns = [ CommutationPattern(**rule) for rule in self.rules ]