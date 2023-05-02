GPU nodes on HPC
==================

Currently Jubail HPC holds 89 GPU nodes equipped with NVIDIA-A100 and NVIDIA-V100 cards. 

.. tip::
    Know more about the Centralized HPC Miniconda,TensorFlow(Keras) and PyTorch installations available :ref:`here<hpc_miniconda>`

Step-by-step guide
-------------------

 In order to submit jobs to be allocated in the GPU nodes, these are the slurm directives (where ``<NUMBER>`` is the number of GPU cards requested):

.. code-block:: bash

    #SBATCH --gres=gpu:<NUMBER>

    #SBATCH -p nvidia

.. Note::        
    The following limits apply to the GPU partition in Slurm. These limits might change in the future depending on the demand:

    - Max CPUs per user = 80
    - Max GPUs per user = 8
    - Max jobs per user = 8
    - Max allowed walltime = 96 hours
    - Default walltime = 5 hours

If you would like to analyze your GPU jobs, Please refer to following 
section: :doc:`Analyzing GPU Usage</hpc/jobs/gpu_jobs>`
