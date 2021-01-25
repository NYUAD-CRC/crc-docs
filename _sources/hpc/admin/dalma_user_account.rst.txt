Dalma User Account
==================

There are 5 categories of users:

System users (<unix_uid> below 1000)
HPC team users (<unix_uid> starts after 1000)
Internal-use users, for example, test users (<unix_uid> starts after 8000)
Local public users, for example, gencore/mri (<unix_uid> starts after 50200; normally managed through SSH keys)
NetID users (<unix_uid> starts after 100000)
Categories 1 and 2 are normally managed internally through Salt; category 5 is managed automatically by IDM using IIQ User Operation. IIQ User Operation can also be run manually to manage categories 3 and 4 users.

 

To create a local public user (category 4):

On idm server as root, run:

iiq_createUser.sh -s <shell> -u <unix_uid> -c "<real_name>" <unix_username>
(for example, iiq_createUser.sh -s /bin/bash -u 50203 -c "MRI Lab" mri)

(Optional) Create/change user's group, see User's group Modification