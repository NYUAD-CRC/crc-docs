===================================
Connecting VS Code to HPC using SSH
===================================

Introduction
------------

.. important::
  Users are encouraged to use the Web version of VS Code (Code-Server) available on the HPC. The Code-server 
  can be found in the ``Interactive Apps`` section of the HPC Web Interface (https://ood.hpc.abudhabi.nyu.edu/)
    

This documentation provides step-by-step instructions on how to connect your local VS Code to 
a High-Performance Computing (HPC) system using SSH. By establishing an SSH connection, 
you can leverage the power of the HPC resources while utilizing the familiar and feature-rich 
VS Code editor.


The below steps also achieve the following:

- This will connect to the compute nodes and not the login nodes and hence prevent any overloads on login nodes.
- Eliminate the possibility of the non terminated vs code-related background processes which may cause login issues on the HPC

.. important::
  It is recommended to have enabled passwordless ssh on your private PC's for seamless experience. Find the guide here :ref:`Passwordless SSH <passwordless_ssh>`

Prerequisites
-------------

- A local installation of VS Code.
- Basic knowledge of SSH and working with remote systems.

Step 1: Modify SSH Config File
------------------------------

Add the following configuration to your SSH config file:

.. code-block:: bash

   Host hpc
     HostName jubail.abudhabi.nyu.edu
     User <NetID>
   
   Host hpc-job
     ForwardAgent yes
     StrictHostKeyChecking no
     UserKnownHostsFile=/dev/null
     ProxyCommand ssh hpc "/opt/slurm/default/bin/salloc --nodes=1 --ntasks-per-node=8 --time=9:00:00 /bin/bash -c 'nc \$SLURM_NODELIST 22'"
     User <NetID>

Replace ``<NetID>`` with your username. This configuration allows you to connect to the "hpc-job" host.

Step 2: Connect with VS Code Remote-SSH Extension
--------------------------------------------------

To remotely connect VS Code to one of the compute nodes, perform the following steps:

1. Install the Remote-SSH extension in your local VS Code instance.
2. Open the Command Palette in VS Code (press ``Ctrl+Shift+P`` or ``Cmd+Shift+P``).
3. Search for and select the ``Remote-SSH: Connect to Host`` option.
4. Choose the ``hpc-job`` host from the list of configured hosts.
5. VS Code will establish a remote SSH connection to the compute node.

