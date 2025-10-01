Account Lifecycle
-----------------

This page outlines the lifecycle of HPC user accounts, including expiration timelines and access details. When you request or renew an HPC account, it is valid for one year. After this period, the account enters a series of states if not renewed, each with specific access permissions and data retention policies.
The account will have a state of the following: **Active**, **Suspended**, **Archived**, and **Deleted** where the following table summarizes them and their descriptions:

.. list-table:: 
    :header-rows: 1
    :widths: auto

    * - State
      - Duration
      - Access Details
    * - Active
      - 1 year from request or renewal
      - HPC resources and data are accessible
    * - Suspended
      - 3 months after Active
      - No HPC access; data retained (no direct access) and available on request.
    * - Archived
      - Lasts for 3 months after suspension ends (total 6 months from suspension)
      - No HPC access; data kept in archive. Data can be restored on request, but restoration takes longer than in suspended state.
    * - Deleted
      - After 6 months from suspension and the account is still not reactivated
      - Account and data permanently deleted, all access revoked.

.. note::
    You can request account reactivation within the 6-month period by following the instructions in this :doc:`page <account_renew>`. If your NetID remains unchanged, your data will be restored to your account. Otherwise, data migration to a new account may be required.
  