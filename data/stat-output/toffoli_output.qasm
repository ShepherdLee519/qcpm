OPENQASM 2.0;
include "qelib1.inc";
qreg q[3];
creg c[3];
ry(-pi/2) q[0];
z q[0];
ry(-pi/2) q[1];
z q[1];
cz q[1],q[2];
ry(-pi/2) q[2];
z q[2];
ry(pi/2) q[2];
rx(-pi/4) q[2];
ry(-pi/2) q[2];
ry(-pi/2) q[2];
z q[2];
cz q[1],q[2];
ry(-pi/2) q[2];
z q[2];
ry(-pi/2) q[1];
z q[1];
cz q[1],q[2];
ry(-pi/2) q[1];
z q[1];
ry(-pi/2) q[2];
z q[2];
cz q[1],q[2];
ry(-pi/2) q[2];
z q[2];
ry(-pi/2) q[1];
z q[1];
cz q[0],q[1];
ry(-pi/2) q[1];
z q[1];
ry(pi/2) q[1];
rx(pi/4) q[1];
ry(-pi/2) q[1];
ry(-pi/2) q[1];
z q[1];
cz q[1],q[2];
ry(-pi/2) q[1];
z q[1];
ry(pi/2) q[1];
rx(-pi/4) q[1];
ry(-pi/2) q[1];
ry(-pi/2) q[1];
z q[1];
cz q[0],q[1];
ry(-pi/2) q[1];
z q[1];
ry(pi/2) q[1];
rx(pi/4) q[1];
ry(-pi/2) q[1];
ry(pi/2) q[2];
rx(pi/4) q[2];
ry(-pi/2) q[2];
ry(-pi/2) q[1];
z q[1];
ry(-pi/2) q[2];
z q[2];
cz q[1],q[2];
ry(-pi/2) q[2];
z q[2];
ry(-pi/2) q[1];
z q[1];
cz q[2],q[1];
ry(-pi/2) q[1];
z q[1];
ry(-pi/2) q[2];
z q[2];
cz q[1],q[2];
ry(-pi/2) q[2];
z q[2];
ry(-pi/2) q[1];
z q[1];
cz q[0],q[1];
ry(-pi/2) q[1];
z q[1];
ry(pi/2) q[1];
rx(-pi/4) q[1];
ry(-pi/2) q[1];
ry(-pi/2) q[1];
z q[1];
cz q[0],q[1];
ry(-pi/2) q[1];
z q[1];
ry(pi/2) q[0];
rx(pi/4) q[0];
ry(-pi/2) q[0];
