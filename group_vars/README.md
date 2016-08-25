Variables
===================

Variables are useful for abstracting configuration from various roles and playbooks.

Variables containing sensitive information should be encrypted. Ansible supports this with vaulted (encrypted) password files.

To make it easier to find where variables are defined (e.g. grep), it's best to keep a plaintext version of variables around that then point to the corresponding vaulted password file. This idea described here:

http://docs.ansible.com/ansible/playbooks_best_practices.html#variables-and-vaults

Vault
-----------

Using the vault is described here:

http://docs.ansible.com/ansible/playbooks_vault.html

To run a playbook with access to variables protected with the vault, use "--ask-vault-pass". For example:

    ansible-playbook playbooks/linux.yml -i hosts.txt --ask-become-pass --ask-vault-pass

To edit vaulted passwords:

    ansible-vault edit foo.yml

To encrypt a file using the vault:

    ansible-vault create foo.yml

All files in group_vars/vault are set to be ignored by version control.