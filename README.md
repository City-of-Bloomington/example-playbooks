## City of Bloomington Ansible Playbooks

We currently have instructions for configuring a linux system available here:

http://city-of-bloomington.github.io/LinuxInstallHelp/Ubuntu-Installation.html

These playbooks are an attempt at codifying and automating this process using the Ansible system:

http://www.ansible.com/how-ansible-works

### Installing Ansible

Create a python virtualenv on the main ansible machine you'll use to configure other machines:

[Virtualenv Setup](virtualenv.md)

    cd ~/path/to/scripts/for/ansible
    #should enable virtualenv

    pip install ansible

### Using Ansible

#### Base OS installation on hosts

This assumes you have already set up the new destination machine with a base OS installation. There are many options for getting that configured:

  - This could be completed using Vagrant and VirtualBox. If you're using VMWare for virtualization, you'll need the commercial version of Vagrant to work with VMWare.
  - I didn't have that, so I just did a manual install on the VM. VMWare does make this very straightforward to do.
  - This could also be an actual hardware instance of a machine.

You'll also need a user account that can sudo.

#### Tell ansible about hosts

Configure the different machines that you want to manage with ansible. You can find the IP by looking at ifconfig on VM itself. Then add it to a hosts file:

    echo "192.168.24.151" > hosts.txt
    export ANSIBLE_INVENTORY=~/path/to/scripts/for/ansible/hosts.txt

You can also pass the hosts file in as a parameter on the command line.

#### Configure SSH public key connections

https://help.ubuntu.com/community/SSH/OpenSSH/Keys

generate local keys:

    ssh-keygen -t rsa

then transfer the client's public key to the host for the user that can sudo.
see above for manual transfer process, or use ssh-copy-id
on OSX, this works:

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

the above steps are also outlined in this guide:

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



