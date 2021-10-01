# qcpm

## 输入格式：

+ circuit data: (.qasm)
  
  example.qasm:
  ```
  OPENQASM 2.0;
  include "qelib1.inc";
  qreg q[16];
  creg c[16];
  cx q[4],q[1];
  t q[4];
  t q[2];
  q[0];
  ...
  ```
 
 + pattern data: (.json)
    
    pattern.json:
    ```json
    [
        {
            "src": [
                ["cx", [0, 1]],
                ["cx", [1, 2]],
                ["cx", [0, 1]]
            ],
            "dst": [
                ["cx", [0, 2]],
                ["cx", [1, 2]]
            ]
        },
        ...
    ]
    ```
 ## 运行

`Mapper` 从 json 文件表示的映射关系中构建映射模式，用于内部的映射处理
`Circuit` 从 qasm 中构建电路

`mapper.execute(circuit)`: 在线路 circuit 上应用映射 mapper

```python
from qcpm.pattern.mapper import Mapper
from qcpm.circuit.circuit import Circuit

mapper = Mapper(pattern_path) # ./.json
circuit = Circuit(circuit_path) # ./.qasm

mapper.execute(circuit)
```

## 输出

测试结果的输出见 `log.txt`

包括：

根据输入构建的映射模式：

```
Pattern  1
cx [0, 1]
cx [1, 2]
cx [0, 1]
 => 
cx [0, 2]
cx [1, 2]
...
```

线路根据对应模式查找的可替换的候选项：

```
Pattern:  1

pos:  73 # 匹配处的第一个门操作在序列中的位置
# 以下是匹配到的对应的门操作序列
No: 73, cx [4, 1]
No: 74, cx [1, 2]
No: 75, cx [4, 1]
...
# 所有候选项的匹配位置
Candidate: 
 [73, 75]
```
