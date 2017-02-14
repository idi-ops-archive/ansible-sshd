import testinfra.utils.ansible_runner


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_sshd_config_file(File):
    f = File('/etc/ssh/sshd_config')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
    assert f.mode == 0o600


def test_sshd_service(Service):
    s = Service('sshd')

    assert s.is_enabled
    assert s.is_running


def test_sshd_process(Process):
    p = Process.filter(user='root', comm='sshd')

    assert len(p) >= 1


# FIX: Port to be tested should be retrieve from Ansible variables
def test_sshd_socket(Socket):
    s = Socket("tcp://0.0.0.0:22")

    assert s.is_listening
