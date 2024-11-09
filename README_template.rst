{{ badge.github_workflow() }}

ansible-module-gitupdater
=========================

Ansible module for the `git-repo-updater <https://github.com/earwig/git-repo-updater>`__ (gitup).

{{ cli('ansible-doc gitupdater') | literal }}

Development
===========

Test functionality
------------------

::

   /usr/local/src/ansible/hacking/test-module -m gitupdater.py -a

Test documentation
------------------

::

   source /usr/local/src/ansible/hacking/env-setup
   /usr/local/src/ansible/test/sanity/validate-modules/validate-modules --arg-spec --warnings gitupdater.py

Generate documentation
----------------------

::

   ansible-doc -M . gitupdater
