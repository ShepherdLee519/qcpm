import sys
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


class QCPatternMapper:
    def __init__(self, pattern_path, *, log=''):
        """ 
        Args:
            pattern_path: json file about patterns.
            log: log file to redirect. default '' means to log in stdout.
        """
        self.log = log
        with logging(log, 'w'):
            self.mapper = Mapper(pattern_path)

    def execute(self, circuit_path, circuit_save_path=''):
        with logging(self.log):
            circuit = Circuit(circuit_path)
            self.mapper.execute(circuit)

            if circuit_save_path != '':
                circuit.save(circuit_save_path)