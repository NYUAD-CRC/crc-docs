R in Dalma Miniconda
====================

Apart from a centralized installation of R, we also have a Miniconda installation of R (ver=3.6) as part of the Miniconda module in Dalma. This provides greater flexibility and easier installation for other complementary packages required for R (eg: Tidyverse, Rstan etc). To find more details on the Miniconda module usage, click :doc:`here<python/dalma_miniconda>`.

.. tip::
    If you have never used Conda, we recommend you to use Dalma Miniconda. 
    You can find the steps to set up Dalma Miniconda by clicking :doc:`here <python/dalma_miniconda>`.

.. note::
    The conda cheat sheet gives you a list of useful commands in a glance:  `Conda-cheat-sheet <https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf>`__

How to clone the R environment
------------------------------

1. If you are using Dalma Miniconda 
    This creates an exclusive local environment (installation) of the R package in the given path (in the example below, the path is "/scratch/wz22/my-envs/R"). The User can now activate this environment and use it and further install any required complementary packages in the activated environment (More details on this in upcoming sections).
    
    .. code-block:: bash

        #conda create -p /scratch/<NetID>/conda-envs/R --clone R-3.6

        #or

        #conda create -n <name of the new env> --clone <existing env>

        #example:
        conda create -p /scratch/wz22/conda-envs/R --clone R-3.6

        #or

        conda create -n R --clone R-3.6


    A sample output is shown below:

    .. image:: ../img/R1.png

    .. note::

        It must be noted that the given path is not the path to the working directory, but the location where the user wishes to install the environment. The user can navigate to any directory (where his application and running script resides) and activate the required environment.  

2. If you are using your own conda package

    .. code-block:: bash

        #conda create -p /scratch/<NetID>/conda-envs/R --clone <path-to-existing-env>

        #or

        #conda create -n <name of the new env> --clone <path to existing env>

        #example:

        conda create -p /scratch/wz22/conda-envs/R --clone /share/apps/NYUAD/miniconda/3-4.8.2/envs/R-3.6

        #or

        conda create -n R --clone /share/apps/NYUAD/miniconda/3-4.8.2/envs/R-3.6

Finding the Conda complementary packages (Tidyverse, Rstan etc)
---------------------------------------------------------------

1. Search on the web for the Conda package of the required library.
    For instance, if the required library is Tidyverse, you can search for "conda install r tidyverse". You can then navigate to the link with anaconda (most probably the first one, like here).
2. Find the installation command from the anaconda link
    The page should look something like this :

    .. image:: ../img/R2.png

    The command highlighted in red box is the command for installing the required package.


How to install the Conda complementary packages
-----------------------------------------------

1. Activate the local R environment
    you can find more about managing environments, by clicking :ref:`here<managing_envs>`.

    .. code-block:: bash
    
        #conda activate <name of the environment>
        #example:
        conda activate R

2. Install the required package
    Paste the installation command found on the Anaconda web page as described above. Enter ``y`` when it prompts for confirmation.

    .. code-block:: bash

        #example:
        conda install -c r r-tidyverse


    A sample output is shown below:

    .. image:: ../img/R3.png

    .. warning::
        It must be noted that the complementary packages must be installed only after activating the local R environment. 

3. Once the installation is done, launch R and check the installation of the package using the "library( )" function of R.
    A sample output is shown below:
    .. image:: ../img/R4.png

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
    #Other SBATCH commands go here
    
    #Activating conda
    source ~/.bashrc
    conda activate R
    
    #Your appication commands go here
    Rscript abc.R

.. seealso::
    Go through the Conda 30 mins test drive to make sure you understand the basic concepts:  https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html