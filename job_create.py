a = [1, 1e-1, 1e-2, 1e-4]
#b = [10^12]
points = [8, 16, 32, 64, 128, 256, 512, 1024]


for i in a:
    value_a = float(i)
    for point in points:
        n_points = int(point)
        if value_a == 1:
          with open(f'job_a_{value_a}.sh', 'a') as f:
              line = f'\npython3 Experiment2.py -a {value_a} -p {n_points} > OutputLogs/a_{value_a}_p_{n_points}.txt'
              f.write(line)
        elif value_a == 1e-1:
          with open(f'job_a_{value_a}.sh', 'a') as f:
              line = f'\npython3 Experiment2.py -a {value_a} -p {n_points} > OutputLogs/a_{value_a}_p_{n_points}.txt'
              f.write(line)
        elif value_a == 1e-2:
          with open(f'job_a_{value_a}.sh', 'a') as f:
              line = f'\npython3 Experiment2.py -a {value_a} -p {n_points} > OutputLogs/a_{value_a}_p_{n_points}.txt'
              f.write(line)
        elif value_a == 1e-4:
          with open(f'job_a_{value_a}.sh', 'a') as f:
              line = f'\npython3 Experiment2.py -a {value_a} -p {n_points} > OutputLogs/a_{value_a}_p_{n_points}.txt'
              f.write(line)
