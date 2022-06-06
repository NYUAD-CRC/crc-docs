How to use MATLAB Parallel Toolbox
==================================

One of the features users may want to use in jubail is Matlab's Parallel Toolbox.  

MATLAB Parallel Toolbox allows you to run parallel computations in multicore systems. For computer cluster and grid support you would need to use the MATLAB Distributed Computing Server which is not currently supported at NYUAD.
Parallel computations can be achieved either using  `parallel for-loops <https://www.mathworks.com/help/matlab/ref/parfor.html>`__ ,
`GPU computing <https://www.mathworks.com/solutions/gpu-computing.html>`__ .For more info visit 
the MATLAB documentation (`Get Started with Parallel Computing Toolbox <https://es.mathworks.com/help/parallel-computing/getting-started-with-parallel-computing-toolbox.html#brjw1fx-2>`__ )


In any case, for all these things to work, you will need to define a set of resources (cpus or workers) where the tasks will be executed.  The easiest way is to use the matlabpool command. This command has been replaced in recent versions for parpool.
Again, refer to the MATLAB documentation for details. 

Running a Serial MATLAB Job
---------------------------

A serial MATLAB job is one that requires only a single CPU-core. Here is an example of a trivial, 
one-line serial MATLAB script (``hello_world.m``):

.. code-block:: matlab

    fprintf('Hello world.\n')

The Slurm script (job.slurm) below can be used for serial jobs:

.. code-block:: bash

    #!/bin/bash
    #SBATCH --job-name=matlab        # create a short name for your job
    #SBATCH --nodes=1                # node count
    #SBATCH --ntasks=1               # total number of tasks across all nodes
    #SBATCH --cpus-per-task=1        # cpu-cores per task (>1 if multi-threaded tasks)
    #SBATCH --time=00:01:00          # total run time limit (HH:MM:SS)
    #SBATCH --mail-type=all          # send email on job start, end and fault
    #SBATCH --mail-user=<YourNetID>@nyu.edu

    #Load matlab module
    module purge
    module load matlab

    #Run Matlab via command line
    matlab -nojvm -singleCompThread -nodisplay -nosplash -nodesktop -batch hello_world

By invoking MATLAB with ``-nojvm -singleCompThread -nodisplay -nosplash``, the GUI and the background java processes are
suppressed as is the creation of multiple threads. 

To run the MATLAB script, simply submit the job to the scheduler with the following command:

.. code-block:: bash

    sbatch job.slurm

.. note::
    Matlab GUI can be launched from the ``Interactive Apps`` section of our HPC Web Interface,
    https://ood.hpc.abuhdabi.nyu.edu (VPN Required). More info on the HPC Web Interface can be found :doc:`here </hpc/ood/index>`.
    It is recommended you use the GUI for testing/debugging purposes. For the actual/production runs, command line/batch mode is 
    recommended as it reduces the overhead created by processes/java threads in the background.


Running a Multi-threaded MATLAB Job with the Parallel Computing Toolbox
-----------------------------------------------------------------------

Most of the time, running MATLAB in single-threaded mode (as described above) will meet your needs. 
However, if your code makes use of the Parallel Computing Toolbox (e.g., ``parfor``) or you have intense 
computations that can benefit from the built-in multi-threading provided by MATLAB's BLAS implementation, 
then you can run in multi-threaded mode. One can use up to all the CPU-cores on a single node in this mode. 
Multi-node jobs are not possible with the version of MATLAB that we have so your Slurm script should always 
use ``#SBATCH --nodes=1``. Here is an example from MathWorks of using multiple cores (``for_loop.m``):

.. code-block:: matlab

    poolobj = parpool;
    fprintf('Number of workers: %g\n', poolobj.NumWorkers);

    tic
    n = 200;
    A = 500;
    a = zeros(n);
    parfor i = 1:n
        a(i) = max(abs(eig(rand(A))));
    end
    toc

The Slurm script (``job.slurm``) below can be used for this case:

.. code-block:: bash

    #!/bin/bash
    #SBATCH --job-name=parfor        # create a short name for your job
    #SBATCH --nodes=1                # node count
    #SBATCH --n=1               # total number of tasks across all nodes
    #SBATCH --cpus-per-task=4        # cpu-cores per task (>1 if multi-threaded tasks)
    #SBATCH --time=00:00:30          # total run time limit (HH:MM:SS)
    #SBATCH --mail-type=all          # send email on job start, end and fault
    #SBATCH --mail-user=<YourNetID>@nyu.edu

    #Load Matlab
    module purge
    module load matlab

    #Run the matlab script
    matlab -nojvm -nodisplay -nosplash -nodesktop -batch for_loop

Note that ``-singleCompThread`` does not appear in the Slurm script in contrast to the serial case. 
One must tune the value of ``--cpus-per-task`` for optimum performance. 
Use the smallest value that gives you a significant performance boost because the more resources you 
request the longer your queue time will be.

Overriding the 12 core limit
----------------------------

By default MATLAB will restrict you to 12 worker threads. You can override this when making the parallel 
pool with the following line, for example, with 24 threads:

.. code-block:: matlab

    poolobj = parpool('local', 24);

If you use more than one thread then make sure that your code can take advantage of all the CPU-cores. 
The amount of time that a job waits in the queue is proportional to the requested resources. 
Furthermore, your fairshare value is decreased in proportion to the requested resources. 

.. tip::
    More the number of matlab workers, more are the chances of overhead and hence reduced speedup.
    If you have a matlab code with independent computations, then 
    :doc:`Job arrays </hpc/jobs/job_array>` and :doc:`Parallel Job Array </hpc/jobs/parallel_job_array>`  
    are one of the most easiest and efficient ways of parallelizing 
    your computations. Follow the corresponding highlighted links for a much more detailed example.
    You can also contact us if you need any help with this.


How Do I Know If My MATLAB Code is Parallelized?
------------------------------------------------

A ``parfor`` statement is a clear indication of a parallelized MATLAB code. However, 
there are cases when the parallelization is not obvious. One example would be a code that uses 
linear algebra operations such as matrix multiplication. In this case MATLAB will use the BLAS library 
which offers multithreaded routines.

There are two common ways to deteremine whether or not a MATLAB code can take advantage of parallelism 
without knowing anything about the code. The first to is run the code using 1 CPU-core and then do a 
second run using, say, 4 CPU-cores. Look to see if there is a significant difference in the execution 
time of the two codes. The second method is to launch the job using, say, 4 CPU-cores then ssh to the 
compute node where the job is running and use htop -u $USER to inspect the CPU usage. To get the name of the compute node where your job is running use the following command:

.. code-block:: bash

    squeue

The rightmost column labeled ``NODELIST(REASON)`` gives the name of the node where your job is running. 
SSH to this node, for example:

.. code-block:: bash

    ssh dn034

Once on the compute node, run the following command:

.. code-block:: bash

    htop -u $USER
     
If your job is running in parallel you should see a process using much more than ``100%`` in the ``%CPU`` 
column. For 4 CPU-cores this number would ideally be ``400%``

Running Matlab on GPUs
----------------------

Many routines in MATLAB have been written to run on a GPU. Below is a MATLAB script (svd_matlab.m) that 
performs a matrix decomposition using a GPU:

.. code-block:: matlab

    gpu = gpuDevice();
    fprintf('Using a %s GPU.\n', gpu.Name);
    disp(gpuDevice);

    X = gpuArray([1 0 2; -1 5 0; 0 3 -9]);
    whos X;
    [U,S,V] = svd(X)
    fprintf('trace(S): %f\n', trace(S))
    quit;

The Slurm script (``job.slurm``) below can be used for this case:

.. code-block:: bash

    #!/bin/bash
    #SBATCH --job-name=matlab-svd    # create a short name for your job
    #SBATCH --nodes=1                # node count
    #SBATCH --ntasks=1               # total number of tasks across all nodes
    #SBATCH --cpus-per-task=1        # cpu-cores per task (>1 if multi-threaded tasks)
    #SBATCH --time=00:01:00          # total run time limit (HH:MM:SS)
    #SBATCH -p nvidia                # Request nvidia partition for GPU nodes
    #SBATCH --gres=gpu:1             # number of gpus per node
    #SBATCH --mail-type=begin        # send email when job begins
    #SBATCH --mail-type=end          # send email when job ends
    #SBATCH --mail-user=<NetID>@nyu.edu

    #Load Matlab Module
    module purge
    module load matlab

    #Run your matlab script
    matlab -nojvm -singleCompThread -nodisplay -nosplash -nodesktop -batch svd_matlab

In the above Slurm script, notice the new lines: ``#SBATCH -p nvidia`` and ``#SBATCH --gres=gpu:1``

The job can be submitted to the scheduler with:

.. code-block:: bash

    sbatch job.slurm

Be sure that your MATLAB code is able to use a GPU before submitting your job. 
See this `Getting started guide on MATLAB and GPUs <https://www.mathworks.com/solutions/gpu-computing/getting-started.html>`__.



