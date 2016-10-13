Tiaga
====================

Installs and configures Tiaga project management web application along with required packages on Ubuntu using apt.

Roughly follows:

http://taigaio.github.io/taiga-doc/dist/setup-production.html

Once the application is installed you will need to import data based on what you want to track.


Role Variables
--------------


Dependencies
------------

This role assumes that cob.linux-common, cob.apache, and cob.mysql have been applied to the system already

Example Playbook
----------------
    - hosts: servers
      roles:

License
-------

BSD

Author Information
------------------

This role and others like it are maintained as part of this repository:

https://github.com/city-of-bloomington/system-playbooks
