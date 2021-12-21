import os
 
path = "/home/jbrahmbhatt/ODEN/OutputPlots"
for x in os.listdir(path):
    with open(f'experiment2_report.md', 'a') as f:
            line = f'![](OutputPlots/{x})\n'
            f.write(line)