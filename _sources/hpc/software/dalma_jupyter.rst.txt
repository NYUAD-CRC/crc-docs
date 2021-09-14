Jupyter Notebook in Dalma
=========================

The Jupyter notebook requires tunneling through the Dalma network, which is currently disabled due to current OS restrictions as well as security reasons. Hence, It's not possible to launch Jupyter on one of the compute nodes and then run it on a local browser. However, you can get into a visualization node, start Jupyter and open it up in a browser launched within the visualization node. The visualization nodes are GPU based, hence GPU enabled code can be run on the notebook too.

Step-by-step guide
------------------

1. Set up your visualization node (Need to be done only once). If you have never used a visualization node on Dalma, click here to get familiar with it.
2. Request a visualization node ( ``viz-tvnc -X``)
3. Get into the visualization node using ssvnc.
4. Open a terminal within the visualization node and launch Jupyter notebook.
5. Open another terminal within the visualization node and launch a browser here and subsequently run Jupyter notebook.

A sample output is shown below:

.. image:: /hpc/img/jupyter.png

.. tip::

    If you don't have a preinstalled browser, you can clone the 'firefox' environment from Dalma 'miniconda' module or launch the browser by passing on the following commands in a terminal within the visualization node

    .. code-block:: bash

        source /share/apps/NYUAD/miniconda/3-4.8.2/bin/activate
        conda activate firefox
        firefox