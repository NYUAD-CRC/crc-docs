How to use the DDT Debugger
===========================

Users can use Allinea DDT debugger to debug serial, multi-threaded or MPI applications submitted to Dalma.

Due to X-Forwarding restrictions in the cluster, the jobs have to be submitted to queues and DDT started in the login nodes and then attach the debugger to the running process in the remote node.

 

Step-by-step guide
------------------

1. Attaching to a running process
    In the login node:

    * Compile your application with debugging enabled (e.g. ``-g`` flag)
    * Submit the application using  ``sbatch``
    * Once the app is running, use the command ``squeue`` to retrieve the NODELIST...You will need the head node name to instruct DDT where to connect to

    Load the allinea module and run ``ddt``

    .. important::
        You will need to ssh Dalma enabling X11 Forwarding:  ``ssh -X <netid>@dalma.abudhabi.nyu.edu``

    .. code-block:: bash
        
        $ module load allinea
        $ ddt 
    

    * Click on the ``ATTACH`` button and ``choose hosts`` to add the head node where the job is running ( see Figure below )

    .. image:: /hpc/img/ddt1.png



    * If it is an MPI app, attach to the ``srun`` process
    

2. Submitting an MPI application from within DDT
    In the login node:

    * Compile your application with debugging enabled (e.g. ``-g`` flag)
    * Copy your submission script and rename it with extension ***.qtf**
        * you can also use the template file in ``/share/apps/NYUAD/allinea/5.0/templates/slurm.qtf``
    * Load the allinea module and run ``ddt``

    

    .. important::
        You will need to ssh Dalma enabling X11 Forwarding: ``ssh -X <netid>@dalma.abudhabi.nyu.edu``

    .. code-block:: bash

        $ module load allinea
        $ ddt 

    * Click on **RUN**
    * Select your application to run 
    * Enable MPI and be sure the **SLURM(generic)** is selected ... Click on Change  and in the next window select the **submission template file** to the ***.qtf** file you just created
    
    .. image:: /hpc/img/ddt2.png

    * Finally set the MPI params (Number of Processes,etc) and hit RUN

    .. image:: /hpc/img/ddt3.png

