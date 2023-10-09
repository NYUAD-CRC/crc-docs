Perl - Create and manage your own Perl environment
==================================================

NYUAD HPC team provides a global Perl software environment which can be used through "Linux environment modules". We do not install additional Perl modules to the global environment. So if you need, say the LWP Perl module, you will need to "localise" the global Perl environment to your home directory and install the LWP module yourself.

The localisation is based on Perl's local::lib



Step-by-step guide
Login Jubail.
(One time setup) Run this in terminal:

$RECIPESDIR/localize-perl.sh
 If the localization is successful, in the end the screen output will be similar to this:


**Now re-login to take effect of localization of Perl**

 
Perl localization completed.
 

Logout Jubail and login again.

Now you should be able to install Perl modules using cpanm. Example installing LWP Perl module:

module load gcc perl
cpanm LWP
Notice that for a lot of Perl modules, gcc must be loaded to compile against them.

 Find more information on how to use cpanm, section Quick start and Tools here:   http://www.cpan.org/modules/INSTALL.html 
