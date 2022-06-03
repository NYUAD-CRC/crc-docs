Singularity Overlays
====================

An Overlay is a directory or a filesystem image which sits on top of a singularity container.

The user can make benefit of the overlays in any of the following ways:

- You have too many conda environments eating up your number of files limit
- You have a datset consisting of a large number of small files
- You would like to share your environments (R,conda,etc) with your collaborators with no installation required.

This process has the following steps which are explained in detailed later:

- Create an overlay of the desired size
- Use a singularity conatiner to get into the overlay
- Create your enviornments or copy your dataset in the ``/opt`` directory
- exit the singularity container

Creating an Overlay
-------------------

The script ``overlay.sh`` facilitates this process of creating an overlay based on your needs.
The command ``overlay.sh`` takes two arguments ``size of the overlay (in MB)`` and ``number of files`` 
in the overlay (in 1000's). The usage is as follows:

.. code-block:: bash

    #overlay.sh <size> <num of files>

    #example:
    overlay.sh 500 700

The above command will create an overlay with ``500MB`` capacity and number of files capacity ``700K``
by the name ``overlay-500M-700K.ext3`` in the directory from which the command was issued.

Run container with overlay filesystem
-----------------------------------------

.. code-block:: bash

    ##Please choose appropriate singularity ext3 image at this location
    #singularity shell  --overlay <chosen-file>.ext3 /share/apps/admin/singularity-images/centos-8.2.2004.sif  

    #example:
    singularity shell  --overlay overlay-500M-700K.ext3 /share/apps/admin/singularity-images/centos-8.2.2004.sif

If you want to mount ext3 file as read and write, you can do that only with one process.

If you have more than one process reading from the given ext3 file, it shall be mounted as read-only.

For read-only mount, please specify ``:ro``

.. code-block:: bash

    singularity shell  --overlay <chosen-file>.ext3:ro /share/apps/admin/singularity-images/centos-8.2.2004.sif

If you use GPUs please specify option ``--nv``

.. code-block:: bash

    singularity shell --nv  --overlay <chosen-file>.ext3 /share/apps/admin/singularity-images/centos-8.2.2004.sif 

More info on singularuty shell `here <https://sylabs.io/guides/3.1/user-guide/cli/singularity_shell.html>`__

You can also use ``singularity exec`` to run the container with overlay filesystem:

.. code-block:: bash

    singularity exec --overlay <chosen-file>.ext3 /share/apps/admin/singularity-images/centos-8.2.2004.sif /bin/bash


More info on singularity exec `here <https://sylabs.io/guides/3.5/user-guide/cli/singularity_exec.html>`__

Write to overlay filesystem
---------------------------

You can write to the directory ``/opt`` to create conda environment and install packages you need.All the environments and datasets written from inside the container
to ``opt`` are actually witten into the overlay which has been created.

While in container
------------------

**Creating a Conda Environment**

You can create a conda environment in /opt as follows:

.. code-block:: bash

    
    #Create new environments in /opt  
    conda create -p /opt/conda-envs/myenv
    
    conda activate /opt/conda-envs/myenv
    ## then use conda as usual

    #Close singularity
    exit


**Transferring Datasets**

You can also copy the Dataset from your local folder and place it under ``/opt``.

.. code-block :: bash

    #Example:
    mkdir -p /opt/data
    cp -r /scratch/wz22/dataset.zip /opt/data/.
    unzip dataset.zip

.. note::
    It is recommended to copy the datasets to the overlay in compressed formats (zip or tar) and then extract it 
    in the overlay.


Sharing the Overlay
-------------------
 
The overlay can also be shared with your collaborators. All the environments and datasets written from inside the container
to ``opt`` are actually witten into the overlay which has been created. Hence, the sharing an overlay with a 
collaborator is equivalent to sharing the working environment with the datasets etc, essentially sharing whatever
is written into the overlay directory ``/opt``.


Job Submission
--------------

A smaple job script can look as follows. Note that all the commands to be 
executed within the container are part of the ``/bin/bash -c "<commands to be executed>"`` 

.. code-block:: bash

    #!/bin/bash
    #SBATCH --mem=8GB
    #SBATCH --time=1:00:00

    #Specify location of the overlay.ext3 file
    overlay_ext3=/scratch/wz22/overlay-500M-700K.ext3

    singularity \
        exec --nv --overlay $overlay_ext3:ro \
        /share/apps/jubail/singularity-images/centos-8.2.2004.sif  \
        /bin/bash -c "source ~/.bashrc; \
                    conda activate /opt/conda-envs/myenv; \
                    python <path_to_python_script_file>.py "
