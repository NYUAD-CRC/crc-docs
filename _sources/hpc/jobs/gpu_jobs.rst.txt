Analyzing GPU Jobs
==================

When running GPU-accelerated jobs on a High-Performance Computing (HPC) system, 
it is essential to monitor the utilization and performance of the GPUs to ensure efficient 
resource utilization and troubleshoot any potential issues. This documentation provides 
instructions on monitoring GPU jobs using the system inbuilt ``gutil`` command which uses ``nvidia-smi`` 
command within, allowing users to track the GPU status in real-time.

This guide will walk you through the process of analyzing GPU jobs using the ``gutil`` 
after obtaining the ``jobid`` from the ``squeue`` output.

.. important::
    Note that jobs with low GPU utilization (``< 10%``) may be terminated 
    by the system in order to free up resources for other users on the cluster. 

Finding the Job ID
---------------------
Before monitoring the GPU job, you need to find the `jobid`. You can use the `squeue` command to obtain 
a list of running jobs and their corresponding job IDs. The output of the ``squeue`` command will display 
the job ID of your running job .

The output will look something like this

.. code-block:: console

    (3-4.11.0)[wz22@login1 ~]$ squeue
             JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
           1457246    nvidia     run     wz22  R    3:35:44      1 cn001

Here, the JobID is ``1457246``.


Monitoring GPU Usage
--------------------

The ``gutil <jobid>`` command allows you to monitor the GPU usage in real-time. The command refreshes the 
output at regular intervals, making it 
easy to track changes over time. The jobid of the desired job is passed as an argument to the ``gutil`` command
as shown below:

.. code-block:: console

    (3-4.11.0)[wz22@login1 ~]$ #gutil <jobid>
    (3-4.11.0)[wz22@login1 ~]$ gutil 1457246

This command will display a continuous stream of output showing the current GPU usage. 
The output includes information such as the GPU temperature, memory usage, and process 
IDs of any running jobs.

A sample output is shown below

.. code-block:: console

    Every 2.0s: nvidia-smi                                                                              cn001: Mon May  1 22:04:18 2023

    Mon May  1 22:04:18 2023
    +-----------------------------------------------------------------------------+
    | NVIDIA-SMI 460.106.00   Driver Version: 460.106.00   CUDA Version: 11.2     |
    |-------------------------------+----------------------+----------------------+
    | GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
    | Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
    |                               |                      |               MIG M. |
    |===============================+======================+======================|
    |   0  A100-PCIE-40GB      Off  | 00000000:81:00.0 Off |                    0 |
    | N/A   32C    P0    64W / 250W |  14298MiB / 40536MiB |     78%      Default |
    |                               |                      |             Disabled |
    +-------------------------------+----------------------+----------------------+

    +-----------------------------------------------------------------------------+
    | Processes:                                                                  |
    |  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
    |        ID   ID                                                   Usage      |
    |=============================================================================|
    |    1   N/A  N/A   1146446      C   python                          14295MiB |
    +-----------------------------------------------------------------------------+

In this example output, we have one NVIDIA A100 GPU with the following information:

- **Memory usage**: The Memory-Usage column shows how much memory is the GPU currently using, in MiB. 
  For example, the GPU above is using 14298MiB of its available 40536MiB.

- **GPU utilization**: The GPU-Util column shows the current GPU utilization for the GPU, 
  as a percentage. For example, the GPU above has a utilization of 78%, indicating that it is 
  being used heavily by an application.

.. list-table:: 
    :widths: auto 
    :header-rows: 1

    * - Memory Usage
      - GPU Utilization
      - Remarks
    * - High 
      - High
      - Your job is running perfectly fine and utilizating the GPU to its full capacity.  
    * - Low
      - High
      - Your job is running fine and utilizing the GPU. Increasing the batch size in a few cases can speed up even more.	
    * - High
      - Low ( ``< 10%``)
      - Not a favourable outcome. Even though the data is residing on the GPU, the computation/utilization is low and hence can be counter productive. 
    * - Low
      - Low (``< 10%``)
      - Not a favourable outcome. 

To exit the ``gutil`` command, press ``Ctrl-C``.


Interactive sessions
--------------------

Users can also make use of interactive sessions to debug their GPU jobs in an incremental fashion, 
if they are not working as expected.

This can be done as follows:

1. Get interactive access of a GPU node as follows:
   
   .. code-block:: console

    salloc -p nvidia --gres=gpu:1 -c 5 

  
 This will give you the interactive access on one of the GPU nodes.
 A sample output is shown below:

  .. code-block:: console

    (3-4.11.0)[wz22@login4 ~]$ salloc -p nvidia --gres=gpu:1 -c 5
    salloc: Granted job allocation 1606651
    salloc: Waiting for resource configuration
    salloc: Nodes cn005 are ready for job

    Disk quotas for wz22 (uid 3387153):
                                DISK SPACE                # FILES (1000's)
              filesystem       size      quota            number      quota
                          --------------------------   --------------------------
                  /home       17GB       29GB ( 60%)       105       150 ( 70%)
                /scratch     1047GB     5000GB ( 21%)       750      2048 ( 37%)
                /archive        0KB     5120GB (  0%)         0       125 (  0%)

    (3-4.11.0)[wz22@login4 ~]$

 It can be seen that node ``cn005`` has been assigned for the job. To exit from the interactive session, enter ``exit`` or press ``Ctrl+d``.

2. Open a new terminal in parallel and follow the above sections to track the GPU utilization as you work on. 

.. caution::
  It is strongly recommended to use the interactive mode for debugging purposes only.
