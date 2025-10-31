*************
Introduction
*************

.. rst-class:: text-justify

    New York University Abu Dhabi (NYUAD) High Performance Computing (HPC) Center serves New York University 
    Abu Dhabi (NYUAD) researchers, faculty and students by providing them with HPC services and support to 
    help them conduct world-class computational research and education. The HPC Center provides its services 
    through a medium-sized Linux cluster called Jubail - launched in March 2022. 
    
    Named after Jubail Island, Home of the Jubail Mangrove Park, the first self-contained educational, 
    nature, and leisure destination of its kind in the Emirate of Abu Dhabi.
    
    In Brief, it is a **3.9 PFLOPs (~49,280 CPU cores)** cluster hosted at the NYUAD Data Center in Saadiyat,  
    comprising 40 racks.


.. list-table:: 
    :widths: auto 
    :header-rows: 1

    * - Node Type
      - Number
      - Specifications
      - Total PFlops
    * - CPU 
      - 334 nodes
      - AMD EPYC Rome CPU (128 cores & 512GB RAM each)
      - 1.4
    * - GPU 
      - 178 GPUs
      - Nvidia Tesla V100, A100, H100 & H200 GPUs
      - 2.5
   

The previous HPC Dalma cluster was integrated with Jubail starting from 10th of March 2022. The details of the
previous HPC systems can be found :doc:`here </hpc/old_hpc>` 

.. warning::
    Please refrain from running jobs on the login nodes. This can lead to your account getting suspended.

Useful Links
------------
.. warning::
    The links mentioned below require you to be connected to the NYUAD VPN

.. list-table:: 
    :widths: auto 
    :header-rows: 1

    * - **Description**
      - **Links**
    * - **Request/Renew HPC Accounts**
      - https://identity.it.nyu.edu
    * - **HPC Web Interface**
      - https://ood.hpc.abudhabi.nyu.edu
    * - **HPC Jobs Stats**
      - https://slurm.hpc.abudhabi.nyu.edu 
    * - **HPC Node Monitor**
      - https://monitor.hpc.abudhabi.nyu.edu


You could:
    * Connect to HPC from your browser. The :doc:`HPC Web Interface <ood/index>` is a one stop solution for all your HPC needs.
    * Open an account on our HPC cluster Jubail (:doc:`Accounts <accounts/index>`)
    * Hop on to :doc:`HPC Training </hpc/training/index>` page to get a quick intro to HPC.
    * Learn more about the system and how you can access it (:doc:`System <system/index>`)
    * Check out the :doc:`Storage <storage/index>` page for user quota and different storages available.
    * Learn how to submit jobs here (:doc:`Jobs Management <jobs/index>`)
    * Learn more about the software stack and what it offers you in terms of your application (MPI,Python,R) (:doc:`Software <software/index>`)
    * Checkout the research works carried out on the system and donot forget to acknowledge us (:doc:`Research <research/index>`)
    * Follow our :doc:`Help <help/index>` page for more HowTo's  
    * The :doc:`HPC Load<hpc_load/index>` page gives a glimpse of the current cluster utilization.
    * Contact us anytime at jubail.admins@nyu.edu

.. important:: 

    **Acknowledgement**
        We ask our users to acknowledge the use of the HPC resources by including the following in any publication resulting from work carried out on the HPC:
        
        **This research was carried out on the High Performance Computing resources at New York University Abu Dhabi.**

.. admonition:: Contact us

    Contact us anytime at jubail.admins@nyu.edu
