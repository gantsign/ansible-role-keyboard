Ansible Role: Keyboard
======================

[![Build Status](https://travis-ci.org/gantsign/ansible-role-keyboard.svg?branch=master)](https://travis-ci.org/gantsign/ansible-role-keyboard)
[![Ansible Galaxy](https://img.shields.io/badge/ansible--galaxy-gantsign.keyboard-blue.svg)](https://galaxy.ansible.com/gantsign/keyboard)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/gantsign/ansible-role-keyboard/master/LICENSE)

Role to configure the keyboard layout etc.

Requirements
------------

* Ansible >= 2.4

* Linux Distribution

    * Debian Family

        * Debian

            * Jessie (8)
            * Stretch (9)

        * Ubuntu

            * Trusty (14.04)
            * Xenial (16.04)
            * Bionic (18.04)

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
    - role: gantsign.keyboard
      # European keyboard model (pc105 is widely used outside Europe as well)
      keyboard_model: pc105
      # Layout for Great Britain / United Kingdom
      keyboard_layout: gb
```

More Roles From GantSign
------------------------

You can find more roles from GantSign on
[Ansible Galaxy](https://galaxy.ansible.com/gantsign).

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

Because the above can be tricky to install, this project includes
[Molecule Wrapper](https://github.com/gantsign/molecule-wrapper). Molecule
Wrapper is a shell script that installs Molecule and it's dependencies (apart
from Linux) and then executes Molecule with the command you pass it.

To test this role using Molecule Wrapper run the following command from the
project root:

```bash
./moleculew test
```

Note: some of the dependencies need `sudo` permission to install.

License
-------

MIT

Author Information
------------------

John Freeman

GantSign Ltd.
Company No. 06109112 (registered in England)
