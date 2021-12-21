#!/bin/sh

for shfile in job*.sh
do
    sbatch ./$shfile
done