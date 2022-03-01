OPENQASM 2.0;
include "qelib1.inc";
qreg q[6];
creg c[6];
cx q[5],q[2];
x q[4];
cx q[5],q[0];
cx q[5],q[2];