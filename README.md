# Ansible Playbooks

Configuring a machine to host services can be challenging. These playbooks are an attempt to codify and automate the processes we use at the City of Bloomington. Ansible is a configuration management system. For more information about Ansible, see:

http://www.ansible.com/how-ansible-works

The primary machine used to issue those commands is called the control machine. Hosts are the remote machines that you configure with Ansible. For more details about terms, see here:

http://docs.ansible.com/ansible/glossary.html

To use Ansible, you'll need a *nix based control machine/server that is used to configure and deploy any number of hosts and services. We have a dedicated server for this (ansible), but it is also possible to configure your local machine to be the control.

## Installing Ansible on control machine

Up-to-date details for installing an ansible control machine are available here:

http://docs.ansible.com/ansible/intro_installation.html

Be sure to install any missing requirements:

    sudo apt-get install build-essential libssl-dev libffi-dev python-dev python-pip
    pip install --upgrade pip

Optionally, create a python virtualenv on the main ansible control machine you'll use to configure other hosts:

[Virtualenv Setup](virtualenv.md)

    cd ~/path/to/scripts/for/ansible
    #should enable virtualenv

Finally, install ansible with pip:

    pip install ansible


## Configure Host Machines

### Base OS installation on hosts

Ansible assumes you have already set up the new host/destination machine with a base OS installation. There are many options for getting that configured:

  - Install a base OS on an actual hardware instance of a machine.
  - Install a base OS on a virtual machine. VirtualBox or VMWare are common options.
      - VirtualBox is a free and capable solution for creating virtual machines on your local machine.
      - VMWare is a commercial solution that also makes the base OS install very straightforward.
  - Use Vagrant to spin up a base virtual machine. Vagrant does have the abilitiy to call a configuration management solution like Ansible automatically. VirtualBox and VMWare are both options here too. If you're using VMWare for virtualization, you'll need the commercial version of Vagrant to work with VMWare.
  - Use Docker containers? (Still working on this...)

For VirtualBox, you'll need a "Host-only Adapter" in order to access the machine. When the VM is powered off, add another network interface:

    Virtual Box -> Devices -> Network -> Network Settings...
    Adapter 2 -> Enable Network Adapter
    Attached to: Host-only Adapter
    Name: vboxnet0

Then, when the machine is powered on, do:

    #find all adapters... should be a new one that is unconfigured
    ip addr
    #enp0s8 for me
    sudo vi /etc/network/interfaces
    #add new section for interface, adapting from lines already there

    # The local network interface
    auto enp0s8
    iface enp0s8 inet dhcp

    sudo /etc/init.d/networking restart
    #check for new ip with:
    ifconfig

Typically, openssh-server is available on server installations by default. Make sure that the host machine is accessible via SSH:

    sudo apt-get update
    sudo apt-get -y install openssh-server

Ansible requires Python installed on the host machine, as well:

    bash
    sudo apt-get install python

You'll also need a user account that can sudo.


### Configure SSH public key connections

https://help.ubuntu.com/community/SSH/OpenSSH/Keys

Generate local keys on the control machine:

    ssh-keygen -t rsa

then transfer the control machine's public key to the host/destination for the user that can sudo. See the link above for manual transfer process, or use ssh-copy-id. On OSX, this works:

https://github.com/beautifulcode/ssh-copy-id-for-OSX

    ssh-copy-id username@hostname

You can test this with:

    ssh username@hostname

If you're not prompted for a password, it worked!


## Ansible Configuration

### Tell ansible about hosts

Configure the host machines that you want to manage with ansible. Find the IP by looking at ifconfig on VM itself, and add it to a hosts file. The default hosts file is "/etc/ansible/hosts", but you can create one anywhere and specify it in an environment variable:

    echo "192.168.24.151" > hosts.txt
    export ANSIBLE_INVENTORY=~/path/to/scripts/for/ansible/hosts.txt

You can also pass the hosts file in as a parameter ("-i") on the command line.


### Ansible configuration defaults

Ansible expects playbooks, roles, etc (e.g. this repository) to be in /etc/ansible by default.

It is possible to work in a different location. Let ansible know with a local ansible.cfg file:

    cd /path/to/scripts/for/ansible
    vi ansible.cfg

For a starting point:

    curl -O https://raw.githubusercontent.com/ansible/ansible/devel/examples/ansible.cfg

Let ansible know where to find the roles:

    roles_path    = /etc/ansible/roles:/path/to/scripts/for/ansible

Note: A sample ansible.cfg file is now included with this repository

### Test Ansible:

At this point, if you run:

    ansible all -m ping -i hosts.txt

it should be "success"!

If you get an error, Ubuntu 16.04 server is no longer shipping with Python 2. You can make sure it is available with:

    ansible-playbook playbooks/bootstrap.yml -i hosts.txt --ask-become-pass

If you're using a VM, this is a good chance to take a snapshot of your host so it's easy to revert back to this point for testing.

## Using Ansible

### Applying system configurations

Ansible uses the concept of "roles" to group configurations for a specific purpose. The roles can be combined to form a playbook to configure a certain type of system.

Pick a playbook, review the configured roles, then give it a go:

    ansible-playbook playbooks/linux.yml -i hosts.txt --ask-become-pass

If the playbook completes successfully, *congratulations!* You should have a working server configured for the corresponding service.


For playbooks that utilize passwords in the vault, use this:

    ansible-playbook playbooks/linux.yml -i hosts.txt --ask-become-pass --ask-vault-pass

For details about the vault:

[Variables and Vaults](group_vars/)

As processes are refined, or as operating systems change, it is important to test and adapt the corresponding playbooks and roles to reflect current requirements.


## Roles

It can be helpful to abstract tasks that show up in more than one playbook / server as roles. 

To create new a new role:

    ansible-galaxy init cob.apache

When getting started with a new role, create it in the system-playbooks/roles directory. Once multiple playbooks make use of a role, abstract it out.

### Role Development

For development, roles need to be checked out from Github directly:

    git clone https://github.com/City-of-Bloomington/ansible-role-linux.git ./roles/City-of-Bloomington.linux
    git clone https://github.com/City-of-Bloomington/ansible-role-apache.git ./roles/City-of-Bloomington.apache
    git clone https://github.com/City-of-Bloomington/ansible-role-postgresql.git ./roles/City-of-Bloomington.postgresql
    git clone https://github.com/City-of-Bloomington/ansible-role-solr.git ./roles/City-of-Bloomington.solr
    git clone https://github.com/City-of-Bloomington/ansible-role-wsgi.git ./roles/City-of-Bloomington.wsgi
    git clone https://github.com/City-of-Bloomington/ansible-role-php.git ./roles/City-of-Bloomington.php

### External Roles

Some of our playbooks utilize external roles. These require using ansible-galaxy to pull them down and make them available locally.

To grab them all, in the main directory of this system-playbooks project, run the following:

    ansible-galaxy install --roles-path ./roles -r roles.yml

These roles are then available for use by playbooks.

Individual roles can be installed manually and included in playbooks. As an example, configuring MySQL:

https://github.com/geerlingguy/ansible-role-mysql  

This is included in the playbook with:

    - geerlingguy.mysql        

This requires using ansible-galaxy to pull down the role first:

    sudo ansible-galaxy install geerlingguy.mysql

This results in:

    "extracting geerlingguy.mysql to /etc/ansible/roles/geerlingguy.mysql" 


## References

Previously, we maintained instructions for manually configuring a linux system available here:

http://city-of-bloomington.github.io/LinuxInstallHelp/Ubuntu-Installation.html

However, these may grow out of date. This repository is a replacement for those.


This was a helpful guide for getting ansible configured initially:

https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-ansible-on-an-ubuntu-12-04-vps

Thanks!