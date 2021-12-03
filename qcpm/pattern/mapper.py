import sys
import json
import pkgutil

from qcpm.candidate import Candidate, filterCandidates, SearchPlan
from qcpm.pattern.pattern import Pattern
from qcpm.pattern.positioning import positioning

from qcpm.common import timerDecorator, Timer


##########################
#                        #
#     Tool Functions     #
#                        #
##########################

def title(content, *, char='*', space=3):
    size = len(content)
    
    return char * (size + space * 2 + 2) + '\n'\
        + char + ' ' * (size + space * 2) + f'{char}\n' \
        + char + ' ' * space + content + ' ' * space + f'{char}\n' \
        + char + ' ' * (size + space * 2) + f'{char}\n' \
        + char * (size + space * 2 + 2)

############################
#                          #
#     Class Definition     #
#                          #
############################

class Mapper:
    """ Mapper that created by patterns json file.

    Example:
        init mapper object: mapper = Mapper(pattern_path)
        apply mapping: mapper.execute(circuit)
            which [circuit] is a Circuit object.
    """
    @timerDecorator(description='Init Mapper')
    def __init__(self):
        self.patterns = {} # contains Pattern object.
        self._init_patterns()

        # dynamically set when [execute()] call.
        self.circuit = None # should be Circuit object
        self._candidates = [] # contains temp Candidates (Candidate object)
        self.plans = [] # candidates mapping plan (Plan object)
        
    def _init_patterns(self):
        """ load pattern file and initiate

        load pattern json file and init self.patterns
        will load all system's pattern info in advance.

        """
        systems = ['IBM', 'Surface']
        self.patterns = {} # reset to empty

        for system in systems:
            data = pkgutil.get_data(__package__, f'/rules/{system}/pattern.json')
            patterns_data = json.loads(data.decode())

            self.patterns[system] = []

            # pattern: 
            # {
            #     "src": [ ["x", [1]], ["cx", [0, 1]], ["x", [1]] ],
            #     "dst": [ ["cx", [0, 1]] ]
            # }
            for pattern in patterns_data:
                # Pattern(src, dst)
                self.patterns[system].append( Pattern(**pattern) )

    def _validate(self, pattern):
        """ Return a a validater function

        validater function uses to validate the candidates(positions)

        Args:
            pattern: pattern which need to validate on circuit.
        ------- 
        Returns:
            A validater function use to check the candidates whether match
                the [pattern] also check conflict-free.
        """

        def validater(position):
            # 1. Validate Operands
            ok, targets = pattern.match(self.circuit, position)
            if not ok:
                return False

            # 2. Validate no conflicts
            targets = set(targets) # [4, 1, 1, 2] => {4, 1, 2}

            # eg. position: [4, 7, 10]
            # => check range(4, 10) (without 7) that has no conflict with targets
            for pos in range(position[0] + 1, position[-1]):
                if pos not in position:
                    operand = self.circuit[pos].operands

                    # eg. [1, 4] => [4] => {4}
                    ops = set(operand)
                    
                    # eg. have no intersection => no conflict
                    if len(targets & ops) != 0:
                        return False

            return True
        
        return validater

    def find(self, pattern):
        """ according to pattern that finds Candidiates' positions

        call [positioning] to find the candidates' positions 

        """
        # Step 1: get possible candidates' positions like [1, 4, 7] => "xcx"
        #
        # eg. operator: xcx
        positions = positioning(self.circuit.draft, pattern.src['operator'])

        # Step 2: validate possible candidates
        validater = self._validate(pattern)
        validated_positions = filter(validater, positions)

        print("\nCandidates: \n")
        for position in validated_positions:
            
            # keep candidates(=> Candidate object) in local _candidates[]
            self._candidates.append( Candidate(position, pattern) )

            print(position)

    def result(self, circuit):
        """ show final result of mapping

        Args:
            circuit: Circuit object which is the mapping target.
        """
        size_origin, size_after = circuit.origin.size, len(circuit.draft)

        print('-' * 15)
        print('>> Origin circuit: ')
        print(circuit.origin)
        print('\n>> Solved circuit: ')
        print(circuit.info)

        print(f'Reduced: \n - size: {size_origin - size_after}', 
            f'({(size_origin - size_after) / size_origin * 100:.2f}%)')
        print(f' - depth: {circuit.origin.depth - circuit.info.depth}\n')

    @timerDecorator(description='Execute Mapping')
    def execute(self, circuit, **kwargs):
        """ execute mapping on circuit object

        Args:
            circuit: A Circuit object. 
                Recall that circuit containes [operators], and [draft].
            -------
            kwargs:
            strategy: strategy to generate mapping plan.
                None => exact mapping
                'MCM' => Monte Carlo-based plan searching
            silence: whether print log info. 
                True => do not print (default False: print)
        -------
        Returns:
            changed[bool]: whether change the target circuit 
                in this pattern mapping executation.
        """
        # get parameters from kwargs.
        strategy = kwargs.get('strategy', None)
        silence = kwargs.get('silence', False)
        system = kwargs.get('system', 'IBM')

        # if silence => close all output:
        stdout = sys.stdout
        if silence:
            sys.stdout = None

        # 0. reset
        self.circuit = circuit
        size_before = len(circuit) # record it to judge whether changed
        self._candidates = []
        self.plans = []

        # 1. collect possible candidates
        print('\n' + title('Pattern & Candidates'))
        with Timer('Find Candidates'):
            for i, pattern in enumerate(self.patterns[system]):
                print('\n' + '-' * 12 + f" {i + 1} " + '-' * 12)
                print(pattern)

                self.find(pattern)

        # 2. filter candidates => (without conflict)
        with Timer('Generate Plans'):
            self._candidates.sort(key=lambda x: (x.begin, x.size, x.end))

            print('\n' + title('Generate Plans') + '\n')
            print('Sorted Candidates: \n')
            print(self._candidates)
            print()

            # should return a Plans object
            if strategy == 'MCM':
                self.plans = SearchPlan(circuit, self._candidates)()
            else:
                self.plans = filterCandidates(self._candidates)
        
        # 3. apply the best plan
        if len(self.plans) != 0:
            with Timer('apply mapping plan'):
                print('\n' + title('Apply Mapping Plan') + '\n')

                self.plans.best.apply(circuit)
        else:
            print("There's no mapping plan.")

        # 4. show the result.
        changed = size_before != len(circuit.draft)
        self.result(circuit)

        # recover sys.stdout if silence
        if silence:
            sys.stdout = stdout

        return changed