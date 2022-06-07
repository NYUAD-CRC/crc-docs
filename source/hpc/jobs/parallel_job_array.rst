Parallel Job Array
==================

There are times, however, when even a job array doesn't really fit your needs. For instance, you may be looking at running 300,000 very short running jobs. Or maybe, the complexity to search through all the output files or having to manually "glue" them back together into a single output file is too demanding. Or maybe it's too difficult to match SLURM's taskids to actual input file names or parametric analysis. Or more probably the time delay between each jobs being scheduled to run is slowing down your processing as your jobs are really short

.. code-block:: bash

    ./process-one-resuls file.1	
    ./process-one-resuls file.2	
    ./process-one-resuls file.3	
    ...	
    ./process-one-result file.50000

For these cases Jubail has the "parallel job array" system– an NYU Abu Dhabi in-house tool – designed to make running large number of jobs even simpler.

To submit a parallel job array you need to prepare a file (eg: ``list_of_commands.txt`` ) ,where each line represents a single job to execute. You can have multiple Linux commands on a line as:

.. code-block:: bash

    myprogram1
    export V=42; myprogram2 | myprogram3
    myprogram4; myprogram5 < inp
    myprogram6 > out

Then you pass the file to the tool and it automatically submits the job array for you.

.. code-block:: bash

    slurm_parallel_ja_submit.sh list_of_commands.txt

The tool splits all jobs into groups and proceeds to run them as a normal job array. 
During execution all jobs within a group are split across the cores of a compute node and run in parallel.

The output is gathered into files, 1 output file per group and 1 error file per group; 
the output is ordered to make things easy for you.

You get significant performance gains by eliminating the job scheduling 
overhead and the queuing delay for each job.

The parallel job array tool allows you to set the time limit for each node – **not each job**!, 
the processor type (sse, or avx2) and the partition, this is useful if your research group has its "compute condo", and the number of nodes to use.

The parallel job array tool determines an optimal number of nodes to use 
It groups all jobs into groups then processes them using conventional job array. 

The number of "nodes" corresponds actually to the number of groups, which is the number of tasks for the job array. 

The time limit parameter applies to the groups – eg an entire group must complete within the time limit.

.. admonition:: More on the **TimeLimit** parameter

    For example:
    Let's say you have an input file ``list_of_commands.txt`` with 10000 commands to run. 
    Let's also assume each command utilizes a single CPU (serial job) an takes around **5 minutes per command (job)**.

    Suppose you specified the ``-N`` parameter (which corresponds to number of nodes) to as eight while
    submitting the "parallel job array". This means that the 10000 jobs of yours are now divided in 8 groups,
    with 

    ::

        Number of jobs per group = 10000/8 = 1250

    Now each group of job will run on one node and each standard compute node on Jubail has 128 CPUs (cores).
    This means that per each core (CPU), we will have 

    ::

        Number of jobs per core (CPU) = 1250/128 = 9 (+1) 
        Hence, total time per CPU = 10 * 5 minutes = 50 minutes

    .. note::

        The ``+1`` factor comes with the fact that since ``1250`` isn't perfectly divisible by ``128``, the reminder is distributed 
        among the different cores in a round robin fashion.

    This is the estimated time it will take a group of jobs (1250) to complete on a single node.

    **Hence, while submitting the ``parallel job array`` it will be good to specify this TimeLimit as well, as
    the lower the walltime, the higher is the probability for the faster allocation of resources.**

    ::

        >> slurm_parallel_ja_submit.sh -N 8 -t 50:00

             


.. code-block:: bash

    >> slurm_parallel_ja_submit.sh –h
    slurm_parallel_ja_submit.sh options:
    -C <constraint> (avx2 or sse)
    -t <time limit HH:MM:SS>
    -p <partition>
    -N <number of nodes>
.. important::
    The parallel job array tool propagates your environment, 
    and loaded modules, to all jobs. 

The tool also support OpenMP jobs, so you can set the number of threads before launching your parallel job array.

.. code-block:: bash

    $> #export the required number of threads
    $> #in the current environment
    $> #before submitting the jobs
    $> 
    $> #For example
    $> export OMP_NUM_THREADS=4
    $> slurm_parallel_ja_submit.sh -N 8 -t 50:00 list_of_commands.txt

By default the tool will allow up to 8 "nodes" (groups). 
You can increase the number of nodes when there is a very large 
number of jobs to process to run faster, or when the groups can't finish within the time limit

Here is how a complete example looks like.  

.. code-block:: bash

    $> cat list_of_commands.txt
    echo processing 1
    echo processing 2
    ...
    echo processing 10000


    $> export OMP_NUM_THREADS=4
    $> slurm_parallel_ja_submit.sh -N 8 -t 50:00 list_of_commands.txt 
    Entered number of nodes to use: 8
    Entered walltime: 50:00
    Input: list_of_commands.txt
    Actual maximum number of nodes that will be used: 8
    Submitting parallel job array using the following modules:
    No Modulefiles Currently Loaded.
    Submitting parallel job array with OMP_NUM_THREADS= 4
    Submitted batch job 265340


    $> squeue
                 JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
          265340_1   compute   sbatch  ms13779  R       0:03      2 cn[107,110]
          265340_2   compute   sbatch  ms13779  R       0:03      2 cn[163,189]
          265340_3   compute   sbatch  ms13779  R       0:03      2 cn[190-191]
          265340_4   compute   sbatch  ms13779  R       0:03      2 cn[192-193]
          265340_5   compute   sbatch  ms13779  R       0:03      4 cn[041,043,049,146]
          265340_6   compute   sbatch  ms13779  R       0:03      4 cn[050,203-205]
          265340_7   compute   sbatch  ms13779  R       0:03      3 cn[206-208]
          265340_8   compute   sbatch  ms13779  R       0:03      3 cn[209-211]

    
    $> ls list_of_commands.txt-265340_*
    list_of_commands.txt-265340_1.err  list_of_commands.txt-265340_2.err  list_of_commands.txt-265340_3.err  list_of_commands.txt-265340_4.err  
    list_of_commands.txt-265340_5.err  list_of_commands.txt-265340_6.err  list_of_commands.txt-265340_7.err  list_of_commands.txt-265340_8.err  
    list_of_commands.txt-265340_1.out  list_of_commands.txt-265340_2.out  list_of_commands.txt-265340_3.out  list_of_commands.txt-265340_4.out  
    list_of_commands.txt-265340_5.out  list_of_commands.txt-265340_6.out  list_of_commands.txt-265340_7.out  list_of_commands.txt-265340_8.out
    
    
    $> cat list_of_commands.txt-265340_1.out
    ============= job 1 ============
    processing 1
    ============= job 2 ============
    processing 2
    ...
    processing 1249
    ============= job 1250 ============
    processing 1250


    $> cat list_of_commands.txt-265340_8.out
    ============= job 8751 ============
    processing 8751
    ============= job 8752 ============
    processing 8752
    ...
    ============= job 9999 ============
    processing 9999
    ============= job 10000 ============
    processing 10000

For compatibilty with existing job array scripts you can
use the ``SLURM_ARRAY_TASK_ID`` environment variable
in your parallel job array processing.
Here the ``list4.txt`` input file contains the line ``./ja.sh`` 1000
times.

An additional benefit of parallel job array processing is
that you are not limited to SLURM's ``MaxSubmit`` and
``MaxJobs account`` / user limits.
Whereas you can submit a maximum of 200 jobs, using parallel job array you have no
such limits.

.. code-block:: bash

    $> cat ja.sh
    #!/bin/bash
    #SBATCH -n 1
    #SBATCH -a 1-1000
    sleep 5
    echo -n $SLURM_ARRAY_TASK_ID " "
    date

    $> sbatch ja.sh

    $> cat list4.txt
    ./ja.sh
    ./ja.sh
    ...
    ./ja.sh

    $> slurm_parallel_ja_submit.sh list4

