Variables
===================

Variables are useful for abstracting configuration from various roles and playbooks.

Variables containing sensitive information should be encrypted. Ansible supports this with vaulted (encrypted) password files.

To make it easier to find where variables are defined (e.g. grep), it's best to keep a plaintext version of variables around that then point to the corresponding vaulted password file. This idea is described here:

http://docs.ansible.com/ansible/playbooks_best_practices.html#variables-and-vaults

General information about how ansible works with variables is available here:

http://docs.ansible.com/ansible/playbooks_variables.html

Vault
-----------

Documentation about the vault is available here:

http://docs.ansible.com/ansible/playbooks_vault.html

To encrypt an already existing, unencrypted file:

    ansible-vault encrypt foo.yml

To edit vaulted passwords:

    ansible-vault edit foo.yml

To create a new encrypted file using the vault:

    ansible-vault create foo.yml
