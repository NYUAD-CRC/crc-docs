PyTorch in Dalma
================

We have PyTorch (1.4 & 1.7) installations as part of Miniconda module in Dalma. 
You can clone the existing centralized environment to your local environment and 
add other required libraries or packages on top of it after activating it. 
To find more details of the Miniconda module in Dalma, click :doc:`here <dalma_miniconda>`.

.. note::
    If you have never used Conda, we recommend you to use Dalma Miniconda. 
    You can find the steps to set up Dalma Miniconda by clicking :doc:`here <dalma_miniconda>`.

How to clone the **PyTorch** environment
----------------------------------------

1. If you are using Dalma Miniconda 

    .. code-block:: bash
    
        #conda create -n <name of the new env> --clone <existing env>
        #example:
        conda create -n pytorch --clone pytorch-1.4
        #You can also have the environment in a custom location
        conda create -p /scratch/wz22/conda-envs/pytroch


2. If you are using your own conda package

    .. code-block:: bash

        #conda create -n <name of the new env> --clone <path to existing env>
        #example:
        conda create -n pytorch --clone /share/apps/NYUAD/miniconda/3-4.8.2/envs/pytorch-1.4

Submitting Job Scripts
----------------------

The conda environment might not get activated when submitting a Job script since the slurm doesn't source the bashrc file. Hence, in order to go about this, you can include the following line in your job submission script before activating the required environment.

.. code-block:: bash
    
    source ~/.bashrc

A sample job submission script is shown below:

.. code-block:: bash

    #!/bin/bash
    #SBATCH -n 10
    #SBATCH -t 48:00:00
    #SBATCH -p nvidia
    #SBATCH --gres=gpu:1
    #Other SBATCH commands go here
    
    #Activating conda
    source ~/.bashrc
    conda activate pytorch
    
    #Your appication commands go here
    python abc.py

.. note::
    These installations have preinstalled cuda and cudnn libraries as well and hence there is no need to load cuda modules explicitly 