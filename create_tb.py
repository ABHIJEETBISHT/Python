import re
import os

if(os.path.exists("mux.v")):
    print("Found !")

#Script Steps
# 1. Get top module
# 2. Get IO ports
# 3. Detect Clock and Reset(if any)
# 4. Generate Clock and Reset sequence
# 5. Toggle inputs across the Simulation time
# 6. Observe (and monitor) output
# 7. Keep a "final" kind of block to print Simulation summary
# 8. Add a initial block to dump fsdb/vcd(waves etc)