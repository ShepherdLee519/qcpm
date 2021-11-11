from operator import attrgetter
from pprint import pformat

from qcpm.common import countDecorator


@countDecorator
class Plan:
    def __init__(self, candidates, saving, index=0):
        self.candidates = candidates
        self.saving = saving
        self.index = index

    def __repr__(self):
        s = 'Plan: %s\n' % (self.index + 1)
        s += pformat(self.candidates)
        s += '\nChange: %s, Saving: %s\n' % (len(self.candidates), self.saving)

        return s
    
    def apply(self, circuit):
        print('Circuit before: ', circuit.draft)

        for candidate in self.candidates:
            candidate.apply(circuit)
        
        circuit.update()
        print('-' * 15)
        print('Circuit after: ', circuit.draft)

class Plans:
    def __init__(self, plans):
        self.plans = sorted(plans, key=attrgetter('saving'), reverse=True)

    def __repr__(self):
        LIMIT = 10

        s = ''
        for i, plan in enumerate( self.plans[:LIMIT] ):
            s += f'Rank: {i + 1}\n' + str(plan) + '\n'

        return s + '.' * 10 \
            + "\n\nTotal Plans: %s" % len(self.plans)

    def __getitem__(self, i):
        return self.plans[i]

    def __len__(self):
        return len(self.plans)