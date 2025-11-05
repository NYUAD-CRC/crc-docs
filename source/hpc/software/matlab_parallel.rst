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
    #SBATCH --time=00:05:00          # total run time limit (HH:MM:SS)
    #SBATCH --mail-type=all          # send email on job start, end and fault
    #SBATCH --mail-user=<YourNetID>@nyu.edu

    #Load matlab module
    module purge
    module load matlab

    #Run Matlab via command line
    matlab -nojvm -singleCompThread -batch hello_world
    #Wait for a minute
    sleep 60

By invoking MATLAB with ``-nojvm -singleCompThread -batch``, the GUI and the background java processes are
suppressed as is the creation of multiple threads. 

To run the MATLAB script, simply submit the job to the scheduler with the following command:

.. code-block:: bash

    sbatch job.slurm

.. note::
    Matlab GUI can be launched from the ``Interactive Apps`` section of our HPC Web Interface,
    https://ood.hpc.abudhabi.nyu.edu (VPN Required). More info on the HPC Web Interface can be found :doc:`here </hpc/ood/index>`.
    It is recommended you use the GUI for testing/debugging purposes. For the actual/production runs, command line/batch mode is 
    recommended as it reduces the overhead created by processes/java threads in the background.


Running a Multi-threaded MATLAB Job 
------------------------------------

Most of the time, running MATLAB in single-threaded mode (as described above) will meet your needs. 
However, if your code makes use of the Parallel Computing Toolbox (e.g., ``parfor`` and ``spmd``) or you have intense 
computations that can benefit from the built-in multi-threading provided by MATLAB's BLAS implementation, 
then you can run in multi-threaded mode.

MATLAB Parallel Toolbox allows you to run parallel computations in multicore systems, parallel computations can be achieved either using  `parallel for-loops <https://www.mathworks.com/help/matlab/ref/parfor.html>`__ or
`GPU computing <https://www.mathworks.com/solutions/gpu-computing.html>`__ , for more info visit 
the MATLAB documentation (`Get Started with Parallel Computing Toolbox <https://es.mathworks.com/help/parallel-computing/getting-started-with-parallel-computing-toolbox.html#brjw1fx-2>`__ )

For computer cluster and grid support you would need to use the MATLAB Distributed Computing Server which is not currently supported at NYUAD. 

In any case, for all these things to work you will need to define a set of resources (cpus or workers) where the tasks will be executed, the easiest way is to use the ``matlabpool`` command this command has been replaced in recent versions with ``parpool``, again refer to the MATLAB documentation for details.  

One can use up to all the CPU-cores on a single node in this mode. 
Multi-node jobs are not possible with the current setup of MATLAB, so your Slurm script should always 
use ``#SBATCH --nodes=1``. Here is an example of using multiple cores (``hello_world_threaded.m``):

.. code-block:: matlab
 
    % Create the parallel pool,
    poolobj = parpool;
    fprintf("Number of workers: %g\n", poolobj.NumWorkers);
    
    tic;
    % Single Program Multiple Data
    spmd
        fprintf("Hello World from Jubail's worker %d!\n", spmdIndex)
    end
    fprintf("Elapsed time: %g seconds\n", toc);
    
    % Close the parallel pool
    delete(poolobj);

The Slurm script (``job.slurm``) below can be used for this case:

.. code-block:: bash

    #!/bin/bash
    #SBATCH --job-name=matlab_threaded              # create a short name for your job
    #SBATCH --nodes=1                               # node count
    #SBATCH --ntasks=1                              # total number of tasks across all nodes
    #SBATCH --cpus-per-task=4                       # cpu-cores per task (>1 if multi-threaded tasks)
    #SBATCH --time=00:05:00                         # total run time limit (HH:MM:SS)
    #SBATCH --mail-type=all                         # send email on job start, end and fault
    #SBATCH --mail-user=<YourNetID>@nyu.edu

    #Load Matlab
    module purge
    module load matlab

    #Run the matlab script
    matlab -batch hello_world_threaded


The job can be submitted to the scheduler with:

.. code-block:: bash

    sbatch job.slurm

Note that ``-singleCompThread`` and ``-nojvm`` does not appear in the Slurm script in contrast to the serial case. 

One must tune the value of ``--cpus-per-task`` for optimum performance, use the smallest value for ``--cpus-per-task`` that gives you a significant performance boost because the more resources you 
request the longer your queue time will be. Furthermore, your fairshare value is decreased in proportion to the requested resources. 

.. note::
	Number of matlab workers by default will be the multiplication of ``--ntasks`` and ``--cpus-per-task``.

.. tip::
    More the number of matlab workers, more are the chances of overhead and hence reduced speedup.
    If you have a matlab code with independent computations, then 
    :doc:`Job arrays </hpc/jobs/job_array>` and :doc:`Parallel Job Array </hpc/jobs/parallel_job_array>`  
    are one of the most easiest and efficient ways of parallelizing 
    your computations. Follow the corresponding highlighted links for a much more detailed example.
    You can also contact us if you need any further help with this.

Running MATLAB on GPUs
----------------------

Many routines in MATLAB have been written to run on a GPU. Below is a MATLAB script (``matlab_gpu.m``) that prints out information about the GPU device:

.. code-block:: matlab

    gpu = gpuDevice();
    disp(gpu);
    reset(gpu);

The Slurm script (``job.slurm``) below can be used for this case:

.. code-block:: bash

    #!/bin/bash
    #SBATCH --job-name=matlab_gpu    # create a short name for your job
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
    matlab -nojvm -singleCompThread -batch matlab_gpu

In the above Slurm script, notice the new lines: ``#SBATCH -p nvidia`` and ``#SBATCH --gres=gpu:1``

The job can be submitted to the scheduler with:

.. code-block:: bash

    sbatch job.slurm

Be sure that your MATLAB code is able to use a GPU before submitting your job. 
See this `Getting started guide on MATLAB and GPUs <https://www.mathworks.com/solutions/gpu-computing/getting-started.html>`__.


Estimate the Value of Pi Using Different Resources
----------------------------------------------------
Here is an example MATLAB code that estimates the value of Pi using Monte Carlo method. This code can be run in serial, multi-threaded or on a GPU. 

Serial Example:

.. code-block:: matlab

    function piEst = computePi(m,n)
    pointsInCircle = 0;

    for i = 1:n
        % Generate random points.
        x = rand(m,1);
        y = rand(m,1);

        % Determine whether the points lie inside the unit circle.
        r = x.^2 + y.^2;
        pointsInCircle = pointsInCircle + sum(r<=1);
    end

    piEst = 4/(m*n) * pointsInCircle;
    end

    % Estimate pi in serial
    m  = 3e5;
    n  = 2e3;

    tic;
    fprintf('piEst = %.6f\n', computePi(m,n));
    fprintf("Elapsed time: %g seconds\n", toc);

Using ``parfor`` for Multi-threaded Example:

.. code-block:: matlab

    function piEst = computePiParfor(m,n)
    pointsInCircle = 0;

    parfor i = 1:n
        % Generate random points.
        x = rand(m,1);
        y = rand(m,1);

        % Determine whether the points lie inside the unit circle.
        r = x.^2 + y.^2;
        pointsInCircle = pointsInCircle + sum(r<=1);
    end

    piEst = 4/(m*n) * pointsInCircle;
    end

    % Estimate pi on multiple threads
    m  = 3e5;
    n  = 2e3;

    % Start a thread-based parallel pool

    parpool('Threads');

    tic;
    fprintf('piEst = %.6f\n', computePiParfor(m,n));
    fprintf("Elapsed time: %g seconds\n", toc);

    % Shut down the parallel pool
    delete(gcp('nocreate'));

GPU Example:

.. code-block:: matlab

    function piEst = computePiGPU(m,n)
    c = zeros(1,"gpuArray");

    for i = 1:n
        % Generate random points on the GPU.
        x = rand(m,1,"gpuArray");
        y = rand(m,1,"gpuArray");

        % Determine whether the points lie inside the unit circle.
        r = x.^2 + y.^2;
        c = c + sum(r<=1);
    end

    piEst = 4/(m*n) * c;
    end

    % Estimate pi using GPU computation
    m  = 3e5;
    n  = 2e3;

    tic;
    fprintf('piEst = %.6f\n', computePiGPU(m,n));
    fprintf("Elapsed time: %g seconds\n", toc);


Each of the above codes can be run using the appropriate Slurm script as described in the previous sections.

How Do I Know If My MATLAB Code is Parallelized?
------------------------------------------------

A ``parfor`` statement is a clear indication of a parallelized MATLAB code. However, 
there are cases when the parallelization is not obvious. One example would be a code that uses 
linear algebra operations such as matrix multiplication. In this case MATLAB will use the BLAS library 
which offers multithreaded routines.

There are two common ways to deteremine whether or not a MATLAB code can take advantage of parallelism 
without knowing anything about the code. 


The first to is run the code using 1 CPU-core and then do a second run using, say, 4 CPU-cores. Look to see if there is a significant difference in the execution 
time of the two codes. 


The second method is to launch the job using, say, 4 CPU-cores then ssh to the compute node where the job is running and use htop -u $USER to inspect the CPU usage. To get the name of the compute node where your job is running use the following command:

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


Installing MATLAB Toolbox
--------------------------
To install additional MATLAB toolboxes on Jubail, please follow the instructions below:

1. Download the required MATLAB toolbox from the MathWorks website. Ensure you have the necessary permissions or license to download the toolbox.

2. Transfer the downloaded toolbox files to your scratch directory using a secure copy method (e.g., SCP or SFTP).

3. Once the files are on Jubail, unzip the toolbox and run the startup file from MATLAB.

If you need further assistance with a specific MATLAB toolbox that is not currently installed on Jubail, please contact the HPC team at jubail.support@nyu.edu