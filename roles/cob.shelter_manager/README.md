Role Name
=========

Install Animal Shelter Manager along with common packages on Ubuntu using apt.

This role is based on the instructions in the README:

    https://dev.sheltermanager.com/tickets/browser/asm3/README

For additional details, clone the git repository:

    git clone http://git.sheltermanager.com/asm3.git

Available here:

    https://dev.sheltermanager.com/tickets

MySQL still requires manual configuration:

    mysql -u root -p

Then, via MySQL:

    SET PASSWORD FOR 'root'@'localhost' = PASSWORD('newpassword');
    CREATE DATABASE asm;

Then, wherever the source code is checked out to, you can run a server with:

    cd /location/of/source/code/asm3/src
    python code.py 5000

In a browser:

    http://0.0.0.0:5000/

You'll be prompted to initialize the database via a web process. Initially this failed for me. I was able to resolve this issue with help from the forum:

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

A description of the settable variables for this role should go here, including any variables that are in defaults/main.yml, vars/main.yml, and any variables that can/should be set via parameters to the role. Any variables that are read from other roles and/or the global scope (ie. hostvars, group vars, etc.) should be mentioned here as well.

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
         - { role: cob.mysql }
         - { role: cob.shelter_manager }

License
-------

BSD

Author Information
------------------

This role and others like it are maintained as part of this repository:

https://github.com/city-of-bloomington/system-playbooks
