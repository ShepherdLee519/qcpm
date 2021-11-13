import numpy as np


def sample(targets, probabilities):
    """ sample a element with [probabilities] in [target]

    Args:
        targets: eg. ['a', 'b', 'c', 'd']
        probabilities: eg. [0.1, 0.2, 0.3, 0.4]
            probabilities should guarantee that sum = 1
    -------
    Returns:
        Sample a element in targets according to probabilities. 
    """
    prob = probabilities[0]
    probs = [ prob ]

    for i in range(1, len(probabilities)):
        prob += probabilities[i]
        probs.append(prob)

    p = np.random.rand()

    for i, prob in enumerate(probs):
        if p <= prob:
            return targets[i] 


class Simulation:
    """ Monte Carlo simulation

    """
    def __init__(self, searcher):
        self.searcher = searcher

    def gatherCandidates(self, candidate):
        """ return the cnadidates after candidate in SIMULATION_SIZE

        """
        targets = []
        circuit = self.searcher.circuit
        candidates = self.searcher.candidates

        index = candidates.index(candidate)
        # range of simulation
        limit = candidate.begin + self.searcher.SIMULATION_SIZE
        if limit > len(circuit):
            limit = len(circuit)
        
        for i in range(index + 1, len(candidates)):
            # filter candidate in simulation range
            if candidates[i].end < limit:
                targets.append(candidates[i])
        
        return targets


    def __call__(self, candidate):
        """ simulate one candidate to get value

        simulate candidate in SIMULATION_SIZE and SIMULATION_TIMES.

        Args:
            candidate: one Candidate object
        -------
        Returns:
            value: simulation result of this candidate.
        """
        values = []

        # self.searcher.logdata += f'     Simulate: {candidate}\n'
        for turn in range(self.searcher.SIMULATION_TIMES):
            # self.searcher.logdata += f'     Turn: {turn + 1}\n'

            targets = self.gatherCandidates(candidate)
            candidates = [ candidate ]
            temp = list(filter(lambda c: not (c & candidates), targets))

            value = candidate.delta
            
            while len(temp) != 0:
                # self.searcher.logdata += f'         targets:\n'
                # self.searcher.logdata += f'         ' + '-' * 20 + '\n'
                # for t in temp:
                #     self.searcher.logdata += f'         {str(t)}\n'
                # self.searcher.logdata += f'         ' + '-' * 20 + '\n'

                # calculate probabilities acoording to saving of each candidate
                probs = [ t.delta for t in temp ]
                probs = np.array(probs) / sum(probs)
                # self.searcher.logdata += f'         probabillities:'
                # probs_str = [f'{prob:.2f}' for prob in probs]
                # self.searcher.logdata += f'[{",".join(probs_str)}]\n'

                # sample a candidate
                selected = sample(targets, probs)
                # self.searcher.logdata += f'         Sample: {selected}\n\n'
                targets.remove(selected)
                candidates.append(selected)
                value += selected.delta

                # update candidates that guarantee that selected one 
                # will not be conflict with candidates in [candidates].  
                temp = list(filter(lambda c: not (c & candidates), temp))
            
            # self.searcher.logdata += f'         Value: {value}\n\n'
            values.append(value)

        mean = np.mean(values)
        # self.searcher.logdata += f'     {"#" * 45}\n     # \n'
        # self.searcher.logdata += f'     #  {candidate} => Mean value: {mean}\n     #\n'
        # self.searcher.logdata += f'     {"#" * 45}\n\n'

        return mean
