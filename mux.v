module mux(in1,in2,sel,out);
input in1,in2,sel;
output out;

assign out = sel ? in1 : in2;

endmodule
