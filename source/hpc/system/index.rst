System
======

Overview
--------

The operating system on Dalma is Linux. Make sure you know the basics. Useful links:

* http://linuxcommand.org/
* http://software-carpentry.org/lessons/
* https://www.edx.org/course/introduction-linux-linuxfoundationx-lfs101x-0


.. image:: ../img/system-1.png


Generic diagram of the cluster architecture and outside connectivity.

Hardware
--------

Dalma consists of more than 12K CPU cores. But it is very unlikely that your code can scale up to use them all (contact us directly if you are confident). From the user perspective, here are the important specifications for most nodes:

* The CPU mode is Intel(R) Xeon(R) CPU E5-2680 v4 @ 2.40GHz, supporting AVX2.
* 28 CPU cores per node. Implications:
    1. If your code doesn't support MPI, or you don't know what MPI is, use maximum 28 cores per job.
    2. For MPI jobs using more than one node, always use a number of cores dividable by 28, to utilize the full nodes.

* 4 GB memory per core by default.

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



Access
------

Once your account is ready, you can access Dalma. With Linux or Mac in NYU AD/NY network, simply ssh in your local terminal:

.. code-block:: bash

    ssh <NetID>@dalma.abudhabi.nyu.edu

If you use Windows or outside NYU AD/NY network, follow the instructions here: :doc:`Access Dalma <access_dalma>`.

.. toctree::
   :maxdepth: 1
   :hidden:

   /hpc/system/access_dalma

.. _data_transfers:

Data Transfers
--------------

You can use either Terminal or FileZilla (with a GUI) to transfer your data from/to Dalma: 

.. toctree::
   :maxdepth: 1
   

   /hpc/system/rsync_transfer
   /hpc/system/filezilla_transfer
   
.. _special_compute_nodes: 

Special Compute Nodes
---------------------


.. toctree::
   :maxdepth: 1
   

   /hpc/system/visual_nodes
   /hpc/system/gpu_nodes 
   
Fast Transfer between NYC and Dalma
-----------------------------------

The default MLPS link between NY and AD has a low bandwidth. Using port 922 on Dalma will use a 
high bandwidth ANKABUT link instead.

.. toctree::
   :maxdepth: 1
   

   /hpc/system/nyc_file_transfer
