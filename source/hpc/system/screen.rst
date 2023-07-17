Screen command
==============

This command provides the ability to launch and use multiple shell sessions from a single ssh session. 

When a process is started with **screen**, the process can be detached from the session & then can reattach the session at a later time. 

When the session is detached, the process that was originally started from the screen is still running and managed by the screen itself. 

The process can then re-attach the session at a later time, and the terminals are still there, the way it was left.

.. list-table:: 
    :widths: auto 
    :header-rows: 1

    * - **Command**
      - **Usage**
    * - **screen -ls**
      - To check the existing running screen/s.
    * - **screen -S screen_name**
      - To create a new screen with the name screen_name
    * - **Ctrl+a d**
      - To detach from a screen
    * - **screen -r screen_name**
      - To attach to a screen with the name screen_name
      
.. code-block:: bash

  [ms13779@login3 ~]$ screen -ls
  No Sockets found in /run/screen/S-ms13779.

  [ms13779@login3 ~]$ screen -S archiving
  [detached from 1189878.archiving]
  [ms13779@login3 ~]$ screen -ls
  There is a screen on:
	 1189878.archiving	(Detached)
  1 Socket in /run/screen/S-ms13779.
  [ms13779@login3 ~]$ screen -r 1189878.archiving
  [detached from 1189878.archiving]

.. note::

  Using screen you can run your command, detach from the screen session, close your device, and the command will still be running in the background, for more details, kindly check this `link <https://linuxize.com/post/how-to-use-linux-screen/>`_
  
The screen.sh script 
====================

``screen.sh`` is an in-house tool to automate the process of running commands in the background using the **screen** command.
It can be used as follows:
 
.. code-block:: bash

  [ms13779@login2 ~]$ screen.sh "cp -r /home/ms13779/result_56_1.txt /scratch/ms13779/"
  cp -r /home/ms13779/result_56_1.txt /scratch/ms13779/
  [ms13779@login2 ~]$ 
   
Where (cp -r /home/ms13779/result_56_1.txt /scratch/ms13779/) can be replaced with your command.

This script will do three things:
    * Execute the command in the background (inside the screen session).
    * Echo/ Print the command to the terminal.
    * Keep track of the command and its progress in a file in the same working directory called **output_background.log**.

.. Warning::

  This script can only be used if the running command doesn't need any interactive communication with the user like entering a password, if communication is required, then direct attaching to the screen using the **screen** command will be needed as described above. 

