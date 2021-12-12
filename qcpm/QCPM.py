import os
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

class DepthSizeError(ValueError):
    """ when solving qasm file's depth size(small/medium/large)
        dismatch the expected depth size, this error will occur.
    
    """
    pass


############################
#                          #
#     Class Definition     #
#                          #
############################

class QCPatternMapper:
    """ Quantum circuit pattern mapper Class.

    Example:
        QCPM = QCPatternMapper()

        # 1. single file to file
        QCPM.execute(circuit_path, './circuit_after')

        # 2. dir to dir (batch work)
        QCPM.execute('./data/', './output/', strategy='MCM')
    
    """

    def __init__(self, **kwargs):
        """ 
        Args:
            pattern_path: json file about patterns.
            log: log file to redirect. default '' means to log in stdout.
        """
        self.log = kwargs.get('log', '') # log file path
        self.logs = kwargs.get('logs', './log/') # log files' output dir

        with logging(self.log, 'w'):
            self.mapper = Mapper()

    def execute(self, input_path, output_path='', **kwargs):
        """ apply mapper on target circuit.

        If input path is dir => call self._executeDir

        Args:
            input_path: qasm file's path or may be qasm files' dir path.
            output_path: default='' means no output.
        """
        # if input_path is a folder path => batch work model
        if os.path.isdir(input_path):
            self._executeDir(input_path, output_path, **kwargs)
            return 

        # else execute mapping on target circuit
        # first => get needed parameters from kwargs
        depth_size = kwargs.get('depth_size', 'all') # small/medium/large
        system = kwargs.get('system', 'IBM')
        strategy = kwargs.get('strategy', None)
        metric = kwargs.get('metric', 'cycle')

        if isinstance(system, list):
            # eg. system = ["IBM", "Surface"]
            system_input, system_output = system
        else:
            # eg. system = 'Surface'
            system_input = system_output = system
        
        with logging(self.log):
            # execute turns limit.
            # in each turn: 
            # ---------------
            # 1. optimization: reduction -> commutation ...(×n)... -> reduction
            # 2. pattern mapping: mapper.execute(circuit)
            # 
            LIMIT = 5

            turn = 1
            # first turn should initial circuit(default call optimization.)
            circuit = Circuit(input_path, system=system_input)

            # after loading circuir, check the depth size
            circuit_depth_size = circuit.origin.depth_size
            if depth_size != 'all' and circuit_depth_size != depth_size:
                raise DepthSizeError(circuit_depth_size)
            
            changed = self.mapper.execute(circuit, 
                system=system_input, strategy=strategy, metric=metric)

            while changed and turn < LIMIT:
                circuit.optimize()
                changed = self.mapper.execute(circuit,
                    system=system_input, strategy=strategy, metric=metric)

                turn += 1

            if output_path != '':
                # save qasm file (after mapping)
                circuit.save(output_path, system=system_output)
            
            self.mapper.result()

    def _executeDir(self, input_dir, output_dir, **kwargs):
        """ execute when call batch work form dir to dir.

        Iterately call [self.execute] to execute.

        Args:
            input_dir/output_dir: file folder path. (from => to)
            [! Other args should be corresponding to self.execute] => **kwargs
        
        """
        for i, file in enumerate(os.listdir(input_dir)):
            # eg. 'example.qasm'
            # filename => 'example'
            filename = os.path.splitext(file)[0]
            # output_name => 'example_output'
            output_name = f'{filename}_output'
            
            print(f'solving {i + 1}-th file <{input_dir}{filename}.qasm>...', sep='')

            # default log file will be ./log/example_log.txt
            self.log = f'{self.logs}{filename}_log.txt'
            
            try:
                # call self.execute to solve single file.
                self.execute(
                    os.path.join(input_dir, f'{filename}.qasm'),
                    os.path.join(output_dir, f'{output_name}.qasm'),
                    **kwargs
                )

                print(f'-- finished! output: <{output_dir}{output_name}>.')
                print(f'---- log file in [{self.log}].\n')

            except DepthSizeError as e:
                print(f'-- depth size: [{e}] IGNORE it.\n')
