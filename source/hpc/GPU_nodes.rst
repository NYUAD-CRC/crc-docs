GPU nodes in Dalma
==================

When using the GPU nodes available on Dalma.

Currently Dalma holds 10 GPU nodes equipped with NVIDIA-V100 cards. Two of those nodes have 8 GPU V100 cards and 1TB of memory per node. The rest (8) have 2 GPU V100 cards with 360GB per node. Each node has 40 CPUS. 

.. Warning::
    The current Nvidia driver version on the GPU nodes is 410.79 which supports cuda/10.0 or lower. We cannot update the Nvidia driver due to certain OS restrictions and dependencies. We shall have the drivers updated in our new release.

Step-by-step guide
-------------------

1. Users that want to have access to the GPU nodes have to make a request for access. By default, any account in Dalma is created without access to the GPU nodes.

2. In order to submit jobs to be allocated in the GPU nodes, these are the slurm directives (where ``<NUMBER>`` is the number of GPU cards requested):

.. code-block:: bash

    #SBATCH --gres=gpu:<NUMBER>

    #SBATCH -p nvidia
.. Note::        
    The following limits apply to the GPU partition in Slurm. These limits might change in the future depending on the demand:

    Max CPUs per user = 20
    Max GPUs per user = 2
    Max jobs per user = 2
    Max allowed walltime = 48 hours
    Default walltime = 4 hours