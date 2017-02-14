Ansible Role: sshd
=========

Configures the OpenSSH daemon.

Requirements
------------

None.

Role Variables
--------------

    sshd_protocol
    sshd_ports       # list
    sshd_listen_ips  # list -- optional
    sshd_allowusers  # list -- optional
    
    sshd_permit_root
    sshd_password_auth
    sshd_challenge_response_auth
    sshd_gssapi_auth
    sshd_gssapi_cleanup_credentials
    
    sshd_use_dns
    sshd_use_pam
    sshd_x11_forwarding
    sshd_print_motd

    sshd_maxstartups

These variables are set to OpenSSH default settings initially.

Dependencies
------------

None.

Example Playbook
----------------

    - hosts: localhost
      become: yes
      roles:

        - role: sshd
          sshd_ports: [ 22, 2222 ]
          sshd_listen_ips: [ 127.0.0.1 ]
          sshd_permit_root: no
          sshd_password_auth: no
          sshd_challenge_response_auth: no
          sshd_gssapi_auth: no
          sshd_use_dns: no
          sshd_x11_forwarding: no
          sshd_print_motd: no
