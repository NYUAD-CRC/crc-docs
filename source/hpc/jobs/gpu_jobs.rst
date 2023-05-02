Analyzing GPU Jobs
==================

When running jobs on a High-Performance Computing (HPC) cluster that use Graphics Processing 
Units (GPUs), it is essential to monitor the GPU usage to optimize performance and ensure 
efficient resource allocation. The ``watch nvidia-smi`` command is a useful tool for monitoring 
GPU usage in real-time.

This guide will walk you through the process of analyzing GPU jobs using the ``watch nvidia-smi`` 
command after accessing the node using the ``ssh`` command obtained from the ``squeue`` output.

.. important::
    Note that jobs with low GPU utilization (``< 10%``) may be terminated 
    by the system in order to free up resources for other users on the cluster. 

Logging into the node
---------------------

Before you can analyze your GPU jobs using the ``watch nvidia-smi`` command, you must first 
log in to the node where your job is running. You can obtain the necessary login credentials 
using the ``squeue`` command. The output of the ``squeue`` command will display the node name 
and job ID of your running job.


The output will look something like this


.. code-block:: console

    (3-4.11.0)[wz22@login1 ~]$ squeue
             JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
           1457246    nvidia     bash     wz22  R    3:35:44      1 cn001

Here, the job is running on ``cn001``. You can log in to the node using the ``ssh`` command:

.. code-block:: console

    (3-4.11.0)[wz22@login1 ~]$ ssh cn001

Once you have successfully logged in to the node, you can proceed with monitoring the GPU usage.
You can notice that that, after ``ssh`` the command prompt has changed from login node (``[wz22@login1 ~]$``)
to the GPU node (``[wz22@cn001 ~]$``)

.. code-block:: console

    (3-4.11.0)[wz22@login1 ~]$ ssh cn001
    Last login: Mon May  1 14:25:21 2023 from 10.10.0.201
    (3-4.11.0)[wz22@cn001 ~]$


Monitoring GPU Usage
--------------------

The ``watch nvidia-smi`` command allows you to monitor the GPU usage in real-time. The ``watch`` 
command refreshes the output at regular intervals (every two seconds by default), making it 
easy to track changes over time.

.. code-block:: console

    (3-4.11.0)[wz22@cn001 ~]$ watch nvidia-smi

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
    |   1  A100-PCIE-40GB      Off  | 00000000:81:00.0 Off |                    0 |
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

To exit the watch command, press ``Ctrl-C`` and then ``exit`` again from the GPU node.

.. code-block:: console

  (3-4.11.0)[wz22@cn001 ~]$ exit
  logout
  Connection to cn001 closed.
  (3-4.11.0)[wz22@login1 ~]$
