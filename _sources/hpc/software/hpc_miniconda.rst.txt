

Miniconda on the HPC
=====================

We have a centralized installation of Miniconda on the HPC. The users can either 
install their own Miniconda or use the centralized installation present on the HPC. This centralized installation can also be used for creating your own local environments, wherein you can install your own packages. Moreover, You can clone the existing centralized environments (like Tensorflow, R) and add other required libraries or packages on top of it.  

The conda cheat sheet gives you a list of useful commands in a glance:  `Conda-cheat-sheet <https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf>`__


.. _one_time_setup:

One Time Setup
---------------

Execute the following command for making the HPC Miniconda as your default conda environment. This is needed to be done **ONLY once**, just for setting up Miniconda for your account. Loading the miniconda module sets the miniconda environement for your account. You also need to source the bashrc file to activate the changes in your current shell. Once the environment is set up, **you donot need to load the miniconda again in your subsequent logins**.

.. code-block:: bash

	module load miniconda
	source ~/.bashrc
	echo "export CONDA_ENVS_PATH=$SCRATCH/conda-envs" >> ~/.bashrc
	echo "export CONDA_PKGS_DIRS=$SCRATCH/conda-envs/pkgs" >> ~/.bashrc

Application Installation
------------------------

Following are the steps which need to be followed to install an application using conda.

* Create a local conda environment using conda create (more details below)
* Activate the local conda environment using conda activate (more details below)
* Install the application using conda install (eg : ``conda install -c r r=3.6``)
* Clean/remove the residual/cache files created by conda which eat up your quota (eg: ``conda clean -a``)

.. Note::

	The number of files quota usually gets filled up very quickly, if you use conda/pip environment as they generate a large number of residual files. They don't remove them automatically and 
	hence stay in your $HOME affecting your files quota. 

	We recommend you to clean your conda/pip cache files (if any). This cleaning up of cache files is very easy and needs only a single command to be run.

  Following commands and links can come handy:

  - ``conda clean -a``
  - https://docs.conda.io/projects/conda/en/latest/commands/clean.html
  - ``pip cache purge``
  - https://pip.pypa.io/en/stable/cli/pip_cache/

.. _managing_envs:

Managing Environments
---------------------


**Create a Local Environment**

The below command creates a conda environment in your ``$SCRATCH/conda-envs`` if you have followed the :ref:`One Time Setup <one_time_setup>` instructions described above else the environments will be created in your home (which is not recommended as ``$HOME`` quota is limited).   

.. code-block:: bash

    #conda create -n <name of the env>
    
    #example:
    conda create -n myenv

**Activate the Local Environment**

.. code-block:: bash

    #conda activate <name of the local env>

    #example:
    conda activate myenv


**Deactivate an Environment**

.. code-block:: bash

    conda deactivate


**Listing the Environments Available**

This shows the existing local and centralized Miniconda environments available

.. code-block:: bash

    conda env list

A sample output is shown below. The list of centralized and local installations can be seen. 

.. code-block:: bash

                                         /scratch/wz22/conda-envs/myenv
                                         /scratch/wz22/conda-envs/myenv2
                                         /scratch/wz22/conda-envs/myenv3
                                         /scratch/wz22/conda-envs/myenv4
    base                            *    /share/apps/NYUAD/miniconda/3-4.8.2
    firefox                              /share/apps/NYUAD/miniconda/3-4.8.2/envs/firefox
    tensorflow-1.15                      /share/apps/NYUAD/miniconda/3-4.8.2/envs/tensorflow-1.15
    tensorflow-2.0                       /share/apps/NYUAD/miniconda/3-4.8.2/envs/tensorflow-2.0


**Cloning an Environment**

.. code-block:: bash

    #conda create -n <name of the new env> --clone <path to existing env>
    #example: Here we clone the existing Tensorflow environment.
    conda create -n tf-gpu --clone tensorflow-1.15

Migrating / Sharing Environment
-------------------------------

It is possible to migrate an environment, with exact same packages and configuration. 
This is the beauty of Conda. Same environment, anywhere.


1. Activate the environment you want to migrate from.
    .. code-block:: bash
       
        # Activate the environment you want to migrate from
        # Example: conda activate <env-migrate-from>
        conda activate myenv

2. Export the environment to an yml file.
    .. code-block:: bash
        
        # In this example, the yml file is called environment.yml
        conda env export > environment.yml

3. Share this yml file.
    The other person / machine, an identical environment could be created using this yml file.
    
    .. code-block:: bash

        # In this example, the yml file is called environment.yml
        conda env create -n myenv -f environment.yml




Submitting Job Scripts
----------------------

The conda environment might not get activated when submitting a Job script since the slurm doesn't source the ``bashrc`` file. Hence, in order to go about this, you can include the following line in your job submission script before activating the required environment.

.. code-block:: bash

    source ~/.bashrc

A sample job submission script is shown below:

.. code-block:: bash

    #!/bin/bash
    #SBATCH -n 10
    #SBATCH -t 48:00:00
    #Other SBATCH commands go here
    
    #Activating conda
    source ~/.bashrc
    conda activate myenv1
    
    #Your appication commands go here
    python abc.py

.. tip::

    In order to avoid activating a long path everytime, an alias can be created in the bashrc similar to the following 

    .. code-block:: bash

        alias myenv1='conda activate myenv1'

    This will activate the environment just by typing ``myenv1``.
    
.. Note::

	If you donot miniconda paths to mess up your bashrc, you can use **ONE** of the following commands 
	
	.. code-block:: bash
	
		source /share/apps/NYUAD/miniconda/3-4.11.0/bin/activate
		#you can also create an alias for the above command in your bashrc
		
	.. code-block:: bash
	
		module load miniconda-nobashrc
		eval "$(conda shell.bash hook)"

.. Note::
    
    Go through the Conda 30 mins test drive to make sure you understand the basic concepts: https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html