Singularity - How to Run on HPC
===============================

We have discussed about the containers already :doc:`Singularity Containers <singularity>`. You can have a look at it if you wish to get an insight into the world of containers. In this section we deal with its usage on the HPC.

.. warning::
	On the HPC, Singularity containers must be only run on compute nodes as they are too resource-intensive for login nodes
	

Commands at a glance
--------------------

Singularity commands mostly used are given below. The ``container.sif`` refers to a sample container and ``example.def`` refers to a sample definition file

	.. code-block:: bash
	
		#Build a container
		singularity build container.sif example.def
		
		#pull an existing container from a hub
		singularity pull docker://gcc
		
		#Shell Into the container
		singularity shell container.sif
		
		#running a container (More on this in subsequent sections)
		singularity run container.sif
		
		#Execute a command inside container
		singularity exec container.sif ls -l
		
		#Mounting/Binding a filesystem to the container
		singularity -B /share/apps/NYUAD
		
		#Singularity help (very helpful)
		singularity help
		singularity help build
		
Interact With Container
-----------------------

**Shell**

The ``shell`` command allows you to spawn a new shell within your container and interact with it as though it were a small virtual machine.

.. code-block:: bash
	
	singularity shell hello-world.sif

Don't forget to ``exit`` when you're done. 


**Executing commands**

The ``exec`` command allows you to execute a custom command within a container by specifying the image file.

.. code-block:: bash

	singularity exec hello-world.sif ls -l /	
	singularity exec hello-world.sif /scratch/user/userid/myprogram

**Running a container**

Execute the default `runscript <https://sylabs.io/guides/3.7/user-guide/quick_start.html#running-a-container>`__ defined in the container

.. code-block:: bash

	singularity run hello-world.sif

Files in a container
--------------------

The filesystem inside the container is isolated from the filesystem outside the container. In order to access your files on a real, physical filesystem, you have to ensure that filesystem's directory is mounted. By default, Singularity will mount the ``$HOME``, ``$SCRATCH`` and ``/share/apps/NYUAD`` directory as well as the current working directory ``$PWD``. To specify additional directories, use the ``SINGULARITY_BINDPATH`` environment variable or the ``--bind`` or ``-B`` command line option.	

.. tip::
	To access cluster filesystem in the container, it is convenient to pre-create these folders in your container
	
	.. code-block:: bash
	
		mkdir /scratch
		mkdir /share/apps/NYUAD
 

.. code-block:: bash

	export SINGULARITY_BINDPATH="/scratch,$TMPDIR"

	#or

	singularity --bind "/scratch,$TMPDIR" [commands]

.. admonition:: Read more at:

    https://sylabs.io/guides/3.7/user-guide/bind_paths_and_mounts.html
		
GPU in a container
------------------

If your container has been compiled with CUDA version >= 9, it should work with the local GPUs. Just add the ``--nv`` flag to your singularity command.

.. code-block:: bash

	singularity exec --nv tensorflow-gpu.sif python3

Sample job script
-----------------

.. code-block:: bash

	#!/bin/bash
	
	#your SBATCH commands go here
	#SBATCH -n 10

	# execute the default runscript defined in the container 
	singularity run tensorflow.sif

	# execute a command within container
	#  the command should include absolute path if the command is not in the default search path
	singularity exec tensorflow.sif /scratch/wz22/run.sh
	
Build and Modify your own containers
------------------------------------

For building conatiners, please refer to the sections :ref:`here <create_singularity_containers>`.

Additional Documents
--------------------

- `Singularity Documentation <https://sylabs.io/guides/3.7/user-guide/index.html>`__
- `Singularity Quick Start Guide <https://www.sylabs.io/guides/3.7/user-guide/quick_start.html>`__





