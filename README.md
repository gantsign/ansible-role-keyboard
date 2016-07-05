Ansible Role: Keyboard
======================

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

License
-------

MIT

Author Information
------------------

John Freeman

GantSign Ltd.
Company No. 06109112 (registered in England)
