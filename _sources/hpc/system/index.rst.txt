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
The new HPC cluster includes the integration of previous HPC cluster Dalma with Jubail HPC cluster.

The Jubail HPC consists of more than 28K cores.

* The CPU model is AMD EPYC 7742 64-Core Processor @2.25GHz,supporting AVX2.
* 512GB per node.
* 4 GB memory per core by default.
* 128 CPU cores per node, implicits the following:
    1. If your code is serial and doesn't has multithreading capabilities, use one core/CPU per job.
    2. If your code doesn't support MPI, or you don't know what MPI is, use maximum 128 cores per job.
    3. For MPI jobs using more than one node, always use a number of cores divisible by 128, to utilize the full nodes.

The Dalma HPC consists of more than 12K CPU cores. But it is very unlikely that your code can scale up to use them all (contact us directly if you are confident). From the user perspective, here are the important specifications for most nodes:

* The CPU model is Intel(R) Xeon(R) CPU E5-2680 v4 @ 2.40GHz, supporting AVX2.
* 4 GB memory per core by default.
* 28 CPU cores per node, implicits the following:
    1. If your code doesn't support MPI, or you don't know what MPI is, use maximum 28 cores per job.
    2. For MPI jobs using more than one node, always use a number of cores divisible by 28, to utilize the full nodes.

Contact us if you need special configuration (extra large memory, GPU, etc...)

Typical Workflow
----------------

1. (One time only) Let us know your computational requirement.
2. (One time only) Apply an HPC account and pass our quiz.
3. If needed, transfer your input data to Jubail.
4. Log on to HPC login nodes.
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
    * - Bulk
      - 189
      - 128
      - 480GB
      - None
      - New HPC Compute nodes
    * - Versatile
      - 24
      - 128
      - 480GB
      - 1/2 (Nvidia A100)
      - New HPC GPU nodes with two nodes have only one GPU card each, rest of them have 2 cards each
    * - Dalma Compute
      - 432
      - 28/40
      - 128 GB / 512 GB
      - None
      - Small jobs < 28 CPUs will be sent to Dalma
    * - Bigmem
      - 4	
      - 32/63/72
      - 1 TB / 2TB	
      - None	
      - Used when memory requirement per node is greater than 500GB
    * - :doc:`Dalma GPU<gpu_nodes>` 
      - 14
      - 40
      - 360 GB / 1 TB
      - 2/8 (Nvidia V100)
      - Two nodes have 8 GPU cards each, rest of them have 2 cards each
    * - :doc:`Visual<visual_nodes>`	
      - 4	
      - 32	
      - 112 GB
      - 2 (Nvidia Quadro P4000)
      - Used for GUI 

.. admonition:: Difference between CPUs,Cores and Tasks

	- On Jubail HPC, One CPU is equivalent to one Core. 
	- In Slurm, the resources (CPUs) are allocated in terms of tasks which are denoted by ``-n`` or ``--natsks``. 
	- By Default, the value of ``-n`` or ``--ntasks`` is one if left undefined.
	- By Default, Each task is equivalent to one CPU.
	- But if you have defined ``-c`` or ``--cpus-per-task`` in your job script, then the CPUs allocated to you would be the multiple of ``-n`` and ``-c``.
	    
Access
------

Once your account is ready, you can access the HPC. With Linux or Mac in NYU AD/NY network, simply ssh in your local terminal:

.. code-block:: bash

    ssh <NetID>@jubail.abudhabi.nyu.edu

If you use Windows or outside NYU AD/NY network, follow the instructions here: :doc:`Access Jubail <access_jubail>`.


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

.. Important::
    Please refrain from running jobs on the login nodes. This can lead to your account getting suspended.

.. _data_transfers:

Data Transfers
--------------

You can use either :doc:`rsycn command </hpc/system/rsync_transfer>` or :doc:`FileZilla (with a GUI) </hpc/system/filezilla_transfer>` to transfer your data from/to the HPC cluster.
Windows users can use `WinScp <https://winscp.net/eng/index.php>`__ for transferring data to and from the HPC cluster.


  
.. note::

  For data sharing among collaborators, Kindly refer to the section :doc:`here </hpc/storage/data_sharing>`
   
.. _special_compute_nodes: 

Special Compute Nodes
---------------------

* :doc:`Visualization Nodes<visual_nodes>` 
* :doc:`GPU nodes on HPC<gpu_nodes>` 
   
Fast Transfer between NYC and NYUAD HPC
----------------------------------------

The default MLPS(Multiprotocol Label Switching) link between NY and AD has a low bandwidth. Using port 922 on NYUAD HPC will use a 
high bandwidth ANKABUT link instead.

* :doc:`Fast Transfer Between NYU NYC and NYUAD<nyc_file_transfer>` 

