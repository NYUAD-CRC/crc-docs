Miniconda in Dalma
==================

We have a centralized installation of Miniconda in Dalma. The users can either 
install their own Miniconda or use the centralized installation present in Dalma. This centralized installation can also be used for creating your own local environments, wherein you can install your own packages. Moreover, You can clone the existing centralized environments (like Tensorflow, R) and add other required libraries or packages on top of it.  

The conda cheat sheet gives you a list of useful commands in a glance:  Conda-cheat-sheet

One Time Set up
---------------

Execute the following command for making Dalma Miniconda as your default conda environment. This is needed to be done **ONLY once**, just for setting up Miniconda for your account. Loading the miniconda module sets the miniconda environement for your account. You also need to source the bashrc file to activate the changes in your current shell. Once the environment is set up, you donot need to load the miniconda again in your subsequent logins.

.. code-block:: bash

    module load miniconda
    source ~/.bashrc

Managing Environments
---------------------

**Create a Local Environment**

.. code-block:: bash

    #conda create -n <name of the environment>
    #example:
    conda create -n myenv1


**Activate the Local Environment**

.. code-block:: bash

    #conda activate <name of the environment>
    #example:
    conda activate myenv1


**Deactivate an Environment**

.. code-block:: bash

    conda deactivate


**Listing the Environments Available**

This shows the existing local and centralized Miniconda environments available

.. code-block:: bash

    conda env list

A sample output is shown below. The list of centralized and local installations can be seen. 

.. code-block:: bash
                                         /home/wz22/.conda/envs/myenv
                                         /home/wz22/.conda/envs/myenv2
                                         /home/wz22/.conda/envs/myenv3
                                         /home/wz22/.conda/envs/myenv4
    base                            *    /share/apps/NYUAD/miniconda/3-4.8.2
    firefox                              /share/apps/NYUAD/miniconda/3-4.8.2/envs/firefox
    tensorflow-1.15                      /share/apps/NYUAD/miniconda/3-4.8.2/envs/tensorflow-1.15
    tensorflow-2.0                       /share/apps/NYUAD/miniconda/3-4.8.2/envs/tensorflow-2.0


**Cloning an Environment**

.. code-block:: bash

    #conda create -p <path to new env> --clone <path to existing env>
    #example: Here we clone the existing Tensorflow environment.
    conda create -n tf-gpu --clone tensorflow-1.15


Submitting Job Scripts
----------------------

The conda environment might not get activated when submitting a Job script since the slurm doesn't source the ``bashrc`` file. Hence, in order to go about this, you can include the following line in your job submission script before activating the required environment.

.. code-block:: bash

    source ~/.bashrc
    A sample job submission script is shown below:

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
    
    Go through the Conda 30 mins test drive to make sure you understand the basic concepts: https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html