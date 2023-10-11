=========================================
Conda Environment Migration from $SCRATCH
=========================================

Conda environments often produce a multitude of small files, which can adversely affect filesystem 
performance, especially on high-performance computing (HPC) systems. The rising number of Python users 
has resulted in a substantial increase in Python/Conda environments. These environments also pose 
challenges for effective file cleanup in ``$SCRATCH``.

To tackle this challenge, users are strongly encouraged to migrate their Conda environments from ``$SCRATCH`` 
to ``$HOME``. The ``conda-migrate`` tool offers a user-friendly solution for this process.

conda-migrate
-------------

``conda-migrate`` is a tool designed to help you migrate your existing Conda environments from ``$SCRATCH`` to ``$HOME``.


.. code-block:: shell

    conda-migrate [-d <path to a directory in scratch>] [--all]

Description
--------------------

The tool offers several key functions:

- It clones an existing Conda environment from a directory in ``$SCRATCH`` to ``$HOME/.conda/envs``.
- It conducts package comparisons between the old and new environments.
- It preserves a copy of the YAML file for each environment in the ``$HOME/.conda/yaml`` directory.
- If migration and comparison are successful, it removes the old environment.
- It updates Conda environment paths in ``~/.bashrc``.
- It conducts cleanup operations using ``conda clean``.


Options
-------

The ``conda-migrate`` tools accepts the following options

- ``-d <path to a directory>``
    Specify the directory containing Conda environments in your ``$SCRATCH`` that you want to migrate.

- ``--all``
    Migrate all valid Conda environments found in the specified directory in ``$SCRATCH``.


Usage
-----

The tool allows you to specify the directory containing the environments in ``$SCRATCH`` you wish to migrate using 
the ``-d`` flag. Additionally, you have the option to use the ``--all`` flag, which will migrate all 
the Conda environments found in the specified directory.

.. code-block:: shell

        conda-migrate -d <path to a directory in scratch> [--all]

Here's the step-by-step process the tool follows:

1. The tool scans the directory for valid Conda environments and presents the user with a list of environments to migrate.
2. Selected environments are serialized into YAML files and stored in ``$HOME/.conda/yaml``.
3. Environments are then cloned individually to the ``$HOME/.conda/envs`` directory.
4. Following successful cloning, the tool performs a comparison between the old and new environments.
5. If the cloned environment in ``$HOME`` matches the old environment in ``$SCRATCH``, the tool removes the old environment from ``$SCRATCH``.
6. Finally, the tool cleans up Conda cache files and updates certain Conda variables that previously pointed to ``$SCRATCH``.

Finding the Conda Environment directories
-----------------------------------------

One of the simplest commands to find out the source directory of the conda environments in ``$SCRATCH`` would be
as follows:

.. code-block:: shell

    conda env list | grep "/scratch"

Example output would be as follows:

.. code-block:: console

    (base)[wz22@login1 ~]$ conda env list | grep /scratch
                         /scratch/wz22/conda-envs/amd
                         /scratch/wz22/conda-envs/abc
                         /scratch/wz22/myenvs/hdf
                         /scratch/wz22/myenvs/xyz
                         
Following observations can be made from the above example:


- There are four different conda environments.
    - amd
    - abc
    - hdf
    - xyz
- There are two source directories where environemnts have been installed.
    - /scratch/wz22/conda-envs
    - /scratch/wz22/myenvs

Migrating Environments
----------------------

In this section, we will take an in-depth look at the tool by examining an example.

To migrate specific conda environment(s), simply specify the path to the directory in ``$SCRATCH`` 
containing the environments with the ``-d`` flag:

.. code-block:: console

    conda-migrate -d /path/to/your/conda/environment

The output is organized into sections to enhance clarity:

1. Valid Environments**


.. code-block:: console

    (3-4.11.0)[wz22@login1 ~]$ conda-migrate -d /scratch/wz22/conda-envs
    Valid Env: amd
    Valid Env: abc
    INVALID ENV: pkgs
    INVALID ENV: pyt
    
    Valid Conda environments in '/scratch/wz22/conda-envs':
    1. amd (/scratch/wz22/conda-envs/amd)
    2. abc (/scratch/wz22/conda-envs/abc)
    
    Select environments to migrate (comma-separated list, 'All' to migrate all):
    2

- In the initial section, the tool lists both the valid and invalid Conda environments found in the specified directory.
- Following this, it prompts the user to choose which Conda environments they want to migrate to ``$HOME``.

2. Migration process


.. code-block:: console

    Selected environments:
    abc:/scratch/wz22/conda-envs/abc
    Migrating and comparing environment: abc
    Source:      /scratch/wz22/conda-envs/abc
    Destination: /home/wz22/.conda/envs/abc

    Packages: 81
    Files: 5375
    Preparing transaction: done
    Verifying transaction: done
    Executing transaction: done
    #
    # To activate this environment, use
    #
    #     $ conda activate /home/wz22/.conda/envs/abc
    #
    # To deactivate an active environment, use
    #
    #     $ conda deactivate

    Old and New Environments are same

    Remove all packages in environment /scratch/wz22/conda-envs/abc:

    Successfully migrated and removed old environment: /scratch/wz22/conda-envs/abc

- This section provides a comprehensive breakdown of the selected environments chosen for migration.
- It initiates the process by cloning the old environment to ``$HOME``.
- Upon successful verification that the old and new environments match, the tool proceeds to clean up the old environment.

Migrate All Valid Environments in a Directory
---------------------------------------------

Additionally, the tool offers a convenient method to migrate all environments from a directory in ``$SCRATCH`` to ``$HOME``.

To migrate all valid Conda environments found in a directory:

.. code-block:: shell

    #conda-migrate -d /path/to/directory --all

    #Example
    conda-migrate -d /scratch/wz22/conda-envs --all


(Optional) Job Submission for Migrating Environments
----------------------------------------------------

For users dealing with a substantial number of environments, environments containing 
numerous files, or facing network connectivity challenges, an alternative option is available for 
migrating Conda environments through job submission.

Here's an example command that executes the tool as a job:

.. code-block:: console

    sbatch -c 10 -t 48:00:00 -J conda-migrate --wrap "conda-migrate -d /scratch/wz22/conda-envs --all"

This command initiates a background job on a compute node. It's designed to migrate all environments 
from a directory in ``$SCRATCH`` (``/scratch/wz22/conda-envs``) to a directory 
in ``$HOME`` (``/home/wz22/.conda/envs``).


.. admonition:: Contact us

    Kindly reach out to us if you need any assistance on jubail.support@nyu.edu
