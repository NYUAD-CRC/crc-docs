Job Array
==========
The SLURM provides one of the simplest method to run parallel computations.
Frequently we need to run the same application / job
script several times for either:

* Processing multiple independent input files
* Looking for an optimal set of input parameters for the same input file (eg parametric analysis)
* You have a code whose major work is looping through iterations which are independent of each other

For instance you may need to process the results of 50
experiments. Then you can 

* Prepare a single job script which processes all 50 experiments, one at a time,or
* Prepare 50 job scripts which process concurrently the experiments, one experiment per job.

In either case this is not an optimal use of your time.
The solution is to process your experiments using a job
array; the script will be executed 50 times but each time
it runs the counter will be different. You can use the
counter to refer to each experiment input as in the job
script to the left.

Consider another example where you have a python script whose most time consuming part is an iterating loop with independent iterations.
Instead of looping through each of the iterations one by one, you can use the SLURM job array to run it in parallel.

The individual tasks in the array are distinguished by an environment variable, ``$SLURM_ARRAY_TASK_ID`` , which Slurm sets to a different value for each task. You set the range of values with the ``--array`` or ``-a`` parameter.

Examples of the ``--array`` parameter
-------------------------------------
.. code-block:: bash

    sbatch --array=0-7       # $SLURM_ARRAY_TASK_ID takes values from 0 to 7 inclusive
    sbatch --array=1,3,5,7   # $SLURM_ARRAY_TASK_ID takes the listed values
    sbatch --array=1-7:2     # Step-size of 2, same as the previous example
    sbatch --array=1-100%10  # Allows no more than 10 of the jobs to run simultaneously

A simple example
----------------
Suppose you have multiple files you wish to process by passing to another code.

.. code-block:: bash

    #!/bin/bash		
    #Processing	for each experiment requires a single core	
    #The input files are named file.1, file.2,..., file.50	
    #SBATCH –n 1	
    #SBATCH –a 1-50

    #your application commands go here
    ./my-code file.${SLURM_ARRAY_TASK_ID}

File of commands
-----------------
Sometimes, it may be easier to write out a file with a list of command lines to execute, one per line. For example, you have multiple instances of a ``python`` program with different 
set of arguments to run. In this case, your "file of commands" could look like:

``jobs.txt``:

.. code-block:: bash

    python myProgram.py arg1 arg2
    python myProgram.py arg3 arg4
    python myProgram.py arg5 arg6

Now you can write a job submission script that looks like:

``submit.sh``:

.. code-block:: bash

    #!/bin/bash

    #SBATCH --cpus-per-task=1
    #SBATCH --array=1-3

    srun $(head -n $SLURM_ARRAY_TASK_ID jobs.txt | tail -n 1)
    
Note in the above example ``--array=1-3`` - the last number corresponds to the total number of jobs (or command lines) in your " file of commands" ``jobs.txt`` file. The ``head -n ... | tail -n 1`` part is just a simple trick to read the ``$SLURM_ARRAY_TASK_ID`` th line from the file (for example, if the task ID is 3, ``head`` reads the first 3 lines from ``jobs.txt``, and then ``tail`` takes the last line from those 3 lines, which is of course the 3rd line in the file.)

Now you can submit this to the cluster by doing:

.. code-block:: bash

    sbatch submit.sh

A job array looks like a normal job, except that the jobid is extended with a taskid – eg ``466546_[1-50]`` and
``466565_1`` .
If the system is idle all the array jobs will be run concurrently. But in practice you will see some jobs running, and some jobs waiting for their turn to run.

Job array processing can be used for serial, multithreaded and MPI jobs alike.
You can kill all jobs in a job array with ``scancel 466546`` or an individual job with ``scancel 466546_42`` for example. You can also refer to a range of taskids such as ``scancel 466546_[3-17]`` .
Each job in the job array will have its own output file (and error file if you are submitting with ``-e``). So you have to be careful with not exceeding the 1000 files per directory limit! You may split the outputs in multiple directories or use the parallel job array tool described next.

.. important::
    If you have a job with independent computations, then 
    :doc:`Job arrays </hpc/jobs/job_array>` and :doc:`Parallel Job Array </hpc/jobs/parallel_job_array>`  
    are one of the most easiest ways to parallelize 
    your computations. Follow the corresponding highlighted links for a much more detailed example.