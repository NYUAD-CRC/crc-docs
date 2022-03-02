Difference in Job Submission between Jubail and Dalma
=====================================================

This section highlights some of the important chnages you would need in your job submission scripts when moving from Dalma HPC to Jubail HPC. 

We shall discuss each of the sections below:

1. Partitions
2. Number of Tasks
3. Memory
4. Bigmem nodes
5. GPU nodes
6. Timelimit 
7. Preempt jobs

Summary
-------
.. list-table:: 
    :widths: auto 
    :header-rows: 1

    * - 
      - **Dalma**
      - **Jubail**
    * - **Partitions**
      - 
      - 
    * - 
      - Dalma had ``serial`` and ``parallel`` partitions 
      - No ``serial`` and ``parallel`` partitions on Jubail 
    * - 
      - 	
      - Only one generalized partition called ``compute``
    * - 
      - 
      - More info can be found :doc:`here </hpc/jobs/quick_start>` 
    * - 
      - 
      - Dalma based job scipts with ``-p parallel`` and ``-p serial`` specified will work on 
        Jubail and these lines will be filtered out automatically by the job scheduling wrapper.
    * -
      -
      - ``SBATCH -p compute`` is optional(as compute is the default partition)
    * -
      -
        .. code-block:: bash

          #SBATCH -p parallel

      -   
        .. code-block:: bash

          #SBATCH -p compute 

    * - **Maximum number of Tasks/CPUs**
      - 
      -  
    * -
      - Maximum number of CPUs per node was 28 in Dalma. 
      - Maximum number of CPUs per node is 128 on Jubail.
    * -
      - 
      - Small jobs (requiring less than 28 CPUs) will be sent to old Dalma nodes by the scheduler.
    * - 
      - 
      - Medium and Large jobs will be prioritized and sent to Jubail.
    * -
      -
      - Small jobs (less than 28 CPUs),mostly belonging to python and R, don't need any change and will be suported on jubail as well.
    * - 
      -
      - Medium and Large jobs (MPI Jobs) would need an adjustment as the ``-n`` or ``--ntasks`` parameter would need to be 
        a multiple of 128 if it was a multiple of 28 on Dalma.
    * -
      - Requesting 280 CPUs(``28x10``) requires 10 nodes (parallel job).

        .. code-block:: bash

          #SBATCH -p parallel
          #SBATCH -n 280  

      - Requesting the nearest multiple of 128 cores as compared to what was requested on Dalma, 256 CPUs (``128x2``) requires only 2 nodes.

        .. code-block:: bash

          #SBATCH -p compute
          #SBATCH -n 256 

    * - **Memory**
      -
      -
    * -
      - Total Memory per node was 112GB on Dalma
      - Total Memory per node is 480GB on Jubail
    * -
      - Default memory assigned for a job was 4GB per CPU.
      - Default memory assigned for a job is 3.75GB per CPU.
    * -
      - Max allowed memory per node was 112GB.
      - Max allowed memory per node is 480GB.
    * -
      - 
        .. code-block:: bash
          
          #SBATCH -p parallel
          #SBATCH --mem=80G

      - 
        .. code-block:: bash

          #SBATCH -p compute
          #SBATCH --mem=200G

    * - **BigMem nodes**
      -
      -
    * -
      - Large memory nodes were requested using the ``bigmem`` partition for memory greater than 112GB.
      - Large memory nodes are requested using the ``bigmem`` partition for memory greater than 480GB. 
    * -
      - Dalma has three large memory nodes.
      - Jubail has four large memory nodes.
    * - 
      - ``#SBATCH -p bigmem`` was optional
      - ``#SBATCH -p bigmem`` is mandatory
    * -
      - Large mem nodes were requested when required memory was greater than 112GB

        .. code-block:: bash

          #SBATCH -p bigmem
          #SBATCH --mem=200G

      - Large mem nodes are requested ONLY when required memory is greater than 480GB

        .. code-block:: bash

          #SBATCH -p bigmem  
          #SBATCH --mem=700G

    * - **GPU nodes**
      -
      -
    * -
      - Dalma had 14 GPU nodes with 2 Nvidia ``V100`` GPU cards on 12 nodes and 8 ``V100`` GPU vards on 2 nodes.
      - On addition to the Dalma GPU nodes, Jubail has 24 GPU nodes with one ``A100`` card on each of them.
    * -
      - Dalma had exclusive GPU nodes. Hence, only GPU jobs were running on GPU nodes.
      - Jubail has both exclusive (``V100`` GPU nodes (Dalma GPU nodes) ) and non-exclusive (versatile, ``A100`` GPU nodes) which can run normal CPU jobs when idle (no GPU cards are needed) and have a higher priority for GPU jobs.
    * -
      - Only Nvidia ``V100`` cards were available on Dalma.
      - On Jubail, Users have an option to choose between Nvidia ``V100`` and and the new ``A100`` cards.
    * -
      -
      - By Default, the GPU jobs will be sent to ``V100`` GPU nodes.
    * -
      -
      - The users can test the performance differences between the ``A100`` and ``V100`` nodes and decide accordingly.
    * -
      -
      - Since, ``A100`` GPU nodes are non exclusive, Users might have to wait in queue for non GPU jobs (normal CPU jobs) on those nodes to be available on a priority basis.
    * -
      -
      - You can also mention in your job script if you would like to explicitly send your job to a100 nodes.
    * -
      - When requesting a single GPU

        .. code-block:: bash

          #SBATCH -p nvidia
          #SBATCH --gres=gpu:1

      - The syntax on Jubail for requesting a single GPU is same as Dalma

        .. code-block:: bash

          #SBATCH -p nvidia
          #SBATCH --gres=gpu:1
    * -
      -
      - When requesting a single GPU on new ``A100`` nodes

        .. code-block:: bash

          #SBATCH -p nvidia
          #SBATCH --gres=gpu:a100:1

    * - **WallTime**
      -
      -
    * - 
      - Max WallTime on Dalma was linked to the account they belong to (physics,students,engineering etc)
      - Max Wall time on Jubail is linked to the type (size) of job submitted by the user irrespective of the account they belong to.
    * -
      -
      - The details of the types of Jobs and their respective limits can be found in the link :ref:`here <partitions_summary>`
    * - **Preempt partition**
      - 
      -
    * - 
      - Partition used for quick testing with high job priority available for everyone.
      -      
    * -
      - Max Walltime for preempt jobs was 30 minutes on Dalma
      - Max Walltime for preempt jobs on Jubail depends on size
        
        * cpus < 28 : 24 hours
        * cpus > 28 : 12 hours  
    * -
      -
      - More info on this can be found :ref:`here <preempt_partition>`

        
        




      

