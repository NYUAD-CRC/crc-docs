$HOME and $SCRATCH
==================

``$HOME`` and ``$SCRATCH`` can be accessed as follows:

::

    # to check where you are
    pwd
    # to change the current working directory to $HOME
    cd $HOME
    # is equivalent to
    cd /home/<your-NetID>
    # or
    cd
    # for $SCRATCH
    cd $SCRATCH

    or 

    cd /scratch/<your-NetID>

We urge our users to clean up their storage regularily.

.. warning::
    **Retention Policy Applies**

    Files older than 90 days at $SCRATCH will be deleted.

.. caution::
    Running jobs from ``/home`` is a **serious violation** of HPC policy. Any users who intentionally violate this policy will get their account suspended. 
    ``$HOME`` SSDs are not designed for this purpose, it will kill the SSDs quickly. 
