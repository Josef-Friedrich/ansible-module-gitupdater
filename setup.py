from setuptools import setup

setup(
    name='ansible-module-gitup',
    version='1.0.0',
    author='Josef Friedrich',
    author_email='josef@friedrich.rocks',
    license='GPL3',
    url='https://github.com/Josef-Friedrich/ansible-module-shellmarks',
    install_requires=[
        'ansible',
        'gitup',
        # test/utils/tox/requirements.txt
        'nose',
        'mock >= 1.0.1, < 1.1',
        'passlib',
        'coverage',
        'coveralls',
        'unittest2',
        'redis',
        'python-memcached',
        'python-systemd',
        'pycrypto',
        'botocore',
        'boto3',
        'pytest',
    ]
)
