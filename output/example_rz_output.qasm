OPENQASM 2.0;
include "qelib1.inc";
qreg q[3];
creg c[3];
cx q[0],q[1];
h q[1];
rz(0.3) q[1];
