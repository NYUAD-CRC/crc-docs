Quick Intro to Job Submission
=============================

Things to Keep in mind
----------------------

.. list-table::
	:widths: auto
	
	* - **Types of Jobs**
	  - The jobs are basically categorized into four types based on their resource requirements (Small,Medium,Large,XLarge).
	* - **Quick Testing**
	  - Use the prempt partition for quick testing of your code. More details below.
	* - **Special jobs**
	  - Nvidia (GPU), bigmem (Large memory) jobs fall into this category and are limited in resource.
	* - **Default WallTime**
	  - The default Wall time of all the jobs is 5 hours (except for ``preempt`` partition). Each type of job has a different Max WallTime limit discussed below.
	* - **Default Memory**
	  - By Default, 3.75GB of memory is assigned to every CPU requested. So if 4 CPUs (``#SBATCH -n 4``) are requested, the assigned memory would be 15GB.
	
- **Partitions**:

	- ``compute``: General purpose partition for all the normal runs
	- ``nvidia`` : Partition of GPU jobs
	- ``bigmem`` : Partition for large memory jobs. Only jobs requesting more than 500GB will fall into this category.
	- ``prempt`` : Supports all types of jobs with a grace period of 30 minutes. More on this :ref:`here <preempt_partition>`
	- ``xxl``    : Special partition for grand challenge applications. Requires approval from management.
	- ``visual`` : We also have a few nodes which give you the liberty of running applications with GUI.

.. _partitions_summary:	
	
Partitions Summary
------------------


.. list-table:: 
	:widths: auto 
	:header-rows: 1

	*	- 
		- Partition
		- Job Type
		- (min,max)CPUs
		- Max Time
		- Max Jobs
		- Example
		- Remarks
	*	- 1
		- ``compute``
		- 
		-
		-
		-
		-
		-
	*	- 
		- 
		- Small
		- (1,64)
		- 7 days
		- 200
		- 
			.. code-block:: bash

				#SBATCH -p compute
				#SBATCH -n 25
		
			

		- The small jobs will be forwarded, preferably to Dalma nodes.
	*	- 
		- 
		- Medium	
		- (28,512)
		- 7 days
		- 20
		- 
			.. code-block:: bash

				#SBATCH -p compute
				#SBATCH -n 56
		- 
	*	- 
		- 
		- Large
		- (256,2048) 
		- 2 days
		- 6
		- 
			.. code-block:: bash

				#SBATCH -p compute
				#SBATCH -n 1024
		- 
	*	- 
		- 
		- XLarge
		- (1024,4096) 
		- 2 days
		- 3
		- 
			.. code-block:: bash

				#SBATCH -p compute
				#SBATCH -n 4000

		-
	*	- 2
		- ``nvidia``
		- GPU
		- (1,80)
		- 4 days
		- 8
		- 
			.. code-block:: bash

				#SBATCH -p nvidia
				#SBATCH --gres=gpu:1


		- Max GPUs:8
	*	- 3
		- ``bigmem``
		- Large Memory Jobs
		- (1,40)
		- 4 days
		- 2
		- 
			.. code-block:: bash

				#SBATCH -p bigmem
				#SBATCH --mem=700G

		- Jobs requesting more than 480GB will be fowarded to bigmem
	*	- 4
		- ``preempt``
		- 
		-
		-
		-
		-
		-
	*	- 
		- 
		- preempt-small
		- (1,28)
		- 7 days
		- 1200
		- 
			.. code-block:: bash

				#SBATCH -p preempt
				#SBATCH -n 25
				#SBATCH -t 12:00:00
		
			

		- grace period of 30 mins	
	*	- 
		- 
		- preempt-big
		- (28,8192)
		- 7 days
		- 100
		- 
			.. code-block:: bash

				#SBATCH -p preempt
				#SBATCH -n 8100
				#SBATCH -t 15:00:00
		
			

		- grace period of 30 mins
	*	- 
		- 
		- preempt-gpu
		- (1,16)
		- 7 days
		- 12
		- 
			.. code-block:: bash

				#SBATCH -p preempt
				#SBATCH -n 14
				#SBATCH --gres=gpu:3
				#SBATCH -t 20:00:00
		
			

		- grace period of 30 mins Max GPUs:8
    	
    	
Sample Job Script
------------------

A job script consists of 2 parts:
	a. Resources requirement.
	b. Commands to be executed.

**Points to be noted**

	- **Ask only what you need**
	- Serial jobs would need only one CPU (``#SBATCH -n 1``)
	- Make sure the walltime specified is not greater than the allowed time limit. More details can be found :ref:`here <partitions_summary>`.
	- By Default 3.75GB of memory is assigned for each CPU allocated and hence defining the memory requirement is optional  
	
.. admonition:: Difference between CPUs,Cores and Tasks

	- On Jubail HPC, One CPU is equivalent to one Core. Jubail also has 128 CPUs per node.
	- In Slurm, the resources (CPUs) are allocated in terms of tasks which are denoted by ``-n`` or ``--ntasks``. 
	- By Default, the value of ``-n`` or ``--ntasks`` is one if left undefined.
	- By Default, Each task is equivalent to one CPU.
	- But if you have defined ``-c`` or ``--cpus-per-task`` in your job script, then the total number of CPUs allocated to you would be the multiple of ``-n`` and ``-c``.
	    
.. code-block:: bash

 #!/bin/bash

 #Define the resource requirements here using #SBATCH

 #For requesting 10 CPUs
 #SBATCH -c 10

 #Max wallTime for the job
 #SBATCH -t 24:00:00  	

 #Resource requiremenmt commands end here

 #Add the lines for running your code/application
 module purge
 module load abc

 #activate any environments if required
 conda activate myenv

 #Execute the code
 python abc.py
   
**Common Job submission arguments:**

* ``-n``   Select number of tasks to run (default 1 core per task)
* ``-N``   Select number of nodes on which to run
* ``-t``   Wallclock in days-hours:minutes:seconds (ex 4:00:00)
* ``-p``   Select partition (compute, gpu, bigmem)
* ``-o``   Output file ( with no ``–e`` option, err and out are merged to the Outfile)
* ``-e``   Keep a separate error File
* ``-d``   Dependency with prior job (ex don't start this job before job XXX terminates)
* ``-A``   Select account (ex physics_ser, faculty_ser)
* ``-c``   Number of cores required per task (default 1)
* ``--ntasks-per-node`` Number of tasks on each node
* ``--mail-type=type`` Notify on state change: BEGIN, END, FAIL or ALL
* ``--mail-user=user`` Who to send email notification
* ``--mem`` Maximum amount of memory per job (default is in MB, but can use GB suffix) (Note: not all memory is available to jobs, 8GB is reserved on each node for the OS) (So a 128GB node can allocate up to 120GB for jobs)

#SBATCH with ``-n`` , ``-c`` and ``-N``
---------------------------------------

It may sometimes be confusing to select between ``-n``, ``-c`` and ``-N``. The following section attempts to 
describe the difference between these parameters. 

- ``-n`` refers to number of tasks. Tasks can communicate across the nodes.
- If the number of tasks, is greater than one, it is possible that they may distributed across multiple nodes.
- ``-c`` refers to number of cpus per task.
- ``-c`` is always confined to a single node and is beneficial for multithreaded jobs.
- ``-N`` assigns the tasks to ``N`` number of nodes.
- Each task is by default assigned one cpu and each task is by default assigned a single node.
- The values of ``-n``, ``-c`` and ``-N`` are by default 1, if not specified.


.. list-table::
	:widths: auto
	:header-rows: 1

	* - Command
	  - Behaviour
	* - 
		.. code-block:: bash

			#SBATCH -n 10
		
	  -
	  	- Same as ``#SBATCH --ntasks=10``

	  	- 10 CPUs are assigned in this case

	  	- CPUs can be assigned in the same node or across multiple nodes.

		- Not recommended for multithreaded jobs or jobs needed to be confied to a single node.
	* -
	 	.. code-block:: bash

			#SBATCH -c 10

	  -
	  	- Same as ``#SBATCH --cpus-per-task=10``
		- 10 CPUs are assigned in this case 
		- CPUs are assigned within a single node
		- Recommended for multithreaded jobs (most python jobs).
	* - 
		.. code-block:: bash

			#SBATCH -N 1
			#SBATCH -n 10

	  -
		- ``-N`` parameter is same as ``--nodes``
		- 10 CPUs are assigned in this case
		- CPUs are assigned to number nodes specified to the parameter ``N`` (1 in this case)
		- Useful to run jobs across selected number of nodes (mostly for MPI jobs).

	* - 
		.. code-block:: bash

			#SBATCH -n 10
			#SBATCH -c 20

	  -
	  	- 200 CPUs are assigned ( 20 for each task).
		- Combination of 20 CPUs spread across 10 nodes.
		- Should be used with caution 
		- Not recommended for python jobs
			


Basic SLURM Commands
--------------------

SLURM is the Resource Manager we use to schedule the jobs to the resources according to the requirements specified. Bellow are
a few of the basic commands a user can use for his/her jobs:

.. list-table:: 
        :widths: auto 
        :header-rows: 1

        *       - **Command**
                - **Descirption**
        *       - 
                        .. code-block:: bash
                                
                             sbatch file1

                - ``sbatch`` command is used to submit a job to the queue. Here ``file1`` is the job script
                  containing the details of resource requirements and commands to be executed.
        *       - 
                        .. code-block:: bash
                                
                                squeue

                - ``squeue`` command shows all your jobs (Runing and Pending) present in the queue
        *       - 
                        .. code-block:: bash

                                scancel 127445
                                scancel -u wz22

                - ``scancel`` commands allows you to cancel your jobs in the queue. You can cancel a single job using the job id
                  or you can cancel all the jobs using your NetId.

 
 
 
 
Requesting a GPU node
---------------------
To request a Gpu node you have two options:

* Requesting only one GPU card of any type
	    
.. code-block:: bash

	#SBATCH -p nvidia
	#SBATCH --gres=gpu:1

* Requesting only one GPU card of a specific type( available types are v100 and a100)
	    
.. code-block:: bash

	#SBATCH -p nvidia
	#SBATCH --gres=gpu:a100:1

If you would like to analyze your GPU jobs, Please refer to following section: :doc:`Analyzing GPU Usage</hpc/jobs/gpu_jobs>`

For more details regarding GPU nodes and cards types, kindly check this section :doc:`GPU nodes</hpc/system/gpu_nodes>`.

.. _preempt_partition:
   
Preempt Partition
-----------------

- **Limitless high priority queue** with the caveat that the jobs can be preempted (killed) to make space for other jobs demanding resources.
- A grace period of 30 mins is given to the job to allow some time for a smooth termination or checkpointing, if needed.
- We intend to increase the machine occupancy and reduce the waiting time in queues for those jobs that may have short runtime or are meant to be for testing ,otherwise jobs will be treated as regular jobs.
- Default Walltime: 2 hours
- Maximum Walltime: 7 days
 


 	
