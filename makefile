default:
	sbatch job.sh
job:
	rm -rf job*.sh
slurm:
	rm -rf slurm*
clean:
	rm -rf OutputLogs/* OutputPlots/* OutputValues/* slurm*