File Transfer using rsync
=========================

For replicating datasets between the HPC clusters and your workstation, or between two filesystems on an HPC cluster, rsync offers powerful functionality beyond that of cp or scp commands. With rsync you can copy directories between your workstation and the HPC clusters - or between different filesystems - in such a way that permission and file modification timestamps are preserved, and that only files which have changed are transferred.

 

.. admonition:: Basic Usage of rsync

    .. code-block:: bash

        rsync [options] source [source] destination

Where source is a list of one or more source files or directories to copy and destination is a directory into which to copy source. 

Commonly useful options are:

* ``-a`` "Archive" mode - permissions and timestamps of the source are replicated at the destination.
* ``-v`` "Verbose".
* ``-n``  "dry run" - don't actually do anything, just indicate what would be done.
* ``-C`` "follow CVS ignore conventions" 

.. admonition:: Before Actually Copying Files

    rsync treats destination in different ways:a new name for the copy of source, a parent directory into which to copy source, or a parent directory into which to place the contents of source, depending on the exact context of the command. For this reason, it is highly advisable to first run rsync with -n and -v to see exactly what rsync will do before issuing the "real" command, eg:

    .. admonition:: Dry Run First!

        .. code-block:: bash
            
            rsync -nav source destination
            rsync -av source destination

For detailed information about rsync, type ``man rsync`` at the command line.

Some examples of rsync usage
----------------------------

To replicate in your /scratch area a directory tree you have saved in /home

.. code-block:: bash

    $ cd /home/$USER/
    $ ls -F
    my_input_data/
    $ rsync -nav my_input_data /scratch/$USER/my_run_dir
    building file list ... done
    my_input_data/file1
    my_input_data/file2
        
    $ rsync -av my_input_data /scratch/$USER/my_run_dir
    building file list ... done
    my_input_data/file1
    my_input_data/file2
        
    $ ls -F /scratch/$USER/my_run_dir
    my_input_data/

There is now a copy of my_input_data directory under ``/scratch/$USER/my_run_dir``.  

**If you append / to source, rsync will copy the contents of source rather than the source directory itself**

.. code-block:: bash

    $ cd /home/$USER/
    $ ls -F
    my_input_data/
    $ rsync -nav my_input_data/ /scratch/$USER/my_run_dir
    building file list ... done
    file1
    file2
        
    $ rsync -av my_input_data/ /scratch/$USER/my_run_dir
    building file list ... done
    file1
    file2
        
    $ ls -F /scratch/$USER/my_run_dir
    file1
    file2
 

The host name followed by a colon tells rsync that source or destination is on another host. If your username on the other host is different from the username on the current host, you can specify the remote username with username@remotehost: as following:

.. code-block:: bash

    $ ls -F
    my_input_data/
    $ rsync -av my_input_data <your-net-id>@jubail.abudhabi.nyu.edu:/scratch/<your-net-id>/my_run_dir
    ### For Example ###
    $ rsync -av my_input_data wz22@jubail.abudhabi.nyu.edu:/scratch/wz22/my_run_dir

To copy in the other direction, from ``/scratch`` on HPC to your workstation.

.. code-block:: bash

    $ hostname
    my_workstation
    $ rsync -av <your-net-id>@jubail.abudhabi.nyu.edu:/scratch/<your-net-id>/my_run_dir my_results
    ### For Example ###
    $ rsync -av wz22@jubail.abudhabi.nyu.edu:/scratch/wz22/my_run_dir my_results
    $ ls my_results

Only those files with modifications will be copired from the HPC to your workstation.

Ignoring certain files
----------------------

The ``-C`` option tells rsync to follow CVS conventions about ignoring certain files.The conventions are described fully in the man page (man rsync) but in summary, when ``-C`` is used the following files are ignored  or any file or directory whose name matches any of these mentioned below are ignored:

.. code-block:: bash

    RCS SCCS CVS CVS.adm RCSLOG cvslog.* tags TAGS .make.state .nse_depinfo *~ #* .#* ,* _$* *$ *.old *.bak *.BAK *.orig *.rej .del-* *.a *.olb *.o *.obj *.so *.exe *.Z *.elc *.ln core .svn/

For example, when copying a tree of source code, you probably want the .c, .f and .h files but not the .o files, to define your own ignored rsync files use any of those methods.

* Any file whose name matches a pattern listed in the environment variable ``CVSIGNORE``. 
	* This environment variable takes a list of patterns separated by spaces, such as the default list above. 
	* When defining ``CVSIGNORE`` you will need to enclose the definition in quotation marks.
	* For example to skip Fortran output to unnamed unit numbers (whose files have names like ``fort.99``) and netcdf files whose name ends in ``intermediate.nc``, set ``CVSIGNORE`` as follows (note that this syntax is for ``BASH``)

.. code-block:: bash

    $ export CVSIGNORE="fort.?? *.intermediate.nc" 
    
    
 
* Or any file whose name matches a pattern listed in the file $HOME/.cvsignore, or in a file named .cvsignore within a directory being copied. 
	* This file has contents as per $CVSIGNORE, but with one pattern per line, for example:

.. code-block:: bash

    $ cat .cvsignore
    fort.??
    *.intermediate.nc
