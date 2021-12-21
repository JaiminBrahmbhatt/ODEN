#!/bin/sh
python3 Experiment2.py -a 0.1 -p 8 > OutputLogs/a_0.1_p_8.txt
python3 Experiment2.py -a 0.1 -p 16 > OutputLogs/a_0.1_p_16.txt
python3 Experiment2.py -a 0.1 -p 32 > OutputLogs/a_0.1_p_32.txt
python3 Experiment2.py -a 0.1 -p 64 > OutputLogs/a_0.1_p_64.txt
python3 Experiment2.py -a 0.1 -p 128 > OutputLogs/a_0.1_p_128.txt
python3 Experiment2.py -a 0.1 -p 256 > OutputLogs/a_0.1_p_256.txt
python3 Experiment2.py -a 0.1 -p 512 > OutputLogs/a_0.1_p_512.txt
python3 Experiment2.py -a 0.1 -p 1024 > OutputLogs/a_0.1_p_1024.txt