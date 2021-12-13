Batch Job
=========

Besides interactive sessions, a user can submit batch jobs to the system. For production jobs, batch jobs should be used. You could also visit the quick intro guide :doc:`here <quick_start>`

A complete batch job workflow:

1. Write a job script, which consists of 2 parts:
    a. Resources requirement.
    b. Commands to be executed.
2. Submit the job.
3. Relax, have a coffee, log off if you wish. The computer will do the work.
4. Come back to examine the result.

Batch Job Script
----------------

A job script is a text file describing the job. As discussed, the first part tells how much resources you want. The second part is what you want to run. Choose one of the following examples to start with. If you are not sure, contact us.

.. admonition:: Resources Limit

    The cluster is shared among the whole university. The HPC steering committee decides each year on resources limit for each department. We at NYUAD HPC center implement these limits.

**Kindly refer to the following :ref:`section <partitions_summary>` to know more about partitions and limits**


If you ask for more resources than you can use, your job will stay in the queue forever. (e.g., you specify 10000 hours walltime in your job script)

If you have multiple jobs (which is very normal), your jobs will start either immediately if the system is free and the quotas for you and your department have not been exhausted.

.. admonition:: Difference between CPUs,Cores and Tasks

	- On Jubail HPC, One CPU is equivalent to one Core. 
	- In Slurm, the resources (CPUs) are allocated in terms of tasks which are denoted by ``-n`` or ``--natsks``. 
	- By Default, the value of ``-n`` or ``--ntasks`` is one if left undefined.
	- By Default, Each task is equivalent to one CPU.
	- But if you have defined ``-c`` or ``--cpus-per-task`` in your job script, then the CPUs allocated to you would be the multiple the multiple of ``-n`` and ``-c``.

A Job with 1 CPU Core
---------------------

This is a very basic example, using only one CPU core.

.. code-block:: bash

    #!/bin/bash
    # Set number of tasks to run
    #SBATCH --ntasks=1
    # Walltime format hh:mm:ss
    #SBATCH --time=00:30:00
    # Output and error files
    #SBATCH -o job.%J.out
    #SBATCH -e job.%J.err
    
    # **** Put all #SBATCH directives above this line! ****
    # **** Otherwise they will not be effective! ****
    
    # **** Actual commands start here ****
    # Load modules here (safety measure)
    module purge
    # You may need to load gcc here .. This is application specific
    # module load gcc
    # Replace this with your actual command. 'serial-hello-world' for example
    hostname

As you can see, it is a simple bash script, 
plus some lines on the top, starting with ``#SBATCH``, 
which are the Slurm directives.

Those Slurm directives specify resources required. E.g., ``–ntasks=1`` 
is 1 CPU core. ``–time=00:30:00`` means the maximum walltime is 30 mins. ``-o job.%J.out`` is redirecting the 
stdout, usually your screen output, to a file called ``job.$JOBID.out``. 
Why? Because the system will run your job in the background, hence no display.

Everything under the Slurm directives is normal Linux command. 
This example runs ``hostname``, which will print the hostname. 
In reality, you should load your desired modules, and execute 
whatever you want to run.

Multithreading Job
------------------

Multithreading enables a process to spawn multiple threads to accelerate its execution. The most common multithreading model in HPC is OpenMP. If your application supports this (not sure? contact us to find out), you could use the below example. 

.. code-block:: bash

    #!/bin/bash
    # Set number of tasks to run
    #SBATCH --ntasks=1
    # Set the number of CPU cores for each task
    #SBATCH --cpus-per-task=4
    # Walltime format hh:mm:ss
    #SBATCH --time=00:30:00
    # Output and error files
    #SBATCH -o job.%J.out
    #SBATCH -e job.%J.err
    
    # **** Put all #SBATCH directives above this line! ****
    # **** Otherwise they will not be effective! ****
    
    # **** Actual commands start here ****
    # Load modules here (safety measure)
    module purge
    # You may need to load gcc here .. This is application specific
    # module load gcc
    
    # If you are using OpenMP application, keep this line.
    export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
    
    # Replace this with your actual command. In this example, you should run a multithreading supported application
    hostname

Comparing to the previous examples, there are 2 extra lines:

1. ``#SBATCH --cpus-per-task=4``: this asks the system to assign 4 CPU cores per tasks. This number should be **no larger than and a divisor of 28 (e.g., 2, 4, 7, 14, 28)** because the majority of our nodes comes with 28 cores.
2. ``export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK``: this tells your applications, if OpenMP supported, to use all the CPU cores assigned to your job, by spawning an exact number of OpenMP threads.

Remember, running a job is 2 steps process: 

1. Request the resources. 
2. Use the resources. This example is a perfect illustration. **Run with what you requested, no more, no less**.

Pure MPI Job
------------

Now comes the pure MPI Jobs.

.. code-block:: bash

    #!/bin/bash
    # Set number of tasks to run
    # This number should be divisible by 128. E.g., 128,256...
    #SBATCH --ntasks=256
    # Walltime format hh:mm:ss
    #SBATCH --time=00:30:00
    # Output and error files
    #SBATCH -o job.%J.out
    #SBATCH -e job.%J.err
    
    # **** Put all #SBATCH directives above this line! ****
    # **** Otherwise they will not be effective! ****
    
    # **** Actual commands start here ****
    # Load modules here (safety measure)
    module purge
    # You may need to load gcc here .. This is application specific
    # module load gcc
    # Replace this with your actual command. 'serial-hello-world' for example
    srun hostname

Comparing to the 1 core example, there are 2 different lines:

1. ``#SBATCH --ntasks=128``: This line requests 128 cores. **This number should be divisible by 128. E.g., 128,256...**
2. ``srun hostname``: This tells your application to run with MPI support, utilizing all CPU cores requested. 

The old school ``mpiexec`` or ``mpirun`` are supported as well. But you need to load ``openmpi`` module in this case.

Hybrid MPI Job
--------------


If your application support MPI + OpenMP hybrid parallelization, you could follow this example to submit a hybrid job. 

.. code-block:: bash

    #!/bin/bash
    # Set number of tasks to run
    #SBATCH --ntasks=56
    # Set the number of CPU cores for each task
    #SBATCH --cpus-per-task=4
    # Walltime format hh:mm:ss
    #SBATCH --time=00:30:00
    # Output and error files
    #SBATCH -o job.%J.out
    #SBATCH -e job.%J.err
    
    # **** Put all #SBATCH directives above this line! ****
    # **** Otherwise they will not be effective! ****
    
    # **** Actual commands start here ****
    # Load modules here (safety measure)
    module purge
    # You may need to load gcc here .. This is application specific
    # module load gcc
    
    # If you are using Hybrid MPI + OpenMP application, keep this line.
    export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
    
    # Replace this with your actual command. 'serial-hello-world' for example
    srun hostname

In this case, 
1. the number of CPU cores requested is ``56 (ntasks) * 4 (cpus-per-task) = 224``. 
2. This number should be divisible by 28 to use all the cores on the nodes. As in the multithreading job example, make sure ``cpus-per-task`` is a divisor of 28.

