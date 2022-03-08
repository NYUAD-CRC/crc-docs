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
		- (1,28)
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
		- 10
		- 
			.. code-block:: bash

				#SBATCH -p compute
				#SBATCH -n 1024
		- 
	*	- 
		- 
		- XLarge
		- (512,4096) 
		- 2 days
		- 5
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
		- 4
		- 
			.. code-block:: bash

				#SBATCH -p nvidia
				#SBATCH --gres=gpu:1


		- Max GPUs:4
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
		- short high priority
		- No Limit
		- cpus<28:24h, cpus>28:12h
		-
		- 
			.. code-block:: bash

				#SBATCH -p preempt
				#SBATCH -n 128
				#SBATCH -t 10:00:00
          		 
				
				
				
		- grace period of 30 mins
    	
    	
Sample Job Script
------------------

A job script, which consists of 2 parts:
	a. Resources requirement.
	b. Commands to be executed.

**Points to be noted**

	- **Ask only what you need**
	- Serial jobs would need only one CPU (``#SBATCH -n 1``)
	- Make sure the walltime specified is not greater than the allowed time limit. More details can be found :ref:`here <partitions_summary>`.
	- By Default 3.75GB of memory is assigned for each CPU allocated and hence defining the memory requirement is optional  
	
.. admonition:: Difference between CPUs,Cores and Tasks

	- On Jubail HPC, One CPU is equivalent to one Core. Jubail also has 128 CPUs per node.
	- In Slurm, the resources (CPUs) are allocated in terms of tasks which are denoted by ``-n`` or ``--natsks``. 
	- By Default, the value of ``-n`` or ``--ntasks`` is one if left undefined.
	- By Default, Each task is equivalent to one CPU.
	- But if you have defined ``-c`` or ``--cpus-per-task`` in your job script, then the total number of CPUs allocated to you would be the multiple of ``-n`` and ``-c``.
	    
.. code-block:: bash

 #!/bin/bash

 #Define the resource requirements here using #SBATCH

 #For requesting 10 CPUs
 #SBATCH -n 10

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

For more details regarding GPU nodes and cards types, kindly check :ref:`this <partitions_summary>`

.. _preempt_partition:
   
Preempt Partition
-----------------

- **Limitless high priority queue** with the caveat that the jobs can be preempted (killed) to make space for other jobs demanding resources.
- A grace period of 30 mins is given to the job to allow some time for a smooth termination or checkpointing, if needed.
- We intend to increase the machine occupancy and reduce the waiting time in queues for those jobs that may have short runtime or are meant to be for testing ,otherwise jobs will be treated as regular jobs.
- Default Walltime: 2 hours
- Maximum Walltime depends on the job size:
	
	- cpus < 28 : 24 hours
	- cpus > 28 : 12 hours
 


 	
