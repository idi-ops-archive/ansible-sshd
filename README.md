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

TCP port number that should be used by sshd

    sshd_port: 22

List of IPs to listen on (useful for restricting SSH on multi-homed servers) (empty list means listen on all IPs)

    sshd_listen_addresses: []

Only allow certain users to connect (empty list means allow all users)

    sshd_allowusers: []

Force certain groups of users to be SFTP-only (empty list means no users are forced to use SFTP)

    sshd_sftp_only_groups: []

Whether to permit root logins

    sshd_permit_root: no

Whether password authentication is allowed (RFC4252)

    sshd_password_auth: no

Allows 'keyboard-interactive' authentication (RFC4256)

    sshd_challenge_response_auth: no

Whether user authentication based on GSSAPI is allowed (needed for Kerberos)

    sshd_gssapi_auth: no

If sshd should destroy the user's GSSAPI credentials on logout

    sshd_gssapi_cleanup_credentials: no

Maximum concurrent unauthenticated connections (start:rate:full)

    sshd_maxstartups: "10:30:100"

Verify that reverse DNS lookup matches the IP address back

    sshd_use_dns: no

Use PAM (don't change unless using other authentication methods)

    sshd_use_pam: yes

Allow X11 forwarding over SSH

    sshd_x11_forwarding: no

Print /etc/motd when user logs in interactively

    sshd_print_motd: yes

Verbosity level (valid values: QUIET, FATAL, ERROR, INFO, VERBOSE, DEBUG, DEBUG1, DEBUG2, and DEBUG3)

    sshd_log_level: 'INFO'


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
