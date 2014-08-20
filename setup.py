#!/usr/bin/env python
from setuptools import setup
import os
import sys

if os.geteuid() == 0:
     data_files = [('/etc/bash_completion.d', ['extras/pycompletion.sh']),]
else:
     print(
'''******************************************************************************
Looks like you didn't run this command using sudo.
Pythonpy needs root privileges to copy pycompletion.sh to /etc/bash_completion.d
1) If you are in a virtualenv, you can configure tab completion without root using:
    source /path/to/virtualenv/bash_completion.d/pycompletion.sh
2) If you aren't using virtualenv, remember that pip requires sudo by default
    on most systems. py is a simple python script does not require any
    root access or special privileges. If you don't like using root,
    learn virtualenv and refer to 1).
Installation proceeding without root access...
******************************************************************************''')
     data_files = [('bash_completion.d', ['extras/pycompletion.sh']),]

py_entry = 'py%s = pythonpy.__main__:main'
pycompleter_entry = 'pycompleter%s = pythonpy.pycompleter:main'
endings = (
    '',
    '%d' % sys.version_info[0],
    '%d.%d' % sys.version_info[0:2]
)

entry_points_scripts = []
for e in endings:
    entry_points_scripts.append(py_entry % e)
    entry_points_scripts.append(pycompleter_entry % e)

setup(
    name='pythonpy',
    version='0.3.4',
    description='python -c, with tab completion and shorthand',
    data_files=data_files,
    license='MIT',
    url='https://github.com/Russell91/pythonpy',
    long_description='',
    packages = ['pythonpy'],
    entry_points = {
        'console_scripts': entry_points_scripts
    },
)
