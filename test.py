from qcpm import QCPatternMapper2


QCPM = QCPatternMapper2()

# solving single file:
"""
    params:
        - log: eg 'log.txt', path of output log file.
        - optimize: Whether to optimize, default: True
        - system: 
                - if in/out is the same system: "IBM" / "Surface"
                - else: array of in/out systems like: ["IBM", "Surface"]
        - metric: "cycle" / "depth" used to calculate value of candidate.
        - stratrgy: strategy use to generate mapping plan, "MCM"/"random"
            default(None) greedy search.
"""
# QCPM.execute('./data/example_reduction', './circuit_after', 
#     strategy='MCM', system='IBM', metric='depth')


# solving files in batch mode(dir to dir):
# input_dir / output_dir
config = {
    # 'logs': './logs/', # for files
    'stat': './', # csv path
    'strategy': 'random',
    'system': ['IBM', 'Surface'], # ['IBM', 'Surface]
    # 'depth_size': 'medium', # default all
    'metric': 'cycle' # cycle or depth
}
QCPM.execute('./data/stat-test/', './data/stat-output/', **config)