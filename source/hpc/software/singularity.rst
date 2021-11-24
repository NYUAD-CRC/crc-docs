Singularity Containers
======================

What is a Container?
----------------------

A container allows you to stick an application and all of its dependencies into a single package. This makes your application portable, shareable, and reproducible.

Containers foster portability and reproducibility because they package ALL of an applications dependencies, including its own tiny operating system!

This means your application won't break when you port it to a new environment. Your app brings its environment with it.

Here are some examples of things you can do with containers:

* Package an analysis pipeline so that it runs on your laptop, in the cloud, and in a high performance computing (HPC) environment to produce the same result.
* Publish a paper and include a link to a container with all of the data and software that you used so that others can easily reproduce your results.
* Install and run an application that requires a complicated stack of dependencies with a few keystrokes.
* Create a pipeline or complex workflow where each individual program is meant to run on a different operating system.

How do containers differ from virtual machines (VMs)
----------------------------------------------------

Containers and VMs are both types of virtualization. But it's important to understand the differences between the two and know when to use each.

Virtual Machines install every last bit of an operating system (OS) right down to the core software that allows the OS to control the hardware (called the kernel). This means that VMs:
* Are complete in the sense that you can use a VM to interact with your computer via a different OS.
* Are extremely flexible. For instance you an install a Windows VM on a Mac using software like VirtualBox.
* Are slow and resource hungry. Every time you start a VM it has to bring up an entirely new OS.

Containers share a kernel with the host OS. This means that Containers:
* Are less flexible than VMs. For example, a Linux container must be run on a Linux host OS. (Although you can mix and match distributions.) In practice, containers are only extensively developed on Linux.
* Are much faster and lighter weight than VMs. A container may be just a few MB.
* Start and stop quickly and are suitable for running single apps.

Because of their differences, VMs and containers serve different purposes and should be favoured under different circumstances.

* VMs are good for long running interactive sessions where you may want to use several different applications. (Checking email on Outlook and using Microsoft Word and Excel).
* Containers are better suited to running one or two applications, often non-interactively, in their own custom environments.

Docker
------

`Docker <https://www.docker.com/>`__ is currently the most widely used container software. It has several strengths and weaknesses that make it a good choice for some projects but not for others.

**Philosophy**

Docker is built for running multiple containers on a single system and it allows containers to share common software features for efficiency. It also seeks to fully isolate each container from all other containers and from the host system.

Docker assumes that you will be a root user. Or that it will be OK for you to elevate your privileges if you are not a root user. See https://docs.docker.com/engine/security/security/#docker-daemon-attack-surface for details.

**Strengths**

- Mature software with a large user community
- `Docker Hub <https://hub.docker.com/>`__
    - A place to build and host your containers
    - Fully integrated into core Docker
    - Over 100,000 pre-built containers
    - Provides an ecosystem for container orchestration
- Rich feature set


**Weaknesses**

- Difficult to learn
    - Hidden innards 
    - Complex container model (layers)
- Not architected with security in mind
- Not built for HPC (but good for cloud) 


Docker shines for DevOPs teams providing cloud-native micro-services to users.

Singularity
-----------

`Singularity <http://singularity.lbl.gov/>`__ is a relatively new container software invented by Greg Kurtzer while at Lawrence Berkley National labs and now developed by his company `Sylabs <https://sylabs.io>`__.  It was developed with security, scientific software, and HPC systems in mind.  

**Philosophy**

Singularity assumes (`more or less <http://containers-ftw.org/SCI-F/>`__) that each application will have its own container.  It does not seek to fully isolate containers from one another or the host system. 
Singularity assumes that you will have a build system where you are the root user, but that you will also have a production system where you may or may not be the root user. 

**Strengths**

- Easy to learn and use (relatively speaking)
- Approved for HPC (`installed on some of the biggest HPC systems in the world <https://singularity.hpcng.org/>`__)
- Can convert Docker containers to Singularity and run containers directly from Docker Hub
- `Singularity Container Services <https://cloud.sylabs.io/home>`__
    - A place to build and share your containers securely

**Weaknesses**

- Younger and less mature than Docker
- Smaller user community (as of now)
- Under active development (must keep up with new changes)

Singularity shines for scientific software running in an HPC environent.


Steps to use a Container
------------------------

1. create or pull an existing container

	- Singularity containers are identified with an extension ``example.sif``
	- Singularity containers are created from definition files whose extension is ``example.def``
	- use ``singularity pull`` to get an existing container from one of the hubs available.
	
2. Launch the container

	- Run the container using `singularity shell <https://sylabs.io/guides/3.1/user-guide/cli/singularity_shell.html>`__ or `singularity exec <https://sylabs.io/guides/3.5/user-guide/cli/singularity_exec.html>`__ or launch it simply like an executable (``./example.sif``)
	

Using docker and singularity images from existing container libraries
---------------------------------------------------------------------

**List of useful container libraries**

1. Docker Based Container Libraries

	- Docker Hub: https://hub.docker.com/

	- Nvidia GPU-Accelerated Containers (NGC): https://ngc.nvidia.com/

	- Quay (Bioinformatics): https://quay.io/ or https://biocontainers.pro/#/registry
	
2. Singularity Container Library

	- Singularity Library: https://cloud.sylabs.io/library

**Example Usage**

.. code-block:: bash
	
	# Load the singularity container
	module load singularity
	
	# pull the docker/singularity image from hub
	# pulls the latest GCC container and saves in current working directory
	singularity pull docker://gcc                      
	
If you prefer to pull a specific GCC version, look at the `available tags <https://hub.docker.com/r/library/gcc/tags/>`__ for the specific container and append the tag version to the end of the container name. For example, if you need to pull the ``GCC v 5.3.0``

.. code-block:: bash


	singularity pull docker://gcc:8.3.0
	
You can also pull the images to a directory of your choosing (assuming you have write permission) by setting the variables ``SINGULARITY_CACHEDIR`` and ``SINGULARITY_TMPDIR``. For instance,

.. code-block:: bash

 	export SINGULARITY_CACHEDIR=$TMPDIR 
  export SINGULARITY_TMPDIR=$TMPDIR
  
.. note::
  While pulling the containers, pay attention to the home directory as the cached image blobs will be saved in ${HOME}/.singularity.
  Since the home directory has a limited amount of space, this can fill up quite easily. Users can change where the files will be cached by setting SINGULARITY_CACHEDIR and SINGULARITY_TMPDIR environment variables.
  
  
Creating Singularity containers
-------------------------------

To use Singularity on the HPC, you either need to create your own Singularity container, or use one created by someone else.You have several options to build Singularity containers:

- You can build small and medium sized containers on HPC using the ``--remote`` option. In a nutshell, you must log in and generate a token on the `Singularity Container Services <https://cloud.sylabs.io/auth>`__ and use the command line to copy that token into your environment (using the command ``singularity remote login``). Once you've done that, the ``--remote option`` will allow you to build containers using the Sylabs remote builder.
- If you have a Linux system to which you have root (admin) access, you can install Singularity and build your Singularity container there.
- If you have a very recent Linux system (like Ubuntu >=18) you can build Singularity containers without root access using the `--fakeroot option <https://sylabs.io/guides/3.4/user-guide/fakeroot.html#build>`__.
- If you don't have a Linux system you could easily install one in a virtual machine using software like `VirtualBox <https://www.virtualbox.org/>`__, `Vagrant <https://www.vagrantup.com/>`__, `VMware <http://www.vmware.com/>`__, or `Parallels <http://www.parallels.com/>`__. (If you use a virtual machine be sure to allocate at least 2GB of memory or some of your builds may fail with out of memory errors.)
- You can allocate a cloud instance, to which you will have root access. Install Singularity and build your Singularity container there. 

You can find information about installing Singularity on Linux `here <https://sylabs.io/guides/latest/user-guide/quick_start.html#quick-installation-steps>`__.

In addition to your own Linux environment, you will also need a definition file to build a Singularity container from scratch. You can find some simple definition files for a variety of Linux distributions in the `example <https://github.com/hpcng/singularity/tree/master/examples>`__ directory of the source code. Detailed documentation about building Singularity container images is available at the `Singularity website <https://sylabs.io/guides/latest/user-guide/>`__. 

Singularity Containers from scratch
-----------------------------------

1. Create a definition file (``example.def``)

	Detailed documentation for a Singularity definition file is `here <https://sylabs.io/guides/3.3/user-guide/definition_files.html>`__. But below is a simple example to get you started.
	
	.. code-block:: bash
	
		Bootstrap: docker
 
  
		From: continuumio/miniconda3
 
  

		%labels
  
		maintainer "Name" <email address>
 
  

		%post
  
		apt-get update && apt-get install -y git
  
		# Conda install stringtie

		conda install -c bioconda stringtie 
	
	
	- The header includes the Bootstrap and the label of the container.

	- Most of the definition files use docker as their bootstrap as docker library is more robust and well maintained.

	- This is using an existing docker image for miniconda (Python 3) available from https://hub.docker.com/r/continuumio/miniconda3

	- ``%post`` section is any modifications or additions the user can make to the original container - in this case we are adding stringtie package to the container.
	
2. Once you have the definition file ready, You can build the sandox (writable directory), where you can log in and install anything inside the sandbox. Note that this requires sudo/root privileges. 
**If you do not have sudo/root privileges, please proceed to step number 3 or use a machine where you have the sudo or root privileges.**


	.. code-block:: bash
	
		# Load the singularity module
		module load singularity
		
		#singularity build --sandbox <name_you_want> <definition_file.def>
		#example
		singularity build --sandbox abc example.def
		
	This will create a sandbox (writable directory) where you can log in and install anything you want after you ``shell`` into the sandox. Note that this requires root/sudo privileges.
	
	.. code-block:: bash
	
		#singularity shell -w <name_of_the_sanbox>
		singularity shell -w abc
		
	Once you have installed the required packages into the sandox, you can exit and build the container by following the next step.
	
3. Build the container

	- This will create a ``.sif`` file which is the container
	
	.. code-block:: bash
		
		#If building with definition file (``example.def``)
		#singularity build <name_you_want>.sif <definition_file.def> 	
		singularity build mycontainer.sif example.def
		
		#If building with a sandbox
		#singularity build <name_you_want>.sif <name_of_the_sandbox>
		singularity build mycontainer.sif abc
		
		
		
	

