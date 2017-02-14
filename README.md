Ansible Role: sshd
==================

Configures the OpenSSH daemon.

Requirements
------------

 * CentOS 7.x
 * systemd
 * SELinux

Role Variables
--------------

See defaults/main.yml

Example Playbook
----------------

    - hosts: localhost
      become: yes
      roles:
        - sshd

Tests
-----

Use [molecule](https://github.com/metacloud/molecule) to test this role. 

Because this role depends on systemd and SELinux, only a Vagrant provider is configured at the moment.

License
-------

MIT
