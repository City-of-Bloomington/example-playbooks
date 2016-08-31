Factory Number One
====================

Installs and configures Factory Number One design pattern library along with required packages (gulp) on Ubuntu using apt.

For reference, the git repository is available here: 

    https://github.com/City-of-Bloomington/factory-number-one

The repository is checked out as part of the tasks.

Role Variables
--------------


Dependencies
------------

This role assumes that cob.linux-common has been applied to the system already

Example Playbook
----------------
    - hosts: servers
      roles:
         - { role: cob.linux-common }
         - { role: cob.fn1 }

License
-------

BSD

Author Information
------------------

The Information and Technology Services Department at the City of Bloomington, Indiana develops custom software to solve challenges common to all cities. We publish these solutions as open source software via our Github page.

This role and others like it are maintained as part of this repository:

https://github.com/city-of-bloomington/system-playbooks
