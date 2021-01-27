How to use MATLAB Parallel Toolbox
==================================

One of the features users may want to use in Dalma is Matlab's Parallel Toolbox.  

MATLAB Parallel Toolbox allows you to run parallel computations in multicore systems. For computer cluster and grid support you would need to use the MATLAB Distributed Computing Server which is not currently supported at NYUAD.
Parallel computations can be achieved either using  **parallel for-loops** , **special array types** or **parallelized numerical algorithms**. You can also submit **batch local workers**, for more info visit the MATLAB documentation ( http://www.mathworks.es/es/help/distcomp/introduction-to-parallel-solutions.html#brjw1fx-2 )

In any case, for all these things to work, you will need to define a set of resources (cpus or workers) where the tasks will be executed.  The easiest way is to use the matlabpool command. This command has been replaced in recent versions for parpool. Again, refer to the MATLAB documentation for details. 

Step-by-step guide
------------------

If you are planning to run parallel computation with Matlab:

1. the maximum allowed number of workers by MATLAB in a node is 12. Use this in your submission script

    .. code-block:: bash

        #SBATCH -n 1
        #SBATCH --cpus-per-task=12

2. Open the matlabpool / parpool
3. Do the computation
4. Close the matlabpool / parpool

**Example:** Suppose we have the following matlab code file named: ``parfortest.m``
 

.. code-block:: matlab
   :linenos:
   :emphasize-lines: 5,6,13

    P=8;
    N=10000;
    n=100;
    x = zeros(N,n);
    parpool ('open',P);
    parfor i = 1:N
        y = zeros(1,n);
        for j = 1:n
            y(j) = rand;
        end
        x(i,:) = y;
    end
    parpool close;
 

Running the example using an interactive session
------------------------------------------------

You can now open an interactive session to run it. To open an interactive shell in the cluster, type the following:

 

 
.. code-block:: bash
    
    [login-node]$> srun --pty  -n 1 --cpus-per-task=12  /bin/bash
 

Once you are in the interactive shell you must load the matlab module like:

.. code-block:: bash

    [compute-node]$> module load matlab 

And finally open matlab and run the example as you would do it in your workstation/laptop. Notice that running Matlab in the interactive queue you will not have GUI available.

Running the example using the batch system
------------------------------------------

First thing you need a submission script like this: ``run.slurm``

.. code-block:: bash

    #!/bin/bash
    #SBATCH -n 1
    #SBATCH --cpus-per-task=12
    #SBATCH -J matlab_test
    #SBATCH -o matlab.%J.out
    #SBATCH -e matlab.%J.err
    
    module purge
    module load matlab
    
    # to run an m file do the following
    matlab -nosplah -nodisplay -nodesktop < parfortest.m > parfortest_output.out
    
    # If you are running a matlab function do the following:
    # matlab -nosplash -nodisplay -nodesktop -r "myCode(arg,...);exit;"
 

Then you can submit the job as usual.