import re
import os
__name__ = '__main__'
file = "mux.v"
def read_design(file):
    design = open(file,"r")
    if(os.path.exists(file)):
        print("Design Found !")
    lines = design.readlines()
    return lines
#Script Steps
# 1. Get top module
def get_top_module(lines):
#mod_list = list()
    for line in lines:
        if (re.findall(r"^\s*module",line)):
            line = re.sub('^\s+','',line,1)
            mod = re.split(r'\s+|\(',line)[1]
            #mod_list.append(mod)
            return mod
    #print(mod_list)
# 2. Get IO ports
# 3. Detect Clock and Reset(if any)
# 4. Generate Clock and Reset sequence
# 5. Toggle inputs across the Simulation time
# 6. Observe (and monitor) output
# 7. Keep a "final" kind of block to print Simulation summary
# 8. Add a initial block to dump fsdb/vcd(waves etc)
def write_tb(top):
    tb= open("tb_"+top+".v","w")
    tb.write("module tb_"+top+"();")

def main():
    lines = read_design(file)
    top = get_top_module(lines)
    print("Top module found: "+top)
    write_tb(top)

if __name__ == '__main__':
    main()