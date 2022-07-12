# ansible-module-gitupdater

Ansible module for the git-repo-updater (gitup).

```
> GITUPDATER    (gitupdater.py)

  gitup https://github.com/earwig/git-repo-updater is a console script that allows you to easily update multiple git
  repositories at once.

Options (= is mandatory):

- cleanup
        Clean up the repositories that have been deleted.
        [Default: False]
- path
        Full path to the git repository.
        [Default: False]
- state
        State of the gitup configuration for this repository. The git repository itself is not affected.
        (Choices: present, absent)[Default: present]

Requirements:  git-repo-updater

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
    cleanup: yes

RETURN VALUES:


path:
    description: Full path to the git repository
    returned: always
    type: string
    sample: /path/to/repository
state:
    description: State of the gitup configuration for this repository
    returned: always
    type: string
    sample: present



MAINTAINERS: Josef Friedrich (@Josef-Friedrich)

METADATA:
	Status: ['preview']
	Supported_by: community
```

# Development

## Test functionality

```
/usr/local/src/ansible/hacking/test-module -m gitupdater.py -a
```

## Test documentation

```
source /usr/local/src/ansible/hacking/env-setup
/usr/local/src/ansible/test/sanity/validate-modules/validate-modules --arg-spec --warnings gitupdater.py
```

## Generate documentation

```
ansible-doc -M . gitupdater
```
