OPENQASM 2.0;
include "qelib1.inc";
qreg q[20];
cx q[15],q[4];
cx q[11],q[15];
cx q[18],q[10];
cx q[11],q[4];
cx q[13],q[12];
cx q[13],q[11];
cx q[16],q[2];
cx q[6],q[15];
