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

Make sure that the client machine is accessible via SSH:

    sudo apt-get update
    sudo apt-get -y install openssh-server

And that the firewall is allowing ssh traffic:

    sudo ufw allow ssh

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

You'll also need a user account that can sudo.

#### Configure SSH public key connections

https://help.ubuntu.com/community/SSH/OpenSSH/Keys

Generate local keys:

    ssh-keygen -t rsa

then transfer the hosts's public key to the client/destination for the user that can sudo. See the link above for manual transfer process, or use ssh-copy-id. On OSX, this works:

https://github.com/beautifulcode/ssh-copy-id-for-OSX

    ssh-copy-id username@hostname

You can test this with:

    ssh username@hostname

If you're not prompted for a password, it worked!

#### Tell ansible about hosts

Configure the client machines that you want to manage with ansible. Find the IP by looking at ifconfig on VM itself, and add it to a hosts file. The default hosts file is "/etc/ansible/hosts", but you can create one anywhere and specify it in an environment variable:

    echo "192.168.24.151" > hosts.txt
    export ANSIBLE_INVENTORY=~/path/to/scripts/for/ansible/hosts.txt

You can also pass the hosts file in as a parameter ("-i") on the command line.


#### Ansible configuration defaults

Ansible expects playbooks, roles, etc (e.g. this repository) to be in /etc/ansible by default.

It is possible to work in a different location. Let ansible know with a local ansible.cfg file:

    cd /path/to/scripts/for/ansible 
    vi ansible.cfg

For a starting point:

    curl -O https://raw.githubusercontent.com/ansible/ansible/devel/examples/ansible.cfg

Let ansible know where to find the roles:

    roles_path    = /etc/ansible/roles:/path/to/scripts/for/ansible

Note: This repository is set to ignore the ansible.cfg file.

#### Test Ansible:

At this point, if you run:

    ansible all -m ping -i hosts.txt

it should be "success"!

If you get an error, Ubuntu 16.04 server is no longer shipping with Python 2. You can make sure it is available with:

    ansible-playbook playbooks/bootstrap.yml -i hosts.txt --ask-become-pass


### Applying system configurations

Ansible uses the concept of "roles" to group configurations for a specific purpose. The roles can be combined to form a playbook to configure a certain type of system.

Pick a playbook, review the configured roles, then give it a go:

    ansible-playbook playbooks/linux.yml -i hosts.txt --ask-become-pass

If the playbook completes successfully, *congratulations!* You should have a working server configured for the corresponding service. 


For playbooks that utilize passwords in the vault, use this:

    ansible-playbook playbooks/linux.yml -i hosts.txt --ask-become-pass --ask-vault-pass

For details about the vault:

[Variables and Vaults](group_vars/)



### Maintenance

As processes are refined, or as operating systems change, it is important to test and adapt these configurations to reflect current requirements. 

#### Creating new roles

    ansible-galaxy init cob.apache



### References

The above steps were originally inspired by:

https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-ansible-on-an-ubuntu-12-04-vps

Thanks!