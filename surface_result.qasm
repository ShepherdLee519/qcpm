OPENQASM 2.0;
include "qelib1.inc";
qreg q[12];
ry(-pi/2) q[8];
x q[8];
y q[8];
ry(pi/2) q[3];
rx(pi/4) q[3];
ry(-pi) q[3];
ry(pi/2) q[5];
rx(pi/4) q[5];
ry(-pi/2) q[5];
cz q[8],q[3];
ry(pi) q[3];
ry(-pi/2) q[8];
cz q[5],q[8];
ry(pi) q[8];
rx(-pi/4) q[3];
rx(-pi/4) q[8];
cz q[5],q[8];
ry(-pi/2) q[8];
cz q[5],q[3];
rx(pi/4) q[3];
ry(-pi) q[3];
cz q[8],q[3];
ry(pi) q[3];
rx(-pi/4) q[3];
ry(-pi) q[3];
ry(pi/2) q[8];
rx(pi/4) q[8];
ry(-pi) q[8];
cz q[5],q[3];
ry(pi/2) q[3];
x q[8];
y q[8];
ry(-pi/2) q[8];
x q[8];
y q[8];
ry(pi/2) q[2];
rx(pi/4) q[2];
ry(-pi) q[2];
ry(pi/2) q[6];
rx(pi/4) q[6];
ry(-pi/2) q[6];
cz q[8],q[2];
ry(pi) q[2];
ry(-pi/2) q[8];
cz q[6],q[8];
ry(pi) q[8];
rx(-pi/4) q[2];
rx(-pi/4) q[8];
cz q[6],q[8];
ry(-pi/2) q[8];
cz q[6],q[2];
rx(pi/4) q[2];
ry(-pi) q[2];
cz q[8],q[2];
ry(pi) q[2];
rx(-pi/4) q[2];
ry(-pi) q[2];
ry(pi/2) q[8];
rx(pi/4) q[8];
ry(-pi) q[8];
cz q[6],q[2];
ry(pi/2) q[2];
x q[8];
y q[8];
ry(-pi/2) q[8];
x q[8];
y q[8];
ry(pi/2) q[1];
rx(pi/4) q[1];
ry(-pi) q[1];
ry(pi/2) q[7];
rx(pi/4) q[7];
ry(-pi/2) q[7];
cz q[8],q[1];
ry(pi) q[1];
ry(-pi/2) q[8];
cz q[7],q[8];
ry(pi) q[8];
rx(-pi/4) q[1];
rx(-pi/4) q[8];
cz q[7],q[8];
ry(-pi/2) q[8];
cz q[7],q[1];
rx(pi/4) q[1];
ry(-pi) q[1];
cz q[8],q[1];
ry(pi) q[1];
rx(-pi/4) q[1];
ry(-pi) q[1];
ry(pi/2) q[8];
rx(pi/4) q[8];
ry(-pi) q[8];
cz q[7],q[1];
ry(pi/2) q[1];
x q[8];
y q[8];
ry(-pi/2) q[9];
x q[9];
y q[9];
ry(pi/2) q[3];
rx(pi/4) q[3];
ry(-pi) q[3];
ry(pi/2) q[6];
rx(pi/4) q[6];
ry(-pi/2) q[6];
cz q[9],q[3];
ry(pi) q[3];
ry(-pi/2) q[9];
cz q[6],q[9];
ry(pi) q[9];
rx(-pi/4) q[3];
rx(-pi/4) q[9];
cz q[6],q[9];
ry(-pi/2) q[9];
cz q[6],q[3];
rx(pi/4) q[3];
ry(-pi) q[3];
cz q[9],q[3];
ry(pi) q[3];
rx(-pi/4) q[3];
ry(-pi) q[3];
ry(pi/2) q[9];
rx(pi/4) q[9];
ry(-pi) q[9];
cz q[6],q[3];
ry(pi) q[3];
x q[9];
y q[9];
ry(-pi/2) q[9];
x q[9];
y q[9];
ry(pi/2) q[2];
rx(pi/4) q[2];
ry(-pi) q[2];
ry(pi/2) q[7];
rx(pi/4) q[7];
ry(-pi/2) q[7];
cz q[9],q[2];
ry(pi) q[2];
ry(-pi/2) q[9];
cz q[7],q[9];
ry(pi) q[9];
rx(-pi/4) q[2];
rx(-pi/4) q[9];
cz q[7],q[9];
ry(-pi/2) q[9];
cz q[7],q[2];
rx(pi/4) q[2];
ry(-pi) q[2];
cz q[9],q[2];
ry(pi) q[2];
rx(-pi/4) q[2];
ry(-pi) q[2];
ry(pi/2) q[9];
rx(pi/4) q[9];
ry(-pi) q[9];
cz q[7],q[2];
ry(pi/2) q[2];
x q[9];
y q[9];
ry(-pi/2) q[10];
x q[10];
y q[10];
rx(pi/4) q[3];
ry(-pi) q[3];
ry(pi/2) q[7];
rx(pi/4) q[7];
ry(-pi/2) q[7];
cz q[10],q[3];
ry(pi) q[3];
ry(-pi/2) q[10];
cz q[7],q[10];
ry(pi) q[10];
rx(-pi/4) q[3];
rx(-pi/4) q[10];
cz q[7],q[10];
ry(-pi/2) q[10];
cz q[7],q[3];
rx(pi/4) q[3];
ry(-pi) q[3];
cz q[10],q[3];
ry(pi) q[3];
rx(-pi/4) q[3];
ry(-pi) q[3];
ry(pi/2) q[10];
rx(pi/4) q[10];
ry(-pi) q[10];
cz q[7],q[3];
ry(pi) q[3];
x q[10];
y q[10];
ry(-pi/2) q[11];
cz q[10],q[11];
ry(-pi/2) q[10];
cz q[9],q[10];
ry(pi/2) q[10];
ry(-pi/2) q[9];
cz q[8],q[9];
ry(pi/2) q[9];
x q[11];
y q[11];
rx(pi/4) q[3];
ry(-pi) q[3];
ry(pi/2) q[4];
rx(pi/4) q[4];
ry(-pi/2) q[4];
cz q[11],q[3];
ry(pi) q[3];
ry(-pi/2) q[11];
cz q[4],q[11];
ry(pi) q[11];
rx(-pi/4) q[3];
rx(-pi/4) q[11];
cz q[4],q[11];
ry(-pi/2) q[11];
cz q[4],q[3];
rx(pi/4) q[3];
ry(-pi) q[3];
cz q[11],q[3];
ry(pi) q[3];
rx(-pi/4) q[3];
ry(-pi) q[3];
ry(pi/2) q[11];
rx(pi/4) q[11];
ry(-pi) q[11];
cz q[4],q[3];
ry(pi/2) q[3];
x q[11];
y q[11];
ry(-pi/2) q[11];
x q[11];
y q[11];
ry(pi/2) q[2];
rx(pi/4) q[2];
ry(-pi) q[2];
ry(pi/2) q[5];
rx(pi/4) q[5];
ry(-pi/2) q[5];
cz q[11],q[2];
ry(pi) q[2];
ry(-pi/2) q[11];
cz q[5],q[11];
ry(pi) q[11];
rx(-pi/4) q[2];
rx(-pi/4) q[11];
cz q[5],q[11];
ry(-pi/2) q[11];
cz q[5],q[2];
rx(pi/4) q[2];
ry(-pi) q[2];
cz q[11],q[2];
ry(pi) q[2];
rx(-pi/4) q[2];
ry(-pi) q[2];
ry(pi/2) q[11];
rx(pi/4) q[11];
ry(-pi) q[11];
cz q[5],q[2];
ry(pi/2) q[2];
x q[11];
y q[11];
ry(-pi/2) q[11];
x q[11];
y q[11];
ry(pi/2) q[1];
rx(pi/4) q[1];
ry(-pi) q[1];
ry(pi/2) q[6];
rx(pi/4) q[6];
ry(-pi/2) q[6];
cz q[11],q[1];
ry(pi) q[1];
ry(-pi/2) q[11];
cz q[6],q[11];
ry(pi) q[11];
rx(-pi/4) q[1];
rx(-pi/4) q[11];
cz q[6],q[11];
ry(-pi/2) q[11];
cz q[6],q[1];
rx(pi/4) q[1];
ry(-pi) q[1];
cz q[11],q[1];
ry(pi) q[1];
rx(-pi/4) q[1];
ry(-pi) q[1];
ry(pi/2) q[11];
rx(pi/4) q[11];
ry(-pi) q[11];
cz q[6],q[1];
ry(pi/2) q[1];
x q[11];
y q[11];
ry(-pi/2) q[11];
x q[11];
y q[11];
ry(pi/2) q[0];
rx(pi/4) q[0];
ry(-pi) q[0];
ry(pi/2) q[7];
rx(pi/4) q[7];
ry(-pi/2) q[7];
cz q[11],q[0];
ry(pi) q[0];
ry(-pi/2) q[11];
cz q[7],q[11];
ry(pi) q[11];
rx(-pi/4) q[0];
rx(-pi/4) q[11];
cz q[7],q[11];
ry(-pi/2) q[11];
cz q[7],q[0];
rx(pi/4) q[0];
ry(-pi) q[0];
cz q[11],q[0];
ry(pi) q[0];
rx(-pi/4) q[0];
ry(-pi) q[0];
ry(pi/2) q[11];
rx(pi/4) q[11];
ry(-pi) q[11];
cz q[7],q[0];
ry(pi/2) q[0];
x q[11];
y q[11];
ry(-pi/2) q[10];
x q[10];
y q[10];
ry(pi/2) q[2];
rx(pi/4) q[2];
ry(-pi) q[2];
ry(pi/2) q[4];
rx(pi/4) q[4];
ry(-pi/2) q[4];
cz q[10],q[2];
ry(pi) q[2];
ry(-pi/2) q[10];
cz q[4],q[10];
ry(pi) q[10];
rx(-pi/4) q[2];
rx(-pi/4) q[10];
cz q[4],q[10];
ry(-pi/2) q[10];
cz q[4],q[2];
rx(pi/4) q[2];
ry(-pi) q[2];
cz q[10],q[2];
ry(pi) q[2];
rx(-pi/4) q[2];
ry(-pi) q[2];
ry(pi/2) q[10];
rx(pi/4) q[10];
ry(-pi) q[10];
cz q[4],q[2];
ry(pi/2) q[2];
x q[10];
y q[10];
ry(-pi/2) q[10];
x q[10];
y q[10];
ry(pi/2) q[1];
rx(pi/4) q[1];
ry(-pi) q[1];
ry(pi/2) q[5];
rx(pi/4) q[5];
ry(-pi/2) q[5];
cz q[10],q[1];
ry(pi) q[1];
ry(-pi/2) q[10];
cz q[5],q[10];
ry(pi) q[10];
rx(-pi/4) q[1];
rx(-pi/4) q[10];
cz q[5],q[10];
ry(-pi/2) q[10];
cz q[5],q[1];
rx(pi/4) q[1];
ry(-pi) q[1];
cz q[10],q[1];
ry(pi) q[1];
rx(-pi/4) q[1];
ry(-pi) q[1];
ry(pi/2) q[10];
rx(pi/4) q[10];
ry(-pi) q[10];
cz q[5],q[1];
ry(pi) q[1];
x q[10];
y q[10];
ry(-pi/2) q[10];
x q[10];
y q[10];
ry(pi/2) q[0];
rx(pi/4) q[0];
ry(-pi) q[0];
ry(pi/2) q[6];
rx(pi/4) q[6];
ry(-pi/2) q[6];
cz q[10],q[0];
ry(pi) q[0];
ry(-pi/2) q[10];
cz q[6],q[10];
ry(pi) q[10];
rx(-pi/4) q[0];
rx(-pi/4) q[10];
cz q[6],q[10];
ry(-pi/2) q[10];
cz q[6],q[0];
rx(pi/4) q[0];
ry(-pi) q[0];
cz q[10],q[0];
ry(pi) q[0];
rx(-pi/4) q[0];
ry(-pi) q[0];
ry(pi/2) q[10];
rx(pi/4) q[10];
ry(-pi) q[10];
cz q[6],q[0];
ry(pi) q[0];
x q[10];
y q[10];
ry(-pi/2) q[9];
x q[9];
y q[9];
rx(pi/4) q[1];
ry(-pi) q[1];
ry(pi/2) q[4];
rx(pi/4) q[4];
ry(-pi/2) q[4];
cz q[9],q[1];
ry(pi) q[1];
ry(-pi/2) q[9];
cz q[4],q[9];
ry(pi) q[9];
rx(-pi/4) q[1];
rx(-pi/4) q[9];
cz q[4],q[9];
ry(-pi/2) q[9];
cz q[4],q[1];
rx(pi/4) q[1];
ry(-pi) q[1];
cz q[9],q[1];
ry(pi) q[1];
rx(-pi/4) q[1];
ry(-pi) q[1];
ry(pi/2) q[9];
rx(pi/4) q[9];
ry(-pi) q[9];
cz q[4],q[1];
ry(pi/2) q[1];
x q[9];
y q[9];
ry(-pi/2) q[9];
x q[9];
y q[9];
rx(pi/4) q[0];
ry(-pi) q[0];
ry(pi/2) q[5];
rx(pi/4) q[5];
ry(-pi/2) q[5];
cz q[9],q[0];
ry(pi) q[0];
ry(-pi/2) q[9];
cz q[5],q[9];
ry(pi) q[9];
rx(-pi/4) q[0];
rx(-pi/4) q[9];
cz q[5],q[9];
ry(-pi/2) q[9];
cz q[5],q[0];
rx(pi/4) q[0];
ry(-pi) q[0];
cz q[9],q[0];
ry(pi) q[0];
rx(-pi/4) q[0];
ry(-pi) q[0];
ry(pi/2) q[9];
rx(pi/4) q[9];
ry(-pi) q[9];
cz q[5],q[0];
ry(pi) q[0];
x q[9];
y q[9];
ry(-pi/2) q[8];
x q[8];
y q[8];
rx(pi/4) q[0];
ry(-pi) q[0];
ry(pi/2) q[4];
rx(pi/4) q[4];
ry(-pi/2) q[4];
cz q[8],q[0];
ry(pi) q[0];
ry(-pi/2) q[8];
cz q[4],q[8];
ry(pi) q[8];
rx(-pi/4) q[0];
rx(-pi/4) q[8];
cz q[4],q[8];
ry(-pi/2) q[8];
cz q[4],q[0];
rx(pi/4) q[0];
ry(-pi) q[0];
cz q[8],q[0];
ry(pi) q[0];
rx(-pi/4) q[0];
ry(-pi) q[0];
ry(pi/2) q[8];
rx(pi/4) q[8];
ry(-pi) q[8];
cz q[4],q[0];
ry(pi/2) q[0];
x q[8];
y q[8];
