Singularity Overlays
====================

An Overlay is a directory or a filesystem image which sits on top of a singularity container.

The user can make benefit of the overlays in any of the following ways:

- You have too many conda environments eating up your number of files limit
- You have a data set consisting of a large number of small files
- You would like to share your environments (R,conda,etc) with your collaborators with no installation required.

This process has the following steps which are explained in more details later:

- Create an overlay of the desired size
- Use a singularity conatiner to get into the overlay
- Create your enviornments or copy your dataset in the ``/opt`` directory
- exit the singularity container

.. note::
    You can think of an overlay as an external filesystem image to which you would be able to write
    using singularity 


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


.. admonition:: Analogy: To make things more understandable

    The command you use to get into the overlay is as follows:

    .. code-block:: bash

        singularity shell  --overlay <chosen-file>.ext3 /share/apps/admin/singularity-images/centos-8.2.2004.sif

    if you look closely it contains paths to two files

    - **The Container**:  ``/share/apps/admin/singularity-images/centos-8.2.2004.sif``
    - **The Overlay** :  ``<chosen-file>.ext3``
    
    You could think of the container as your personal computer (PC) and the overlay as an external hard disk or a pen drive. 

    The thing about this conatiner PC is, that you wouldn't be able to write any files to it but you can write files to your pen drive (the overlay). You have also plugged in your /home and /scratch and hence these are also available from inside the container pc.

    Each of these pendrives have their own capacity (quota). You could potentially create an overlay pendrive of the capacity (quota) you like and use it store your files(data).

    When you run the above command, you basically login to your container PC and plug in these pendrives. It looks very similar to as compared to when you log in to Jubail. You could navigate through your files in /scratch and /home as usual. For files in the overlay you can cd to the desired folder and view the files in a similar manner.

    For example:

    .. code-block:: bash

        cd /opt/data
        ls -lrt data

    For transferring data between any of these pendrives (``/home``, ``/scratch`` , ``overlay`` etc), you could use the 
    usual ``cp``, ``mv`` commands. Any files/directories created outside ``/scratch``, ``/home`` (eg: ``/data`` or ``/opt``)
    will reside inside the overlay filesystem that can only be accessed by plugging in the overlay filesystem using the
    command mentioned above. 

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

You can write to the directory ``/opt`` to create conda environment and install packages that you need.All the environments and datasets written from inside the container
to ``opt`` are actually witten into the overlay which has been created.

.. note::
    It should be noted that you can write to any of the directories and create your own directories in
    the overlay as well:
    
    for example:
    
    .. code-block:: bash

        mkdir -p /data
        mkdir -p /conda

    The above commands will create ``/data`` and ``/conda`` directories, which will be part of the overlay itself.
    In Short, anything written inside the overlay except in ``/scratch`` and ``/home`` will go inside the overlay
    and the files/directories written in ``/scratch`` and ``/home``, will stay there and wouldn't be part of the 
    overlay.

While in container
------------------

**Creating a Conda Environment**

You can create a conda environment in /opt as follows:

.. code-block:: bash

    module load miniconda
    source ~/.bashrc
    
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
to ``opt`` are actually witten into the overlay which has been created. Hence, the sharing of an overlay with a 
collaborator is equivalent to sharing the working environment with the datasets, also it means essentially sharing whatever
is written into the overlay directory ``/opt``.


Job Submission
--------------

A sample job script can look as follows. 

Note that all the commands to be executed within the container are part of the ``/bin/bash -c "<commands to be executed>"`` 

.. code-block:: bash

    #!/bin/bash
    #SBATCH --mem=8GB
    #SBATCH --time=1:00:00

    #Specify location of the overlay.ext3 file
    overlay_ext3=/scratch/wz22/overlay-500M-700K.ext3

    singularity \
        exec --nv --overlay $overlay_ext3:ro \
        /share/apps/admin/singularity-images/centos-8.2.2004.sif  \
        /bin/bash -c "source ~/.bashrc; \
                    conda activate /opt/conda-envs/myenv; \
                    python <path_to_python_script_file>.py "
