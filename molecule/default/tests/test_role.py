import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_keyboard_file(host):
    kb = host.file('/etc/default/keyboard')

    assert kb.exists
    assert kb.is_file
    assert kb.user == 'root'
    assert kb.group == 'root'
    assert oct(kb.mode) == '0644'

    assert kb.contains('XKBMODEL="pc105"')
    assert kb.contains('XKBLAYOUT="brai"')
    assert kb.contains('XKBVARIANT="right_hand"')
    assert kb.contains('XKBOPTIONS="lv3:alt_switch,compose:rctrl"')
    assert kb.contains('BACKSPACE="guess"')
