Enabling Passwordless Authentication
====================================

.. _passwordless_ssh:


To enable passwordless authentication to HPC from your personal computer, please follow the steps below:

1. **Windows Users**:
   
   - Open the app ``Windows Powershell`` and generate a public key using the command ``ssh-keygen``.You may keep hitting enter when prompted for the paraphrase.
   - Copy the public key to the HPC system. A sample command is given below:
      
      .. code-block:: console

         type $env:USERPROFILE\.ssh\id_rsa.pub | ssh <NetID>@jubail.abudhabi.nyu.edu "cat >> .ssh/authorized_keys"

      Replace ``<NetID>`` with your NetID.   
    

2. **Linux and Mac Users**:
   
   - Open the terminal.
   - Generate an SSH key pair by running the following command
      
      .. code-block:: console

        ssh-keygen -t rsa

      Press Enter to accept the default settings and provide a passphrase if desired.

   - Copy the public key to the HPC system using the following command
      
      .. code-block:: console

        ssh-copy-id -i ~/.ssh/id_rsa.pub <NetID>@jubail.abudhabi.nyu.edu

      Replace ``<NetID>`` with your university NetID.

.. important::
   - It is recommended to generate SSH keys exclusively on private laptops or desktops. 
   - If a user replaces or loses their laptop, it is crucial to remove the old SSH key from Jubail to ensure security measures are in place. This precautionary step helps cover all potential scenarios and minimizes unauthorized access risks.
