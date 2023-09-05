Uploading Data to Google Drive
==============================

Introduction
------------

The ``gdrive`` module provides a convenient way to interact with your Google Drive account from the 
command line. With ``gdrive``, you can easily upload, download, and manage files and directories on 
your Google Drive. This guide will walk you through the initial setup and common usage of the ``gdrive``
module.

Prerequisites
-------------

Before you begin, ensure that you have access to the ``gdrive`` module on your account. You can load the module using the following command::

    
    $ module load gdrive


Initial Authentication
-----------------------

The first time you use ``gdrive``, you will need to authenticate it with your Google account. Follow 
these steps:

1. Open your terminal and run the following command to initiate the authentication process::


   
    $ gdrive about

   This command will prompt you to authenticate.

2. You will see a message indicating that authentication is needed and a URL like the following::

   

    Go to the following URL in your browser:
    https://accounts.google.com/o/oauth2/auth?access_type=offline&client_id=3b3a15a0-bdb7-4cb0-abb4-3cb390278020.apps.googleusercontent.com&redirect_uri=d8a4cd5d-9700-482c-9c7e-abcdefghijk&response_type=code

3. Copy the URL and paste it into your web browser.

4. Sign in to your Google account using your NetID@nyu.edu credentials.

5. After signing in, you will receive a verification code. Copy this code.

6. Return to your terminal and paste the verification code when prompted.

Congratulations! Your 'gdrive' module is now authenticated with your Google Drive account.

Common Commands
----------------

Once authenticated, you can use 'gdrive' for various operations. Here are some common commands:

Uploading a File
~~~~~~~~~~~~~~~~

To upload a file to your Google Drive, use the following command, replacing `somefile.tar` with the name of the file you want to upload::

   

    $ gdrive upload somefile.tar

Uploading an Entire Directory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To upload an entire directory and its contents to Google Drive, use the `--recursive` flag with the `upload` command, replacing `some-directory-name` with the name of the directory::

    

    $ gdrive upload --recursive some-directory-name

Getting Help
~~~~~~~~~~~~

For more information and a list of available commands, you can use the following command::

    

    $ gdrive help

Additional Notes
----------------

- ``gdrive`` is particularly efficient for handling larger files. If you have a directory with a substantial amount of data to back up, it's recommended to create a single large tar file and upload it.

- Keep in mind that files uploaded to Google Drive are not directly accessible from the command line. To access them, you will need to download and extract them locally.

By following this guide, you can make the most of the ``gdrive`` module to manage your files and 
directories on Google Drive efficiently.
