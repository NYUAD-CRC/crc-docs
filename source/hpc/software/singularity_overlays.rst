Singularity Overlays
====================

Efficient handling of large input and output (I/O) volumes is crucial for scientific workflows, 
particularly those involving tasks like image processing. However, when dealing with a multitude of 
files (e.g., Python packages comprising numerous small files), this can effect workflow speed and even impact 
the overall filesystem performance for other users.

To address these challenges, a persistent overlay serves as an empty writable filesystem that gets mounted 
within the Singularity container during runtime. It preserves any modifications made to its filesystem while 
the container is active. While the overlay appears as just another directory from the container's perspective, 
the HPC filesystem treats it as a single file, enabling all I/O operations to be applied to this consolidated file. 
This key aspect of overlays reduces the burden on the HPC filesystem by managing metadata solely for the overlay 
file instead of individual files within the overlay.

An Overlay is simply a directory or a filesystem image which sits on top of a Singularity container.

The user can make benefit of the overlays in any of the following ways:

- You have too many conda environments eating up your number of files limit
- You have a data set consisting of a large number of small files
- You would like to share your environments (R,conda,etc) with your collaborators with no installation required.
    

Creating an Overlay
-------------------

To create an overlay, use the ``create-overlay`` command. This command takes the size of the overlay in 
megabytes and the number of files as arguments. The usage is as follows:

.. code-block:: console

    create-overlay -s <size-in-Megabytes> -n <number-of-files-in-1000's> [ -o <name-of-overlay> ]

    # Example:
    create-overlay -s 500 -n 700

The above example will create an overlay by the name ``overlay-500M-700K.ext3`` of 500MB capacity with a 
number of file limit of 700K. 
The overlay will be named ``overlay-<size>M-<numfiles>K.ext3`` by default. It can be customized by specifying
the name with ``-o`` argument.

Mounting an Overlay
-------------------

To mount an overlay, use the ``mount-overlay`` command. This command takes the name of the overlay file 
as an argument. You can specify multiple overlays by using the ``-o`` option multiple times. 
The usage is as follows:

.. code-block:: bash

    mount-overlay -o <name-of-overlay> [-o <name-of-overlay> ...]

    # Example:
    mount-overlay -o overlay1.ext3 -o overlay2.ext3

The above example will mount the overlays ``overlay1.ext3`` and ``overlay2.ext3`` simultaneously.

.. note::
    Please note that when mounting or running multiple overlays, it is important to be aware that only the first overlay 
    specified will be mounted as writable, while the remaining overlays will be mounted as read-only. 
    This means that any changes made to the first overlay will be retained, but modifications to the 
    subsequent overlays will not be allowed.

Running with an Overlay
-----------------------

To run a command with the overlay mounted, use the ``run-overlay`` command. This command takes the 
name of the overlay file and a command file as arguments. You can specify multiple overlays by 
using the ``-o`` option multiple times. The usage is as follows:

.. code-block:: bash

    run-overlay -o <name-of-overlay> [-o <name-of-overlay> ...] -f <command-file>

    # Example:
    run-overlay -o overlay1.ext3 -o overlay2.ext3 -f file1.txt

The above example will run the commands present in ``file1.txt`` with the overlays ``overlay1.ext3`` 
and ``overlay2.ext3`` mounted simultaneously.


.. note::
    If you need finer control over the overlay, you can directly use the underlying Singularity 
    commands such as ``singularity shell``, ``singularity exec``, etc. For example, you can mount multiple overlays 
    using the ``singularity shell`` command as follows:

    .. code-block:: bash

        singularity shell --overlay overlay1.ext3 --overlay overlay2.ext3 /share/apps/admin/singularity-images/centos-8.2.2004.sif

    This will start an interactive shell within the container with both overlays mounted. From there, you can manually 
    perform operations and run commands within the overlay filesystem.

    Similarly, you can use the ``singularity exec`` command to run a specific command with multiple overlays. For example:

    .. code-block:: bash

        singularity exec --overlay overlay1.ext3 --overlay overlay2.ext3 /share/apps/admin/singularity-images/centos-8.2.2004.sif command



    Using these commands directly gives you more control and flexibility over the overlays, but it requires manual 
    setup and execution. The ``mount-overlay`` and ``run-overlay`` commands provided earlier are simplified wrappers 
    that handle the common tasks automatically for you.

Analogy: Understanding Overlays
-------------------------------

To help understand overlays, let's consider an analogy. Think of the Singularity container as your personal workspace, and the overlays as additional layers on your workspace.

- The base container is your initial workspace, containing all the tools and resources you need.
- Each overlay represents a specific task or project, with its own set of files and modifications.
- Mounting an overlay is like placing a transparent sheet on top of your workspace. It adds new files and modifications without altering the original workspace.
- Running a command with an overlay is like working on your workspace with the transparent sheet in place. The changes made by the command are temporary and isolated within the overlay, leaving your original workspace intact.

You can also think of the Singularity container as your personal computer (PC), and the overlay as 
an external hard disk or a pendrive.

When you run a Singularity container with an overlay with the ``mount-overlay`` 
or ``run-overlay`` command, it's like logging into your container PC and 
plugging in the overlay pendrive. Just like you can navigate your files in ``/scratch`` and ``/home``, 
you can also access files in the overlay by navigating to the desired folders.

You can write files and create directories in the overlay (for example ``/data`` , ``/env`` , ``/conda`` etc). 
Any files/directories created outside ``/scratch`` and ``/home`` will reside inside the overlay filesystem. This allows 
you to store environments, datasets, and other files specific to your needs.

.. code-block:: bash

    mkdir /data

By using overlays, you can keep your base container clean and separate different tasks or projects, making it easier to manage and share your work with others.

Sharing the Overlay
-------------------

The overlay can be shared with your collaborators to provide them with your working environment and 
datasets. By sharing the overlay file, you are essentially sharing everything that has been 
written into the overlay directories (``/data`` , ``/conda`` etc).

Job Submission
--------------

To submit a job that uses the overlay, you can include the necessary commands in a job script. 
Here's an example:

.. code-block:: bash

    #!/bin/bash
    #SBATCH --mem=8GB
    #SBATCH --time=1:00:00

    run-overlay -o overlay1.ext3 -o overlay2.ext3 -f file.txt

This script will run the commands present in ``file.txt`` with the overlays ``overlay1.ext3`` 
and ``overlay2.ext3`` mounted simultaneously.

An example file.txt is given below:

.. code-block:: bash

    source ~/.bashrc
    conda activate /opt/conda-envs/myenv
    python abc.py


If you need finer control over the overlay or want to use the underlying Singularity 
commands directly, you can modify the job script as follows:

.. code-block:: bash

    #!/bin/bash
    #SBATCH --mem=8GB
    #SBATCH --time=1:00:00

    #Specify location of the overlay.ext3 file
    overlay_ext3=/scratch/$USER/<project_dir>/<chosen-file>.ext3

    singularity \
        exec --overlay $overlay_ext3:ro \
        /share/apps/jubail/singularity-images/centos-8.2.2004.sif  \
        /bin/bash -c "source ~/.bashrc; \
                    conda activate /opt/conda-envs/myenv; \
                    python <path_to_python_script_file>.py "


Note that in this case, you will need to manually mount the overlays  and use the ``singularity exec`` 
command to run the desired command. This provides finer control over the overlay setup and execution.

Remember to adjust the resource requirements (e.g., memory and time) in the job script 
according to your specific needs.


