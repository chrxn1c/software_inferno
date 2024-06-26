from setuptools import setup

setup(
    name='database_module',
    version='0.1',
    description='Connection to db',
    author='chrxn1c',
    author_email='drop_table_if_exists_users@gmail.com',
    packages=['database_module'],
    install_requires=['sqlite3'],
)
