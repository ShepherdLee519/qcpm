OPENQASM 2.0;
include "qelib1.inc";
qreg q[4];
creg c[4];
ry(-pi/2) q[0];
z q[0];
ry(-pi/2) q[2];
cz q[1],q[2];
ry(pi/2) q[2];
ry(-pi/2) q[1];
z q[1];
ry(pi/2) q[3];
rx(pi/2) q[3];
ry(-pi/2) q[3];
ry(-pi/2) q[3];
cz q[2],q[3];
ry(pi/2) q[3];
ry(pi/2) q[3];
rx(-pi/2) q[3];
ry(-pi/2) q[3];
x q[2];
y q[2];
x q[3];
y q[3];
ry(-pi/2) q[3];
cz q[1],q[3];
ry(pi/2) q[3];
ry(-pi/2) q[2];
cz q[1],q[2];
ry(pi/2) q[2];
ry(-pi/2) q[1];
z q[1];
ry(-pi/2) q[2];
z q[2];
ry(-pi/2) q[1];
cz q[2],q[1];
ry(pi/2) q[1];
ry(-pi/2) q[2];
z q[2];
ry(-pi/2) q[1];
z q[1];
