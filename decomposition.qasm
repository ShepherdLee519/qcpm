OPENQASM 2.0;
include "qelib1.inc";
qreg q[4];
creg c[4];

z q[0];
=> 
x q[0];
y q[0];


h q[0];
=> 
ry(-pi/2) q[0];
z q[0];
/
z q[0];
ry(pi/2) q[0];
/
x q[0];
ry(-pi/2) q[0];


t q[0];
=>
ry(pi/2) q[0];
rx(pi/4) q[0];
ry(-pi/2) q[0];


tdg q[0];
=>
ry(pi/2) q[0];
rx(-pi/4) q[0];
ry(-pi/2) q[0];


s q[0];
=> 
ry(pi/2) q[0];
rx(pi/2) q[0];
ry(-pi/2) q[0];


sdg q[0];
=>
ry(pi/2) q[0];
rx(-pi/2) q[0];
ry(-pi/2) q[0];


cx q[0],q[1];
=>
ry(-pi/2) q[1];
cz q[0],q[1];
ry(pi/2) q[1];
/
ry(-pi/2) q[1];
cz q[1],q[0];
ry(pi/2) q[1];