Content Converter
====================

Installs and configures Content Converter web application along with required packages on Ubuntu using apt.

For reference, the git repository is available here: 

    https://github.com/City-of-Bloomington/content-converter

The repository is checked out as part of the tasks.

Once the application is installed you will need to import data based on what you want to track.

(TODO: instructions on process)


Role Variables
--------------


Dependencies
------------

This role assumes that cob.linux-common, cob.apache, and cob.mysql have been applied to the system already

Example Playbook
----------------
    - hosts: servers
      roles:
         - { role: cob.linux-common }
         - { role: cob.apache }
         - { role: geerlingguy.mysql }
         - { role: cob.shelter_manager }

License
-------

BSD

Author Information
------------------

This role and others like it are maintained as part of this repository:

https://github.com/city-of-bloomington/system-playbooks
