from operator import attrgetter
from pprint import pformat


class Plan:
    """ Plan object that corresponding to a mapping plan.

    contains each mapping operator as a Candidate.
    """
    def __init__(self, candidates, saving):
        self.candidates = candidates # list of Candidate object
        self.saving = saving # saving about using this plan

    def __repr__(self):
        s = pformat(self.candidates)
        s += f'\nChange: {len(self.candidates)}, Saving: {self.saving}\n'

        return s
    
    def apply(self, circuit, *, silence=False):
        """ apply this plan on target Circuit.

        plan.apply => [candidate.apply(), ...]

        Args:
            circuit: Circuit object
        """
        if not silence:
            print(f'Circuit before: {circuit.draft}')
            print('-' * 15)

        for candidate in self.candidates:
            candidate.apply(circuit, silence=silence)
        
        # change the circuit, should update its operators/draft
        circuit.update()

        if not silence:
            print('-' * 15)
            print(f'Circuit after: {circuit.draft}\n')


class Plans:
    """ container of Plan object
    
    """
    def __init__(self, plans):
        # sorted plans in a descending order of [saving]
        # thus plans[0] is the best plan (may not only)
        self.plans = sorted(plans, key=attrgetter('saving'), reverse=True)

    def __repr__(self):
        LIMIT = 10 # show limit about plans

        s = ''
        for i, plan in enumerate( self.plans[:LIMIT] ):
            s += f'Plan: {i + 1}\n{plan}\n'

        return s + '.' * 10 \
            + f"\n\nTotal Plans: {len(self.plans)}\n"

    def __getitem__(self, i):
        return self.plans[i]

    def __len__(self):
        return len(self.plans)

    def best(self, *, strategy='saving', silence=False):
        """ return the best plan to apply

        Args:
            strategy: strategy use to decide the best plan. default: <saving>
                thus return the Plan with the highest saving.
        -------
        Returns:
            the best Plan
        """
        if strategy == 'saving':
            plan = self.plans[0]

        if not silence:
            print(f'Selected Best Plan: \n{plan}')

        return plan