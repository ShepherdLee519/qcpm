OPENQASM 2.0;
include "qelib1.inc";
qreg q[30];
x q[1];
x q[7];
x q[15];
x q[21];
ccx q[0],q[3],q[4];
ccx q[1],q[2],q[5];
ccx q[6],q[9],q[10];
ccx q[7],q[8],q[11];
ccx q[14],q[17],q[18];
ccx q[15],q[16],q[19];
ccx q[20],q[23],q[24];
ccx q[21],q[22],q[25];
x q[0];
x q[1];
x q[6];
x q[7];
x q[14];
x q[15];
x q[20];
x q[21];
ccx q[0],q[2],q[4];
ccx q[1],q[3],q[5];
ccx q[6],q[8],q[10];
ccx q[7],q[9],q[11];
ccx q[14],q[16],q[18];
ccx q[15],q[17],q[19];
ccx q[20],q[22],q[24];
ccx q[21],q[23],q[25];
x q[0];
x q[4];
x q[6];
x q[14];
x q[18];
x q[20];
ccx q[4],q[10],q[12];
ccx q[5],q[11],q[13];
ccx q[18],q[24],q[26];
ccx q[19],q[25],q[27];
x q[4];
x q[5];
x q[18];
x q[19];
ccx q[5],q[10],q[13];
ccx q[4],q[11],q[12];
ccx q[19],q[24],q[27];
ccx q[18],q[25],q[26];
x q[5];
x q[12];
x q[19];
ccx q[12],q[26],q[28];
ccx q[13],q[27],q[29];
x q[12];
x q[13];
ccx q[13],q[26],q[29];
ccx q[12],q[27],q[28];
x q[13];