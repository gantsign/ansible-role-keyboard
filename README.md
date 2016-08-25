Ansible Role: Keyboard
======================

[![Build Status](https://travis-ci.org/gantsign/ansible-role-keyboard.svg?branch=master)](https://travis-ci.org/gantsign/ansible-role-keyboard)
[![Ansible Galaxy](https://img.shields.io/badge/ansible--galaxy-gantsign.keyboard-blue.svg)](https://galaxy.ansible.com/gantsign/keyboard)

Role to configure the keyboard layout etc.

Requirements
------------

* Ubuntu

Role Variables
--------------

The following variables will change the behavior of this role (default values
are shown below):

```yaml
# The XKB keyboard model name.
keyboard_model: pc104

# The XKB keyboard layout name.
keyboard_layout: us

# The XKB keyboard variant components.
keyboard_variant: ''

# The XKB keyboard option components.
keyboard_options: ''

# The behavior of <BackSpace> and <Delete> keys.
keyboard_backspace: guess
```

See `man keyboard` for configuration options.

Example Playbook
----------------

```yaml
- hosts: servers
  roles:
     - { role: gantsign.keyboard }
```

More roles from GantSign
------------------------

You can find more roles from GantSign on [Ansible Galaxy](https://galaxy.ansible.com/gantsign).

Development & Testing
---------------------

This project uses [Molecule](http://molecule.readthedocs.io/) to aid in the
development and testing; the role is unit tested using
[Testinfra](http://testinfra.readthedocs.io/) and
[pytest](http://docs.pytest.org/).

To develop or test you'll need to have installed the following:

* Linux (e.g. [Ubuntu](http://www.ubuntu.com/))
* [Docker](https://www.docker.com/)
* [Python](https://www.python.org/) (including python-pip)
* [Ansible](https://www.ansible.com/)
* [Molecule](http://molecule.readthedocs.io/)

To run the role (i.e. the `tests/test.yml` playbook), and test the results
(`tests/test_role.py`), execute the following command from the project root
(i.e. the directory with `molecule.yml` in it):

```bash
molecule test
```

License
-------

MIT

Author Information
------------------

John Freeman

GantSign Ltd.
Company No. 06109112 (registered in England)
