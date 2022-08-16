A Detailed SLURM Guide
======================

SLURM: Partitions
-----------------

A partition is a collection of nodes, they may share some attributes (CPU type, GPU, etc)

* Compute nodes may belong to multiple partitions to ensure maximum use of the system
* Partitions may have different priorities and limits of execution and may limit who can use them
* Jubail's partition (as seen by users)

	- ``compute``: General purpose partition for all the normal runs
	- ``nvidia`` : Partition of GPU jobs
	- ``bigmem`` : Partition for large memory jobs. Only jobs requesting more than 500GB will fall into this category.
	- ``prempt`` : Supports all types of jobs with a grace period of 30 minutes. More on this :ref:`here <preempt_partition>`
	- ``xxl``    : Special partition for grand challenge applications. Requires approval from management.
	- ``visual`` : We have a few nodes which give you the liberty of running applications with GUI.
* There are other partitions, but these are reserved for specific groups and research projects
* For those who are experts in SLURM we use partitions to request GPUs, large memory, and visual instead of "constraints" as this approach gives us more flexibility for priorities and resource limits.

SLURM: Submitting Jobs
----------------------

1. To submit a job first you write a "job script"

    .. code-block:: bash

        #!/bin/bash
        #SBATCH -n 1
        ./myprogram
2. Then you submit the script in any of the following manner

    .. code-block:: bash

        $> sbatch job.sh
        #OR
        $> sbatch < job.sh
        #OR
        $> sbatch << EOF
        #!/bin/bash
        #SBATCH -n 1
        ./myprogram
        EOF

SLURM: Arguments
----------------

* Arguments to ``sbatch`` can be put on the command line or embedded in the job script
* Putting them in the job script is a better option as then it "documents" how to rerun your job

.. code-block:: bash

    #!/bin/bash
    #SBATCH -n 1
    ./myprogram

.. code-block:: bash

    $> sbatch job1.sh

OR

.. code-block:: bash

    #!/bin/bash
    ./myprogram

.. code-block:: bash    

    $> sbatch -p preempt -n 1 job2.sh


**Common Job submission arguments:**

* ``-n``   Select number of tasks to run (default 1 core per task)
* ``-N``   Select number of nodes on which to run
* ``-t``   Wallclock in days-hours:minutes:seconds (ex 4:00:00)
* ``-p``   Select partition (compute, gpu, bigmem)
* ``-o``   Output file ( with no –e option, err and out are merged to the Outfile)
* ``-e``   Keep a separate error File
* ``-d``   Dependency with prior job (ex don't start this job before job XXX terminates)
* ``-A``   Select account (ex physics_ser, faculty_ser)
* ``-c``   Number of cores required per task (default 1)
* ``--ntasks-per-node`` Number of tasks on each node
* ``--mail-type=type`` Notify on state change: BEGIN, END, FAIL or ALL
* ``--mail-user=user`` Who to send email notification
* ``--mem`` Maximum amount of memory per job (default is in MB, but can use GB suffix) (Note: not all memory is available to jobs, 8GB is reserved on each node for the OS) (So a 128GB node can allocate up to 120GB for jobs)


SLURM: Job Dependencies
-----------------------

Submitting with dependencies: Useful to create workflows.

Any specific job may have to wait until any of the specified conditions are met, these conditions are set with **--depend=type:jobid** where type can be:

    * ``after``         run after <jobid> has terminated
    * ``afterany``      if <jobid> is a job array run after any job in the job array has terminated
    * ``afterok``       run after <jobid> if it finished successfully
    * ``afternotok``    run after <jobid> if it failed to finish successfully

.. code-block:: bash

    #Wait for specific job array elements	
    sbatch --depend=after:123_4 my.job
    sbatch --depend=afterok:123_4:123_8 my.job2	
    #Wait for any job array element to complete	
    sbatch --depend=afterany:123 my.job
    #Wait for entire job array to complete successfully	
    sbatch --depend=afterok:123 my.job
    #Wait for entire job array to complete and at least one task fails	
    sbatch --depend=afternotok:123 my.job

SLURM: Listing Jobs
-------------------

Each submitted job is given a unique number

* You can list your jobs to see which ones are waiting (pending) or running
* As well as how long a job has been running and on which node(s)

.. code-block:: bash

    $> squeue
    JOBID           PARTITION   NAME     USER    ST  TIME    NODES   NODELIST(REASON)
    435251_[1-50]   compute     151215_F wz22    PD  0:00      1        (Priority)
    435252_[1-50]   compute     151215_F wz22    PD  0:00      1        (Priority)
    435294          compute     Merge5.s wz22    PD  0:00      1        (Priority)
    435235_[20-50]  compute     151215_F wz22    PD  0:00      1        (Priority)
    435235_19       compute     151215_F wz22    R   12:55     1        cn028
    435235_17       compute     151215_F wz22    R   47:34     1        cn021
    435235_15       compute     151215_F wz22    R   49:04     1        cn027
    435235_13       compute     151215_F wz22    R   50:34     1        cn024
    435235_11       compute     151215_F wz22    R   54:35     1        cn029
    435235_9        compute     151215_F wz22    R   56:35     1        cn026
    435235_7        compute     151215_F wz22    R   58:35     1        cn025
    435235_5        compute     151215_F wz22    R   59:36     1        cn020
    435235_3        compute     151215_F wz22    R   1:00:36   1        cn011
    435235_1        compute     151215_F wz22    R   1:04:37   1        cn013
    
SLURM: Listing Jobs
-------------------

* You can look at completed jobs using the "sacct" command
* To look at jobs you ran since July 1, 2022

.. code-block:: bash

    $> sacct --starttime=2022-07-01


* You can retrieve the following informations about a job after it terminates:

.. code-block:: bash

    AllocCPUS       Account        AssocID          AveCPU
    AveCPUFreq      AveDiskRead    AveDiskWrite     AvePages
    AveRSS          AveVMSize      BlockID          Cluster
    Comment         ConsumedEnergy CPUTime          CPUTimeRAW
    DerivedExitCode Elapsed        Eligible         End
    ExitCode        GID            Group            JobID
    JobName         Layout         MaxDiskRead      MaxDiskReadNode
    MaxDiskReadTask MaxDiskWrite   MaxDiskWriteNode MaxDiskWriteTask
    MaxPages        MaxPagesNode   MaxPagesTask     MaxRSS
    MaxRSSNode      MaxRSSTask     MaxVMSize        MaxVMSizeNode
    MaxVMSizeTask   MinCPU         MinCPUNode       MinCPUTask
    NCPUS           NNodes         NodeList         NTasks
    Priority        Partition      QOSRAW           ReqCPUFreq
    ReqCPUs         ReqMem         Reserved         ResvCPU
    ResvCPURAW      Start          State            Submit
    Suspended       SystemCPU      Timelimit        TotalCPU
    UID             User           UserCPU          WCKey


* To retrieve specific informations about a job

.. code-block:: bash

    $> sacct -j 511512 -format=partition,alloccpus,elapsed,state,exitcode
     JobID         JobName    Partition   Account   AllocCPUS  State     ExitCode
     ------------ ---------- ---------- ---------- ---------- ---------- --------
     511512        sub.sh     nvidia     avengers     20      COMPLETED    0:0
     511512.batch  batch                 avengers     20      COMPLETED    0:0
     511512.0      env                   avengers     20      COMPLETED    0:0


SLURM: Job Progress
-------------------

* You can see your job's progress by looking at the output and error files
* By default output and error files are named "slurm-XXX.out" and "slurm-XXX.err" where XXX is the job id
* "tail –f" allows you to track new output as it is produced

.. code-block:: bash

    $> cat slurm-435563.out
    $> more slurm-435563.out
    $> tail –f slurm-435563.out

SLURM: Killing Jobs
-------------------

* Sometimes you need to kill your job when you realise it is not working as expected
* Note that your job can be killed automatically when it reaches its maximum time/memory allocation
    
.. code-block:: bash

    $> scancel 435563

SLURM: Tasks
------------

In SLURM users specify how many tasks (not cores!) they need using (**-n**), each task by default
uses 1 core but this can be redefined by users using the (**-c**) option.

For example ``#SBATCH -n 2`` is requesting 2 cores, while ``#SBATCH -c 3`` ``#SBATCH -n 2`` is
requesting 6 cores.

When submitting parallel jobs on Jubail you need not specify the number of nodes. The
number of tasks and cpus-per-task is sufficient for SLURM to determine how many nodes to
reserve.

SLURM: Node List
----------------

Sometimes applications require a list of nodes where they are to run in parallel to start.
SLURM keeps the list of nodes within the environment variable ``$SLURM_JOB_NODELIST``.

SLURM: Accounts
---------------

SLURM maintains user associations which include user, account, qos, and partition.

Users may have several associations, also accounts are hierarchical. For example, account "physics" maybe be a sub-account of "faculty", which may be a sub-account of "institute", etc.

When submitting jobs, users with multiple associations must explicitely list the account, qos,partition and all details they wish to use.

.. code-block:: bash

    sbatch -p preempt -A physics job

Jubail specific job submission tools extend SLURM's associations to define a ``default`` association, so you only need to specify which account is, for example you belong to multiple
accounts (faculty) and (research-lab) and you want to execute using your non-default
account. So at most you'll need to specify:

.. code-block:: bash

    sbatch -p <partition> -A <account> job

Moreover, accounts, partitions, qos and users may each be configured with resource usage
limits. Thus the administrators can impose limits to the number of jobs queued, jobs running,
cores usage, and run time.

