Singularity - How to Run on HPC
===============================

We have discussed about the containers already :doc:`Singularity Containers <singularity>`. You can have a look at it if you wish to get an insight into the world of containers. In this section we deal with its usage on the HPC.

.. warning::
	On the HPC, Singularity containers must be only run on compute nodes as they are too resource-intensive for login nodes
	

Singularity Module
------------------

Singularity is available on the HPC in the form of modules.The default version available is ``3.8``. You can load the following as follows:

.. code-block:: bash
	
	#This will load the default version (3.8)
	module load singularity
	
	#In order to view all the versions available
	module load all
	module avail singlarity
	
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