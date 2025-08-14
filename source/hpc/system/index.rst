System
======


Overview
--------

The operating system on the HPC is Linux. Make sure you know the basics. Useful links:

* https://www.tutorialspoint.com/unix/index.htm
* https://www.geeksforgeeks.org/essential-linuxunix-commands
* http://linuxcommand.org/
* http://software-carpentry.org/lessons/
* https://www.edx.org/course/introduction-linux-linuxfoundationx-lfs101x-0


.. image:: ../img/system-1.png


Generic diagram of the cluster architecture and outside connectivity.

Hardware
--------

The HPC cluster includes the integration of previous HPC cluster Dalma with Jubail HPC cluster.

The Jubail HPC consists of more than 29K cores.

* The CPU model is AMD EPYC 7742 64-Core Processor @2.25GHz,supporting AVX2.
* 480GB usable memory per node (512 GB theoretically). Bigmem nodes consist of 1 TB theoretical memory.
* 3.75 GB memory per core by default.
* 128 CPU cores per node, implicits the following:
    1. If your code is serial and doesn't has multithreading capabilities, use one core/CPU per job.
    2. If your code doesn't support MPI, or you don't know what MPI is, use maximum 128 cores per job.
    3. For MPI jobs using more than one node, always use a number of cores divisible by 128, to utilize the full nodes.

The Dalma HPC consists of more than 12K CPU cores. But it is very unlikely that your code can scale up to use them all (contact us directly if you are confident). From the user perspective, here are the important specifications for most nodes:

* The CPU model is Intel(R) Xeon(R) CPU E5-2680 v4 @ 2.40GHz, supporting AVX2. There are 8 nodes with Intel(R) Xeon(R) Gold 6148 (40 CPU cores). Bigmem node CPU models are AMD EPYC 7551, Intel(R) Xeon(R) CPU E7- 8837, Intel(R) Xeon(R) CPU E7-8867 v4 
* 112GB usable memory per node (128 GB theoretically). Bigmem nodes consist of 1 and 2 TB theoretical memory.
* 4 GB memory per core by default.
* 28 CPU cores per node, implicits the following:
    1. If your code doesn't support MPI, or you don't know what MPI is, use maximum 28 cores per job.
    2. For MPI jobs using more than one node, always use a number of cores divisible by 28, to utilize the full nodes.

Contact us if you need special configuration (extra large memory, GPU, etc...)

Typical Workflow
----------------

1. (One time only) Let us know your computational requirement.
2. (One time only) Apply an HPC account and pass our quiz.
3. If needed, transfer your input data to the HPC.
4. Log on to HPC login nodes.
5. Submit jobs on login nodes. 
6. Your jobs will queue for execution.
7. Once done, examine the output.

Summary of Nodes
----------------

Compute Nodes:
--------------
.. list-table::
    :widths: auto
    :header-rows: 1

    * - | 
        | Node Type
      - | 
        | Num Nodes
      - | CPUs / Node
      - | 
        | MEM / Node
        | (RAM)
      - |
        | ____________Remarks____________
    * - Bigmem Jubail
      - 1
      - 128
      - 1 TB
      - | 
        | AMD EPYC 7742
        | 
        | Memory requirement > 512 GB
    * - Jubail
      - 233
      - 128
      - 512 GB
      - AMD EPYC 7742
    * - Bigmem Dalma
      - 4
      - 32 / 64 / 72
      - 1 TB / 2 TB
      - | 
        | AMD EPYC 7551
        | 
        | Intel(R) Xeon(R) CPU E7- 8837
        | 
        | Intel(R) Xeon(R) CPU E7-8867 v4
        | 
        | Memory requirement > 512 GB
    * - Dalma
      - 432
      - 28 / 40
      - 128 GB / 512 GB
      - | 
        | Intel(R) Xeon(R) CPU E5-2680 v4
        | [Small jobs < 28 CPUs]
        | 
        | Intel(R) Xeon(R) Gold 6148

GPU Nodes:
--------------
.. list-table::
    :widths: auto
    :header-rows: 1

    * - | 
        | Node Type
      - | 
        | Num Nodes
      - | 
        | CPUs / Node
      - | 
        | MEM / Node
        | (RAM)
      - | 
        | GPUs / Node
      - | 
        | MEM / GPU
        | (VRAM)
      - | 
        | Num GPUs
      - | 
        | ___________Remarks___________
    * - Jubail
      - 36
      - 64 / 128
      - 512 GB
      - 1 / 2 / 3 / 4
      - 40 / 80
      - 101
      - | 
        | Nvidia A100
        | 
        | AMD EPYC 7543
        | 
        | AMD EPYC 7742
    * - Dalma 1TB
      - 2
      - 40
      - 1 TB
      - 8
      - 32
      - 16
      - | 
        | Nvidia Tesla V100
        | 
        | Intel(R) Xeon(R) Gold 6148 CPU
    * - Dalma
      - 11
      - 40
      - 320 GB / 384 GB
      - 2
      - 32
      - 22
      - | 
        | Nvidia Tesla V100
        | 
        | Intel(R) Xeon(R) Gold 6148 CPU

Visual Nodes:
--------------
.. list-table::
    :widths: auto
    :header-rows: 1

    * - | 
        | Node Type
      - | 
        | Num Nodes
      - | 
        | CPUs / Node
      - | 
        | MEM / Node
        | (RAM)
      - | 
        | GPUs / Node
      - | 
        | MEM / GPU
        | (VRAM)
      - | 
        | Num GPUs
      - | 
        | __Remarks__
    * - Visual
      - 4
      - 32
      - 128 GB
      - 2
      - 8
      - 8
      - GUI Nodes


Access
------

Once your account is ready, you can access the HPC. With Linux or Mac in NYU AD/NY network, simply ssh in your local terminal:

.. code-block:: bash

    ssh <NetID>@jubail.abudhabi.nyu.edu

If you use Windows or outside NYU AD/NY network, follow the instructions here: :doc:`Access Jubail <access_jubail>`.

.. admonition:: Caution for VS Code Users
  
  Please always use the following method to connect to HPC from :doc:`VS Code on HPC <vscode>`. 
  Connecting directly to the login nodes leaves background processes running in the login node for each new connection thus accumulating 
  over time until you reach the threshold after which no more processes for a user are allowed on login which 
  further results in login failures. Any VS code processes on login nodes are now automatically terminated after 10 minutes.

.. toctree::
 :hidden:

 /hpc/system/access_jubail
 /hpc/system/vscode

Passwordless Authentication
---------------------------

Users can follow the following guide to setup passwordless authnetication to the HPC :doc:`Enabling Passwordless Authentication </hpc/system/passwordless_auth>`.

.. toctree::
 :hidden:

 /hpc/system/passwordless_auth



Whenever you login, you land up on one of the four login nodes, which is shown on left most section of
your terminal.It may look something like ``[wz22@login2 ~]$`` suggesting that you are on the second login node.


.. code-block:: bash

  Access allowed by pam_access
  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  Welcome to Jubail!

  For documentation & examples: https://crc-docs.abudhabi.nyu.edu
  For support: nyuad.it.help@nyu.edu
  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  Last login: Wed Feb 15 15:27:08 2023 from 10.224.42.159
  Disk quotas for wz22 (uid 3387153):
                          DISK SPACE                # FILES (1000's)
          filesystem       size      quota            number      quota
                      --------------------------   --------------------------
               /home       92KB       50GB (  0%)         0       500 (  0%)
            /scratch        4KB     5000GB (  0%)         0       500 (  0%)
            /archive        4KB     5120GB (  0%)         0       125 (  0%)
  [wz22@login2 ~]$

.. Important::
    Please refrain from running jobs on the login nodes. This can lead to your account getting suspended.

.. _data_transfers:

Data Transfers
--------------

You can use either :doc:`rsycn command </hpc/system/rsync_transfer>` or :doc:`FileZilla (with a GUI) </hpc/system/filezilla_transfer>` to transfer your data from/to the HPC cluster.
Windows users can use `WinScp <https://winscp.net/eng/index.php>`__ for transferring data to and from the HPC cluster.

.. toctree::
  :hidden:

  /hpc/system/rsync_transfer
  /hpc/system/filezilla_transfer

  
.. note::

  For data sharing among collaborators, Kindly refer to the section :doc:`here </hpc/storage/data_sharing>`

.. note::

  For large date transfer, Kindly refer to the section :doc:`here </hpc/system/screen>`
   

  
Globus Data Transfer
--------------------

The NYUAD HPC Researchers can also benefit from transferring large data within the globus network 
at a faster rate.

* :doc:`Globus Data Transfer <globus>`

.. toctree::
  :hidden:

  /hpc/system/globus
  /hpc/system/screen

