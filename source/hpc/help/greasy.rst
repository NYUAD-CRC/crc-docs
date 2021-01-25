"Greasy" Workload Management Tool
==================================

We want to introduce you the "greasy" tool. This tool will easy to implement "High Throughput Computing" (HTC) jobs on Dalma. HTC jobs  are usually concerned about resource availability and resilience normally for long running tasks. In most cases HPC environments are not suitable to run HTC workload and this is where Greasy can become a handy tool to use. It will help users to manage workflows with many serial tasks even if they have dependencies among them in an easy and robust way.


This is a tools which is still under development, so some improvements may come up in the future.

You can start by copying the example directory that you will find in the installation dir: 
/share/apps/NYUAD/greasy/openmpi_1.10.2/2.1/example/

Step-by-step guide
The first thing to notice is that there are two  files:


1.- the file with the tasks to do ( example.txt )

example.txt is the text file that contains the list of tasks to do.
There is a direct correspondence between the line number and the task index, so the line 11th in the file will correspond to the task with index 11.
The dependencies are expressed in the format [#  #] at the beginning of the line.
For more details about how to write dependencies please go to the user's guide

example.txt Collapse source
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
/bin/sleep 1
/usr/bin/hostname
/bin/sleep 3
/bin/sleep 4
/bin/sleep 5
/bin/sleep 6
 
###########################################
# These Lines with dependencies are correct 
###########################################
[# 5 #]         /bin/sleep 11 
[# -1#]         /bin/sleep 12
[#1-3#]         /bin/sleep 13
 
#########################
# these ones are not Ok
#########################
# sharps missing
[ 1 ]           /bin/sleep 22
[#1 ]           /bin/sleep 23
[ 1 #]          /bin/sleep 24
# Forward dependencies are not allowed
[# +1 #]        /bin/sleep 26
[# 1000 #]      /bin/sleep 27
# Dependencies must point to a task
[# -1 #]        /bin/sleep 29
# Dependencies must be numerical, and ranges must be expressed correctly
[# 2->6 #]      /bin/sleep 31
[# mistake #]   /bin/sleep 32
2.- the submission script ( dalma_greasy.job )


The file  dalma_greasy.job is the file you submit to queues
Greasy has different types of "engines" for different kinds of underlying hardware. In a cluster environment like Butinah you can use "mpi" engine by setting the environment variable in the submission script :


export GREASY_ENGINE=mpi
but this is the default engine so you don't have to put it in the script.

If you plan to use only one node for your tasks then you might like to set the engine to "thread". The following line would be fine if you run it on the superfat node which has 32 cores. Note that the number of workers are set to 32-1 since 1 is used for scheduling.
 

export GREASY_ENGINE=thread
export GREASY_NWORKERS=31
 

Please refer to the Greasy User's Guide for more config details

dalma_greasy.job Expand source
 

3.- Running Greasy  is simple: 

prepare your tasks file
load the module

 

$> module load greasy
$> module load openmpi
submit the job

$> sbatch dalma_greasy.job
 

4.- Getting the results  is also very simple: 

Check the log file ( GREASY_LOGFILE ) for progress. In this file you can also check the resources utilization so you can tune your runs to make a more efficient use of the cluster.
To see different colors for different kind of messages, use the tool "greasycolorlog"
$> cat greasy.log | greasycolorlog Collapse source
$> cat greasy.log | greasycolorlog
 
[2014-01-30 11:12:35] Start greasing /scratch/jonarbo/apps/runs/greasy/example/example.txt
[2014-01-30 11:12:35] WARNING: Task 23 does not seem to be correct. Skipping...
[2014-01-30 11:12:35] WARNING: Task 26 does not seem to be correct. Skipping...
[2014-01-30 11:12:35] WARNING: Task 31 does not seem to be correct. Skipping...
[2014-01-30 11:12:35] WARNING: Task 32 does not seem to be correct. Skipping...
[2014-01-30 11:12:35] WARNING: Dependency 1000 of task 27 is not valid.
[2014-01-30 11:12:35] WARNING: Dependency 28 of task 29 is not valid.
[2014-01-30 11:12:35] WARNING: Invalid tasks found. Greasy will ignore them
[2014-01-30 11:12:35] INFO: MPI engine is ready to run with 23 workers
[2014-01-30 11:12:35] INFO: Allocating task 1
[2014-01-30 11:12:35] INFO: Allocating task 2
[2014-01-30 11:12:35] INFO: Allocating task 3
[2014-01-30 11:12:35] INFO: Allocating task 4
[2014-01-30 11:12:35] INFO: Allocating task 5
[2014-01-30 11:12:35] INFO: Allocating task 6
[2014-01-30 11:12:35] INFO: Allocating task 15
[2014-01-30 11:12:35] INFO: Allocating task 22
[2014-01-30 11:12:35] INFO: Allocating task 24
[2014-01-30 11:12:35] ERROR: Task 15 failed with exit code 32512 on node compute-6-26.local. Elapsed: 00:00:00
[2014-01-30 11:12:35] ERROR: Task 24 failed with exit code 512 on node compute-6-26.local. Elapsed: 00:00:00
[2014-01-30 11:12:35] ERROR: Task 2 failed with exit code 32512 on node compute-6-26.local. Elapsed: 00:00:00
[2014-01-30 11:12:35] WARNING: Cancelling task 13 because of task 2 failure
[2014-01-30 11:12:35] ERROR: Task 22 failed with exit code 512 on node compute-6-26.local. Elapsed: 00:00:00
[2014-01-30 11:12:36] INFO: Task 1 completed successfully on node compute-6-26.local. Elapsed: 00:00:01
[2014-01-30 11:12:38] INFO: Task 3 completed successfully on node compute-6-26.local. Elapsed: 00:00:03
[2014-01-30 11:12:39] INFO: Task 4 completed successfully on node compute-6-26.local. Elapsed: 00:00:04
[2014-01-30 11:12:40] INFO: Task 5 completed successfully on node compute-6-26.local. Elapsed: 00:00:05
[2014-01-30 11:12:40] INFO: Allocating task 11
[2014-01-30 11:12:40] INFO: Allocating task 14
[2014-01-30 11:12:41] INFO: Task 6 completed successfully on node compute-6-26.local. Elapsed: 00:00:06
[2014-01-30 11:12:51] INFO: Task 11 completed successfully on node compute-6-26.local. Elapsed: 00:00:11
[2014-01-30 11:12:51] INFO: Allocating task 12
[2014-01-30 11:12:54] INFO: Task 14 completed successfully on node compute-6-26.local. Elapsed: 00:00:14
[2014-01-30 11:13:03] INFO: Task 12 completed successfully on node compute-6-28.local. Elapsed: 00:00:12
[2014-01-30 11:13:03] INFO: MPI engine finished
[2014-01-30 11:13:03] INFO: Summary of 19 tasks: 8 OK, 4 FAILED, 1 CANCELLED, 6 INVALID.
[2014-01-30 11:13:03] INFO: Total time: 00:00:28
[2014-01-30 11:13:03] INFO: Resource Utilization: 8.69%
[2014-01-30 11:13:03] INFO: Creating restart file /scratch/jonarbo/apps/runs/greasy/example/example.txt.rst...
[2014-01-30 11:13:03] INFO: Restart file created
[2014-01-30 11:13:03] Finished greasing /scratch/jonarbo/apps/runs/greasy/example/example.txt
 

5.- Restarting the job 

Restarting a job can be done easily because Greasy will create a restart file with the that were not completed and it will include some clues about what went wrong so the user can fix it and use the restart file for the next submission.

example.txt.rst Collapse source
#  
# Greasy restart file generated at 2014-01-30 11:13:03
# Original task file: /scratch/jonarbo/apps/runs/greasy/example///scratch/jonarbo/apps/runs/greasy/example/example.txt
# Log file: /scratch/jonarbo/apps/runs/greasy/example/greasy.log
# 
 
# Warning: Task 2 failed
/usr/bin/hostname
# Warning: Task 13 was cancelled due to a dependency failure
[# 8 #] /bin/sleep 13
# Warning: Task 15 failed
/usr/bin/hostname
# Warning: Task 22 failed
[ 1 ] /bin/sleep 22
# Warning: Task 24 failed
[ 1 #] /bin/sleep 24 
 
# Invalid tasks were found. Check these lines on /scratch/jonarbo/apps/runs/greasy/example/example.txt: 
# 23, 26, 27, 29, 31, 32
 
# End of restart file
 