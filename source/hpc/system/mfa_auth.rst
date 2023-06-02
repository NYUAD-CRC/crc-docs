HPC Access with MFA Authentication
==================================

Introduction
------------
This following sections provide instructions for accessing the High-Performance Computing (HPC) system 
with multifactor DUO authentication enabled. Users will be prompted to authenticate themselves using 
DUO during the login process. Additionally, steps are provided for enabling passwordless authentication by copying 
SSH keys for Windows, Linux, and Mac users to override the multifactor authentication. 

.. Lastly, this guide includes instructions for modifying SSH configurations to incorporate control masters. 

.. Important::
    Users who have already set up passwordless authentication by copying their SSH keys will not be 
    affected by the multifactor DUO authentication. Passwordless authentication allows users to log 
    in to the HPC system without entering a password. Instead, authentication is based on the presence 
    of a valid SSH key on the user's local machine and the corresponding public key stored on the 
    HPC system.

MFA Authentication
------------------

Starting from now, accessing the HPC system requires multifactor DUO authentication. Upon login, 
users will be prompted to provide additional authentication through DUO. The following options will 
be presented:

1. **DUO Push to +XXX XX XXX 7777**
   
   Select this option if you want to receive a DUO Push notification on your mobile device. Confirm the login request on your device to proceed.

2. **SMS passcodes to +XXX XX XXX 7777**
   
   Select this option if you want to receive an SMS passcode on your registered phone number. Enter the passcode provided to proceed.

A sample example is given below:

.. code-block:: console

    Duo two-factor login for wz22

    Enter a passcode or select one of the following options:

    1. Duo Push to +XXX XX XXX 7777
    2. SMS passcodes to +XXX XX XXX 7777

    Passcode or option (1-2): 1
    password for wz22:

.. _passwordless_ssh:

Enabling Passwordless Authentication
------------------------------------
To enable passwordless authentication and override the multifactor DUO authentication, follow the steps below based on your operating system:

1. Windows Users:
   
   - Open the app ``Windows Powershell`` and generate a public key using the command ``ssh-keygen``.You may keep hitting enter when prompted for the paraphrase.
   - Copy the public key to the HPC system. A sample command is given below:
      
      .. code-block:: console

         type $env:USERPROFILE\.ssh\id_rsa.pub | ssh <NetID>@jubail.abudhabi.nyu.edu "cat >> .ssh/authorized_keys"

      Replace ``<NetID>`` with your NetID.   
    

2. Linux and Mac Users:
   
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
   It is recommended to generate SSH keys exclusively on private laptops or desktops. 
   If a user replaces or loses their laptop, it is crucial to remove the old SSH key from Jubail to ensure 
   security measures are in place. This precautionary step helps cover all potential scenarios and minimizes 
   unauthorized access risks.

.. SSH Configuration with Control Masters (Optional)
.. -------------------------------------------------
   Users can modify their SSH configurations to incorporate control masters, which allow for more efficient SSH connections. Control masters create a persistent connection to the remote host, eliminating the need to establish a new connection for each subsequent SSH session.

   To set up control masters, follow the steps below:

   1. Create the control masters directory:
      Run the following command to create the directory where control masters will be stored
      
      ::

         mkdir ~/.ssh/controlmasters

   2. Edit the SSH configuration file:
      Edit the SSH configuration file located at ``~/.ssh/config`` using a text editor
      
      ::

         nano ~/.ssh/config

   3. Add the following configuration for the HPC system:
      Insert the following lines into the SSH configuration file
      
      ::

         Host jubail.abudhabi.nyu.edu
         IdentitiesOnly yes
         ControlPath ~/.ssh/controlmasters/%r@%h:%p
         ControlMaster auto
         ControlPersist 3h

      This configuration ensures that SSH connections to ``jubail.abudhabi.nyu.edu`` will use control masters, providing faster and more efficient connections. The ``ControlPersist`` directive specifies that the control master connection will persist for 3 hours.



Explanation
-----------
.. - Control masters, introduced in the SSH protocol, allow for the creation of persistent SSH connections 
  to remote hosts. By utilizing control masters, subsequent SSH sessions to the same host can reuse the 
  existing connection, resulting in faster and more efficient connections. The SSH configuration 
  specified in this document enables control masters for connections to the HPC system, 
  improving the overall SSH experience.

- Passwordless authentication relies on the use of SSH keys for authentication 
  instead of passwords. Users generate a public-private key pair, where the public key is stored on 
  the HPC system and the private key remains on the user's local machine. During authentication, 
  the private key is used to prove the user's identity without requiring a password. This method is 
  more secure and convenient than traditional password-based authentication.
- Users who have already set up passwordless authentication by copying their SSH keys to the HPC system are not required to go through the multifactor DUO authentication process. Since passwordless authentication relies on the possession of a valid SSH key, it provides an inherent level of security that negates the need for additional authentication factors such as DUO.
