OPENQASM 2.0;
include "qelib1.inc";
qreg q[5];
creg c[5];
h q[2];
cx q[0],q[2];
h q[2];
