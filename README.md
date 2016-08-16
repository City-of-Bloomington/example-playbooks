## City of Bloomington Ansible Playbooks

We have instructions for manually configuring a linux system available here:

http://city-of-bloomington.github.io/LinuxInstallHelp/Ubuntu-Installation.html

These playbooks are an attempt to codify and automate this process using Ansible:

http://www.ansible.com/how-ansible-works

To use Ansible, you'll need a host/server machine that is used to configure and deploy any number of clients. We have a dedicated server for this (ansible), but it is also possible to configure your local machine to be a host. 

### Installing Ansible

Create a python virtualenv on the main ansible machine you'll use to configure other machines:

[Virtualenv Setup](virtualenv.md)

    cd ~/path/to/scripts/for/ansible
    #should enable virtualenv

    pip install ansible

### Using Ansible

#### Base OS installation on clients

Ansible assumes you have already set up the new client/destination machine with a base OS installation. There are many options for getting that configured:

  - Install a base OS on an actual hardware instance of a machine.
  - Install a base OS on a virtual machine. VirtualBox or VMWare are common options.
      - VirtualBox is a free and capable solution for creating virtual machines on your local machine.
      - VMWare is a commercial solution that also makes the base OS install very straightforward.
  - Use Vagrant to spin up a base virtual machine. Vagrant does have the abilitiy to call a configuration management solution like Ansible automatically. VirtualBox and VMWare are both options here too. If you're using VMWare for virtualization, you'll need the commercial version of Vagrant to work with VMWare.
  - Use Docker containers? (Still working on this...)

You'll also need a user account that can sudo.

#### Tell ansible about hosts

Configure the different machines that you want to manage with ansible. You can find the IP by looking at ifconfig on VM itself. Then add it to a hosts file:

    echo "192.168.24.151" > hosts.txt
    export ANSIBLE_INVENTORY=~/path/to/scripts/for/ansible/hosts.txt

You can also pass the hosts file in as a parameter on the command line.

#### Configure SSH public key connections

https://help.ubuntu.com/community/SSH/OpenSSH/Keys

Generate local keys:

    ssh-keygen -t rsa

then transfer the client's public key to the host for the user that can sudo. See the link above for manual transfer process, or use ssh-copy-id. On OSX, this works:

https://github.com/beautifulcode/ssh-copy-id-for-OSX


#### Ansible configuration defaults (optional)

    cd ~/path/to/scripts/for/ansible 
    vi ansible.cfg

using this as template:

https://raw.githubusercontent.com/ansible/ansible/devel/examples/ansible.cfg


#### Test Ansible:

hopefully, at this point, if you run:

    ansible all -m ping -i hosts.txt

it should be "success"!

another helpful testing / debug command:

    ansible apache -m command -a "/bin/echo hello sammy"

The above steps are also outlined in this guide:

https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-ansible-on-an-ubuntu-12-04-vps


### Applying configurations

I have modeled these playbooks closely to the documentation we have for configuring our linux servers. This may not be optimal from Ansible's best practices perspective, but it's a good place to start. So far, we have:

    ansible-playbook common.yml -i hosts.txt --ask-become-pass

    ansible-playbook db.yml -i hosts.txt --ask-become-pass

    ansible-playbook apache.yml -i hosts.txt --ask-become-pass

    ansible-playbook php.yml -i hosts.txt --ask-become-pass


Be sure to change:

    remote_user: username

to whatever username you configured on the system.



