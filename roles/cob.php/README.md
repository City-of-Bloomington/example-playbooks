COB.PHP
=========

Install PHP along with common packages on Ubuntu using apt.

Dependencies
------------

This role assumes that cob.linux-common and cob.apache have been applied to the system already

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: cob.linux-common }
         - { role: cob.apache }
         - { role: cob.php }

License
-------

BSD

Author Information
------------------

This role and others like it are maintained as part of this repository:

https://github.com/city-of-bloomington/system-playbooks
