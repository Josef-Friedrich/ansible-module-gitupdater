.. image:: https://github.com/Josef-Friedrich/ansible-module-gitupdater/actions/workflows/tests.yml/badge.svg
    :target: https://github.com/Josef-Friedrich/ansible-module-gitupdater/actions/workflows/tests.yml
    :alt: Tests

ansible-module-gitupdater
=========================

Ansible module for the `git-repo-updater <https://github.com/earwig/git-repo-updater>`__ (gitup).

:: 

    > MODULE gitupdater (/etc/ansible/library/gitupdater.py)

      gitup https://github.com/earwig/git-repo-updater is a console script
      that allows you to easily update multiple git repositories at once.

    OPTIONS (red indicates it is required):

       cleanup  Clean up the repositories that have been deleted.
            default: false

       path    Full path to the git repository.
            default: false

       state   State of the gitup configuration for this repository. The git
               repository itself is not affected.
            choices: [present, absent]
            default: present

    REQUIREMENTS:  git-repo-updater

    AUTHOR: Josef Friedrich (@Josef-Friedrich)

    METADATA:           metadata_version: '1.0'
              status:
              - preview
              supported_by: community

    EXAMPLES:
    # Bookmark a repository, state can be omitted
    - gitupdater:
        path: /var/repos/project

    # Bookmark a repository
    - gitupdater:
        path: /var/repos/project
        state: present

    # Delete bookmark
    - gitupdater:
        path: /var/repos/project
        state: absent

    # Delete non-existent repositories
    - gitupdater:
        cleanup: true

    RETURN VALUES:

       path    Full path to the git repository
            returned: always
            sample: /path/to/repository
            type: string

       state   State of the gitup configuration for this repository
            returned: always
            sample: present
            type: string

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
