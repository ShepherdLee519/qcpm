import sys
import os
from contextlib import contextmanager

from qcpm.pattern import Mapper
from qcpm.circuit import Circuit


stdout = sys.stdout

@contextmanager
def logging(log_path, mode='a'):
    """ logging context management

    enter: redirect stdout to log_file(according to log_path)
        if log_paht is '' no redirect
    leave: recover the sys.stdout to origin stdout
    """
    if log_path != '':
        # redirect to log file
        log_file = open(log_path, mode)
        sys.stdout = log_file
    
    try:
        yield
    finally:
        if log_path != '':
            log_file.close()
        
        sys.stdout = stdout


############################
#                          #
#     Class Definition     #
#                          #
############################

class QCPatternMapper:
    def __init__(self, *, pattern_path=None, log=''):
        """ 
        Args:
            pattern_path: json file about patterns.
            log: log file to redirect. default '' means to log in stdout.
        """
        self.turns_limit = 5
        
        self.log = log
        with logging(log, 'w'):
            self.mapper = Mapper(pattern_path)

    def execute(self, circuit_path, circuit_save_path='', *, strategy=None, silence=False):
        if os.path.isdir(circuit_path):
            self._executeDir(circuit_path, circuit_save_path, 
                strategy=strategy, silence=silence)
            return 
        
        with logging(self.log):
            count = 1
            circuit = Circuit(circuit_path)
            changed = self.mapper.execute(circuit, strategy=strategy, silence=silence)

            while changed and count < self.turns_limit:
                circuit.optimize()
                changed = self.mapper.execute(circuit, strategy=strategy, silence=silence)
                count += 1

            if circuit_save_path != '':
                circuit.save(circuit_save_path)

            if silence:
                self.mapper.result(circuit)

    def _executeDir(self, input_dir, output_dir, *, strategy=None, silence=False):
        for file in os.listdir(input_dir):
            filename = os.path.splitext(file)[0]
            output_name = f'{filename}_output'
            self.log = f'./log/{filename}_log.txt'
            
            self.execute(
                os.path.join(input_dir, filename),
                os.path.join(output_dir, output_name),
                strategy=strategy, silence=silence
            )
