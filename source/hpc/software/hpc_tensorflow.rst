TensorFlow (Keras) on HPC
===========================

We have Tensorflow (2.4 & 2.11) installations as part of Miniconda module on the HPC. 
You can clone the existing centralized environments to your local environments and add 
other required libraries or packages on top of it. To find more details of the 
Miniconda module on the HPC, click :doc:`here <hpc_miniconda>`. Since Keras uses Tensorflow in the backend, this environement also comes with GPU enabled keras preinstalled.

.. important:: 
    The current Nvidia driver version on the GPU nodes is updated to ``460.106`` which supports ``cuda/11.2`` and hence the TensorFlow versions >= 2.0 are now supported.

.. note::
    If you have never used Conda, we recommend you to use the HPC Miniconda. 
    You can find the steps to set up the HPC Miniconda by clicking :doc:`here <hpc_miniconda>`.

How to clone the TensorFlow environment
---------------------------------------

1. **If you are using the HPC Miniconda**

    .. code-block:: bash

        #conda create -n <name of the new env> --clone <existing env>

        #or

        #conda create -p <path to local env> --clone <existing env>

        #example:
        conda create -n tf-gpu --clone tensorflow-2.11

2. **If you are using your own conda package**

    .. code-block:: bash

        #conda create -n <name of the new env> --clone <path to existing env>
        #example:
        conda create -n tf-gpu --clone /share/apps/NYUAD5/miniconda/3-4.11.0/envs/tensorflow-2.11

Submitting Job Scripts
----------------------

The conda environment might not get activated when submitting a Job script since the slurm doesn't source the bashrc file. Hence, in order to go about this, you can include the following line in your job submission script before activating the required environment.

.. code-block:: bash

    source /share/apps/NYUAD5/miniconda/3-4.11.0/bin/activate

A sample job submission script is shown below:

.. code-block:: bash

    #!/bin/bash
    #SBATCH -c 10
    #SBATCH -t 48:00:00
    #SBATCH -p nvidia
    #SBATCH --gres=gpu:1
    #Other SBATCH commands go here
    
    #Activating conda
    source /share/apps/NYUAD5/miniconda/3-4.11.0/bin/activate
    conda activate tf-gpu
    
    #Your appication commands go here
    python abc.py

.. note:: 
    These installations have preinstalled cuda and cudnn libraries as well and hence there is no need to load cuda modules explicitly. 
