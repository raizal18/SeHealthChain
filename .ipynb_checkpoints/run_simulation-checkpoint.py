import os
import sys
import math
import json
import numpy as np
## RUN simulator_config.py in Different terrminal before start Simulation
from intiate_simpy import run_simulator
import pickle
import subprocess
import time

# os.system('powershell.exe py simulator_config.py')
subprocess.call('powershell.exe py simulator_config.py')
time.sleep(5)

(CumThroughPut, ThrouputPerNode, userLatencyShard, userlatencyNode, NUMBEROFNODES, NUMBEROFSHARD) = run_simulator()

with open('base.pkl','wb') as f:
    pickle.dump([CumThroughPut, 
ThrouputPerNode,  
userLatencyShard,  
userlatencyNode, 
NUMBEROFNODES, NUMBEROFSHARD],f)








