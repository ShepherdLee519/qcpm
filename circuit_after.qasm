OPENQASM 2.0;
include "qelib1.inc";
qreg q[4];
creg c[4];
id q[1];
ry(pi/2) q[2];
rx(-pi/2) q[2];
ry(-pi/2) q[2];
