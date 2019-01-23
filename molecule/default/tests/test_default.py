import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


# Test is /etc/hosts file is exist and have root:root attr
def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'

# Nginx example test
# def test_nginx_running_and_enabled(host):
#    nginx = host.service("nginx")
#    assert nginx.is_running
#    assert nginx.is_enabled
