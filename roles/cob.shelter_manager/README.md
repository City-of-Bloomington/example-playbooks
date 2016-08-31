Shelter Manager
===================

Install Animal Shelter Manager along with common packages on Ubuntu using apt.

This role is based on the instructions in the README:

    https://dev.sheltermanager.com/tickets/browser/asm3/README

For reference, the git repository is available here. (checked out via tasks):

    git clone http://git.sheltermanager.com/asm3.git

Found via:

    https://dev.sheltermanager.com/tickets

After configuring the service and navigating to the application in your browser, you'll be prompted to initialize the database. Initially this failed for me. I was able to resolve this issue with help from the forum:

    https://dev.sheltermanager.com/forum/viewtopic.php?pid=609#p609

The solution was to edit the file:

    asm3/src/db.py

And change the following lines:

    elif DB_TYPE == "MYSQL":
        #s = MySQLdb.escape_string(s)
        s = s.replace("'", "`")

After the import ran successfully, I changed those lines back:

    elif DB_TYPE == "MYSQL":
        s = MySQLdb.escape_string(s)
        #s = s.replace("'", "`")

To import legacy data to your application, check the following resource:

    https://sheltermanager.com/repo/asm3_help/csvimportfields.html#csvimportfields



Role Variables
--------------


Dependencies
------------

This role assumes that cob.linux-common, cob.apache, and cob.mysql have been applied to the system already

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

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
