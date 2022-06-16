System
======

Overview
--------

The operating system on Jubail is Linux. Make sure you know the basics. Useful links:

* https://www.tutorialspoint.com/unix/index.htm
* http://linuxcommand.org/
* http://software-carpentry.org/lessons/
* https://www.edx.org/course/introduction-linux-linuxfoundationx-lfs101x-0


.. image:: ../img/system-1.png


Generic diagram of the cluster architecture and outside connectivity.

Hardware
--------

The new HPC cluster includes the integration of previous HPC cluster Dalma with Jubail HPC cluster.

The Jubail HPC consists of more than 28K cores.

* The CPU model is AMD EPYC 7742 64-Core Processor @2.25GHz,supporting AVX2.
* 480GB per node.
* 3.75 GB memory per core by default.
* 128 CPU cores per node, implicits the following:
    1. If your code is serial and doesn't has multithreading capabilities, use one core/CPU per job.
    2. If your code doesn't support MPI, or you don't know what MPI is, use maximum 128 cores per job.
    3. For MPI jobs using more than one node, always use a number of cores divisible by 128, to utilize the full nodes.

The Dalma HPC consists of more than 12K CPU cores. But it is very unlikely that your code can scale up to use them all (contact us directly if you are confident). From the user perspective, here are the important specifications for most nodes:

* The CPU model is Intel(R) Xeon(R) CPU E5-2680 v4 @ 2.40GHz, supporting AVX2.
* 3.75 GB memory per core by default.
* 28 CPU cores per node, implicits the following:
    1. If your code doesn't support MPI, or you don't know what MPI is, use maximum 28 cores per job.
    2. For MPI jobs using more than one node, always use a number of cores divisible by 28, to utilize the full nodes.

Contact us if you need special configuration (extra large memory, GPU, etc...)

Typical Workflow
----------------

1. (One time only) Let us know your computational requirement.
2. (One time only) Apply an HPC account and pass our quiz.
3. If needed, transfer your input data to Dalma.
4. Log on to Dalma login nodes.
5. Submit jobs on login nodes. 
6. Your jobs will queue for execution.
7. Once done, examine the output.

Summary of Nodes
----------------

.. list-table:: 
    :widths: auto 
    :header-rows: 1

    * - Node Type
      - Num Nodes
      - CPUs / Node
      - Memory / node
      - GPUs / node
      - Remarks
    * - Standard
      - 375
      - 28
      - 112 GB 
      - None
      - Use for general purpose
    * - Bigmem
      - 3	
      - 64
      - 1 TB / 2TB	
      - None	
      - Use when memory requirement per node is greater than 112GB
    * - :doc:`GPU </hpc/system/gpu_nodes>` 
      - 10
      - 40
      - 360 GB
      - 2/8	(Nvidia V100)
      - Two nodes have 8 GPU cards each, rest of them have 2 each
    * - Visual	
      - 4	
      - 38	
      - 112 GB
      - 1 (Nvidia Quadro P4000)
      - Used for GUI 


Access
------

Once your account is ready, you can access Jubail HPC. With Linux or Mac in NYU AD/NY network, simply ssh in your local terminal:
This works if you are within the NYU network or connected to the VPN

.. code-block:: bash

    ssh <NetID>@jubail.abudhabi.nyu.edu

Whenever you login, you land up on the login node which is shown on left most section of
your terminal and may look something like ``[wz22@login-0-2 ~]$`` suggesting that you are on one of the login nodes.


.. code-block:: bash

  Last login: Fri Dec 17 04:07:47 2021 from hpc.abudhabi.nyu.edu
  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  Welcome to Jubail!

  For documentation & examples: https://crc-docs.abudhabi.nyu.edu
  For support: nyuad.it.help@nyu.edu
  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  [wz22@login-0-2 ~]$

.. warning::
    Please refrain from running jobs on the login nodes. This can lead to your account getting suspended.



