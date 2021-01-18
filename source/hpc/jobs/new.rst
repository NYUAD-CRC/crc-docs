Interactive Sessions
--------------------

You could get an interactive session directly from your terminal, on compute nodes. Only short interactive jobs should be used (e.g., experimenting with new modifications to your Matlab code).

To start an interactive session, use srun command:

.. code-block:: bash

    srun --pty -n 1 /bin/bash

Then you can run your applications on the terminal directly. E.g., 

.. code-block:: bash

    [wz22@login-0-1 ~]$ srun --pty -n 1 /bin/bash
    srun: job 775175 queued and waiting for resources
    srun: job 775175 has been allocated resources
    [wz22@compute-21-1 ~]$

.. warning::
    In a real scenario, the system might be exhausted with no available resources to you. You need to wait in this circumstance.



In this example, user ``wz22`` requested 1 CPU core (``-n 1``) on login node (``login-0-1``). The system responded, assigned a job id (``775175``), queued the job and assigned 1 CPU core from one of the compute nodes (``compute-21-1``) to the user.

To exit the interactive session, type ``Ctrl+d``, or 

.. code-block:: bash

    exit    

Batch Job
---------

Besides interactive sessions, a user can submit batch jobs to the system. For production jobs, batch jobs should be used. 

A complete batch job workflow:

1. Write a job script, which consists of 2 parts:
    a. Resources requirement.
    b. Commands to be executed.
2. Submit the job.
3. Relax, have a coffee, log off if you wish. The computer will do the work.
4. Come back to examine the result.

**Batch Job Script**

A job script is a text file describing the job. As discussed, the first part tells how much resources you want. The second part is what you want to run. Choose one of the following examples to start with. If you are not sure, contact us.

.. admonition:: Resources Limit
    The cluster is shared among the whole university. The HPC steering committee decides each year on resources limit for each department. We at NYUAD HPC center implement these limits.

**Typically, a user can ask for 48 hours, 700 CPU cores maximum per job.**


If you ask for more resources than you can use, your job will stay in the queue forever. (e.g., you specify 10000 hours walltime in your job script)

If you have multiple jobs (which is very normal), your jobs will start either immediately if the system is free and the quotas for you and your department have not been exhausted.

**A Job with 1 CPU Core**

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

**Multithreading Job**

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

**Pure MPI Job**

Now comes the pure MPI Jobs.

.. code-block:: bash

    #!/bin/bash
    # Set number of tasks to run
    # This number should be divisible by 28. E.g., 56, 84, 112...
    #SBATCH --ntasks=56
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

1. ``#SBATCH --ntasks=56``: This line requests 56 cores. **This number should be divisible by 28. E.g., 56, 84, 112...**
2. ``srun hostname``: This tells your application to run with MPI support, utilizing all CPU cores requested. 

The old school ``mpiexec`` or ``mpirun`` are supported as well. But you need to load ``openmpi`` module in this case.

**Hybrid MPI Job**


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



Job Array
---------

This example shows how to submit a job array, 
consist of 100 jobs, with environmental variable ``SLURM_ARRAY_TASK_ID`` varies from 1 to 100.

.. code-block:: bash

    #!/bin/bash
    # Set number of tasks to run
    #SBATCH --ntasks=1
    # Walltime format hh:mm:ss
    #SBATCH --time=00:30:00
    # Output and error files
    #SBATCH -o job.%J.out
    #SBATCH -e job.%J.err
    #SBATCH -a 1-100
    
    # **** Put all #SBATCH directives above this line! ****
    # **** Otherwise they will not be effective! ****
    
    echo "I am running job $SLURM_ARRAY_TASK_ID"

Or you can varies ``SLURM_ARRAY_TASK_ID`` from 51 to 100.

.. code-block:: bash

    #SBATCH -a 50-100

Or set the maximum number of simultaneously running tasks from the job array to 10.

.. code-block:: bash

    #SBATCH -a 1-100%10

We only allow a maximum of 200 jobs in queue for any given user.

.. important::
    If you have a job with independent computations, then 
    :doc:`Job arrays </hpc/jobs/job_array>` and :doc:`Parallel Job Array </hpc/jobs/parallel_job_array>`  
    are one of the most easiest ways to parallelize 
    your computations. Follow the corresponding highlighted links for a much more detailed example.

Submitting a Job
----------------

Once you have your job script prepared, you could use the command 
**sbatch** to submit your job.

.. code-block:: bash

    sbatch <jobscript>

Let say if you saved your job script into a file called ``job.sh``. Then you should run the following.

.. code-block:: bash

    sbatch job.sh

After the submission, it will return the corresponding job id. E.g.,

.. code-block:: bash

    [wz22@login-0-1 overview]$ sbatch threads-job.sh
    Submitted batch job 775602

In this case, the job id is ``775602``. You can safely log off Dalma at this point. Once the system can accommodate your request, the script will be executed. The screen output will be saved to the files you specified in the job script.

Checking Job Status
-------------------

**Before and During Job Execution**

This command shows all your current jobs.

``squeue``

Example output:

.. code-block:: bash

    [wz22@login-0-1 ~]$ squeue -j 31408
                JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
                31408   ser_std  job1.sh     wz22  R       0:02      1 compute-21-4

It means the job with Job ID ``31408``, has been running (``ST: R``) for 2 minutes on ``compute-21-4``.

For more verbose information, use ``scontrol show job``.

.. code-block:: bash

    scontrol show job <jobid>

**After Job Execution**

Once the job is finished, the job can't be inspected by squeue or scontrol show job. At this point, you could inspect the job by sacct.

.. code-block:: bash

    sacct -j <jobid>

The following commands give you extremely verbose information on a job.

.. code-block:: bash

    sacct -j <jobid> -l


Canceling a Job
---------------

If you decide to end a job prematurely, use ``scancel``

.. code-block:: bash

    scancel <jobid>

.. admonition:: Use with Cautions
    
    To cancel all jobs from your account. Run this on Dalma terminal.

    .. code-block:: bash

        scancel -u <NetID>

