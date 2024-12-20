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
* 480GB per node.
* 3.75 GB memory per core by default.
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
3. If needed, transfer your input data to the HPC.
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
    * - Jubail Compute
      - 224
      - 128
      - 480GB
      - None
      - New HPC Compute nodes
    * - Jubail Gpu
      - 95 GPUs
      - 64/128
      - 480GB
      - 1/2/3/4 (Nvidia A100)
      - New HPC GPU nodes
    * - Dalma Compute
      - 428
      - 28/40
      - 102 GB / 480 GB
      - None
      - Small jobs < 28 CPUs will be sent to Dalma
    * - Dalma GPUs
      - 39 GPUs
      - 40
      - 360 GB / 1 TB
      - 2/8 (Nvidia V100)
      - Two nodes have 8 GPU cards each, rest of them have 2 cards each
    * - Bigmem
      - 5	
      - 32/64/72/128
      - 1 TB / 2TB	
      - None	
      - Used when memory requirement per node is greater than 500GB
    * - Visual	
      - 4	
      - 32	
      - 105 GB
      - 2 (Nvidia Quadro P4000)
      - Used for GUI 

	    
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
               /home    10099MB       20GB ( 49%)        77       150 ( 52%)
            /scratch       53GB     5000GB (  1%)        74       500 ( 15%)
            /archive       24GB     5120GB (  0%)         1       125 (  1%)
            
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

