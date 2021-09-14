Singularity For Conda
=====================

A simple conda environment requires a lot of files to be created on file system. 
With a limit of 0.5 million files per user, more than a 100 thousand of that may be eaten just by one conda environment.

To address this situation, we offer users an option to use Singularity containers combined with overlay option.

Choose and copy ext3 file
--------------------------

Templates for ext3 filesystem files are located in ``/share/apps/NYUAD/dalma/overlay-fs-ext3``.

These templates have fixed disk size-so choose one that has an appropriate template based on name of the file. 
Please copy a chosen template to your own directory on ``/scratch``

Naming: ``overlay-0.5GB-300K.ext3`` means this file system will be able to hold up to ``0.5 GB``  and up to ``300K`` files

For example

.. code-block:: bash

    cd /scratch/$USER/<directory_for_project>
    cp /scratch/work/public/overlay-fs-ext3/overlay-0.5GB-200K.ext3.gz .
    gunzip overlay-0.5GB-300K.ext3.gz

Run container with overlay filesystem
-----------------------------------------

.. code-block:: bash

    module load all
    module load singularity/3.4.0

    ##Please choose appropriate singularity ext3 image at this location
    singularity exec  --overlay <chosen-file>.ext3 /share/apps/dalma/singularity-images/centos-8.2.2004.sif /bin/bash 

If you want to mount ext3 file as read and write, you can do that only with one process.

If you have more than one process reading from the given ext3 file, it shall be mounted as read-only.

For read-only mount, please specify ``:ro``

.. code-block:: bash

    singularity exec  --overlay <chosen-file>.ext3:ro /share/apps/dalma/singularity-images/centos-8.2.2004.sif /bin/bash

If you use GPUs please specify option ``--nv``

.. code-block:: bash

    singularity exec --nv  --overlay <chosen-file>.ext3 /share/apps/dalma/singularity-images/centos-8.2.2004.sif /bin/bash

More info on singularity exec `here <https://sylabs.io/guides/3.5/user-guide/cli/singularity_exec.html>`__

Write to overlay filesystem
---------------------------

You can write to directory /ext3 to create conda environment and install packages you need

While in container
------------------

.. code-block:: bash

    #install miniconda and choose NOT to initialize conda initialize when prompted (choose ``no`` for ``conda init``)
    #Give the path to installation 
    conda create -p /ext3/cenv python=3.7
    conda activate /ext3/cenv
    ## then use conda as usual
    #Close singularity
    exit


Job Submission
--------------

.. code-block:: bash

    #!/bin/bash
    #SBATCH --mem=8GB
    #SBATCH --time=1:00:00

    #Specify location of the overlay.ext3 file
    overlay_ext3=/scratch/$USER/<project_dir>/<chosen-file>.ext3

    singularity \
        exec --overlay $overlay_ext3:ro \
        /share/apps/dalma/singularity-images/centos-8.2.2004.sif  \
        /bin/bash -c "source /etc/miniconda3/bin/activate; \
                    conda activate /ext3/cenv; \
                    python <path_to_python_script_file>.py "
