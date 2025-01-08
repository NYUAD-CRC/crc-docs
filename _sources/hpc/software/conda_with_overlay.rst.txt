Conda with Overlay
==================

`Conda <https://crc-docs.abudhabi.nyu.edu/hpc/software/hpc_miniconda.html#miniconda-on-the-hpc/>`__ environments allow users to create customizable, portable work environments and dependencies to support specific packages or versions of software for research. Common conda distributions include Anaconda, Miniconda and `Miniforge <https://github.com/conda-forge/miniforge>`__. Packages are available via "channels". Popular channels include "conda-forge" and "bioconda".  
This section describes using Miniforge which sets "conda-forge" as the package channel, inside an overlay.

An `Overlay <https://crc-docs.abudhabi.nyu.edu/hpc/software/singularity_overlays.html>`__ is simply a directory or a filesystem image which sits on top of a `Singularity Container <https://crc-docs.abudhabi.nyu.edu/hpc/software/singularity.html>`__.
As a user you can benefit from the overlays in the following ways:

- You have too many conda environments eating up your number of files limit
- You would like to share your environments (R,conda,etc) with your collaborators with no installation required.
    

Creating a Conda Overlay
------------------------

To create an overlay with conda, use the ``create-overlay-conda`` command. This command takes the size of the overlay in 
megabytes and the number of files as arguments. The usage is as follows:

.. code-block:: console

    create-overlay-conda -s <size-in-Megabytes> -n <number-of-files-in-1000's> [ -o <name-of-overlay> ]

    # Example:
    create-overlay-conda -s 7000 -n 700

The above example will create an overlay by the name ``overlay-7000M-700K.ext3`` of 7000MB capacity with a 
number of file limit of 700K. 
The overlay will be named ``overlay-<size>M-<numfiles>K.ext3`` by default. It can be customized by specifying
the name with ``-o`` argument.

A sample output of the ``create-overlay-conda`` command is shown below:

.. code-block:: console

    (base) [fatema@login4 test-overlay-conda]$ create-overlay-conda -s 7000 -n 700 -o overlay-with-conda
    ======================
    # Overlay Info       #
    ======================
    Overlay Size: 7000M
    No. of Files limit: 700K
    Name of Overlay: overlay-with-conda.ext3
    ======================
    # Creating overlay   #
    ======================
    6965945344 bytes (7.0 GB, 6.5 GiB) copied, 26 s, 268 MB/s
    7000000+0 records in
    7000000+0 records out
    7168000000 bytes (7.2 GB, 6.7 GiB) copied, 26.7555 s, 268 MB/s
    mke2fs 1.45.4 (23-Sep-2019)
    Discarding device blocks: done                            
    Creating filesystem with 1750000 4k blocks and 700704 inodes
    Filesystem UUID: 5a9d4e59-4c09-42d4-a31b-b2af371084eb
    Superblock backups stored on blocks: 
	    32768, 98304, 163840, 229376, 294912, 819200, 884736, 1605632

    Allocating group tables: done                            
    Writing inode tables: done                            
    Creating journal (16384 blocks): done
    Copying files into the device: done
    Writing superblocks and filesystem accounting information: done 

    ====================
    #      Done	 #
    ====================
    Finished creating overlay. It is located in /scratch/fatema/test-overlay-conda/overlay-with-conda.ext3


.. hint:: 
    Please make sure the <size-in-Megabytes> is appropriate to accommodate the size of the conda.
 
    
Mounting an Overlay
-------------------

To mount an overlay, use the ``mount-overlay`` command. This command takes the name of the overlay file 
as an argument.  
The usage is as follows:

.. code-block:: bash

    mount-overlay -o <name-of-overlay> [-c <path-to-container>]...

    # Example:
    mount-overlay -o overlay-7000M-700K.ext3


Managing the Conda Environment in the Overlay
---------------------------------------------

Activate your conda environment with the following:

.. code-block:: bash

    source /ext3/env.sh
   
   
    
Now that your environment is activated, to confirm that your environment is appropriately referencing your Miniforge installation, try out the following:

.. code-block:: bash

    which conda
    # output: /ext3/miniforge3/bin/conda
    which python
    # output: /ext3/miniforge3/bin/python
    python --version
    # output: Python 3.12.8
    which pip
    # output: /ext3/miniforge3/bin/pip



