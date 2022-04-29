Installing Jupyter Kernels
==========================

This user guide provides instructions for installing Jupyter kernels when 
using Jupyter notebook via HPC Web interface OnDemand. 
For more information about OnDemand and using Jupyter notebooks, 
please check the following :doc:`section </hpc/ood/index>`.

A Jupyter kernel is a programming language-specific process that executes the code contained in a Jupyter notebook. The following provides installation instructions for a few popular Jupyter kernels, which will be installed in your home directory at ~/.local/share/jupyter/kernels. Install the kernels when logged in to NYUAD HPC before accessing them via the Jupyter OnDemand interactive app.

When installing kernels, make sure to use descriptive names in order to distinguish among them. Once installed, when launching Jupyter on OnDemand, the kernels will show up on a Launcher tab (File > New Launcher) and when selecting kernels through other methods.

Many software kernels are available for use with Jupyter. See a full list here: https://github.com/jupyter/jupyter/wiki/Jupyter-kernels.

Python
------

The default kernel is for Python 3.10.0, and this is ready to be used when Jupyter is launched. To use other versions of Python, enter a set of commands like the following:

.. code-block:: bash
	
	module load python/3.8.6
	python -m ipykernel install --user --name py376 --display-name "Python 3.8.6"
	
Make sure to use a descriptive name.

The kernels will be able to access your user-installed Python packages.

Conda Envs
----------

To use a Python kernel from a Conda environment, install the ipykernel package in the Conda environment and then create a kernel. For example, with a Conda environment named myenv, enter a set of commands like the following to create a Python kernel:


.. code-block:: bash
	
	module purge
	conda activate myenv
	conda install -c conda-forge ipykernel
	python -m ipykernel install --user --name myenv --display-name "My env"
	

To use an **R kernel from a Conda environment**, install the IRkernel package in the Conda environment and then create a kernel. For example, with a Conda environment named myenv, enter a set of commands like the following to create an R kernel:

.. code-block:: bash

	module purge
	conda activate myenv
	conda install -c r r-irkernel
	Rscript -e "IRkernel::installspec(name = 'r410', displayname = 'R 4.1.0')"
	
	
R
--

To install an R kernel, first load the python/3.8.6 module and the R module version of your choice:

.. code-block:: bash

	module load python/3.8.6 r/<version>
	
Then within an R session, create a kernel with a command like the following:

.. code-block:: bash

	> IRkernel::installspec(name = 'r410', displayname = 'R 4.1.0')
	
The kernel will be able to access your user-installed R packages.


Stata
-----

To install a Stata kernel, enter the following commands:

.. code-block:: bash

	module load python/3.9.2 stata
	pip install stata_kernel --user
	python -m stata_kernel.install --user

Julia
-----

To install a Julia kernel, first load the python/3.9.2 module and the Julia module version of your choice:

module load python/3.8.6 julia/<version>

Then within a Julia session, install the IJulia package:

.. code-block:: bash

	pkg> add IJulia

This will create a Julia kernel automatically.

The kernel will be able to access your user-installed Julia packages.

MATLAB
------

To install a MATLAB kernel, enter the following commands:

.. code-block:: bash

	module load python/3.8.6 matlab
	pip install imatlab --user
	python -mimatlab install --user

The Matlab engine for Python requires an older version of Python, so here we use the python/3.8.6 module.

Within a notebook, to display inline graphics include the following command in one of the beginning cells:

.. code-block:: bash

	imatlab_export_fig('print-png')

Mathematica
-----------

To install a Mathematica kernel, run the following commands:

.. code-block:: bash

	module load python/3.8.6 mathematica
	git clone https://github.com/WolframResearch/WolframLanguageForJupyter.git
	cd WolframLanguageForJupyter
	./configure-jupyter.wls add


Bash
----

To install a Bash kernel, enter the following commands:

.. code-block:: bash

	module load usc python/3.9.2
	pip install bash_kernel --user
	python -m bash_kernel.install --user
	
	