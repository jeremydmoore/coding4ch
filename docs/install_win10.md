# Installing on Windows 10 version 1909

A step by step series of examples to install the requisite programs to setup a development environment to run the code in this repository. All of the software to-be-installed below is either:
1. a commercial program included as part of Windows 10, but not installed by default
1. an open source program

## Prerequisites for Windows 10 version 1909
These setup instructions were written on a computer running Windows 10 Education, version 1909, OS build 18363.657 (info will be updated to current computer status once prerequisite and install are completed).

### Installation Steps:
1. Install [GitHub Desktop](https://github.com/jeremydmoore/coding4ch/blob/master/docs/install_win10.md#install-github-desktop)
1. Install Visual Studio Code
1. Install Git
1. Enable Windows Subsystem for Linux (WSL)
1. Install Ubuntu 18.04 LTS
1. Install Python and pip
1. Setup Visual Studio Code to use WSL's Python
1. Install Pipenv
1. Install development environment using PipFile from this GitHub repository


### Install [GitHub Desktop](https://desktop.github.com)
* Code repository management software for version control


### Install [Visual Studio Code](https://code.visualstudio.com/)
* Text editor
* [Privacy information](https://code.visualstudio.com/docs/supporting/faq#_how-to-disable-telemetry-reporting)
1. [Install Visual Studio Code Remote - WSL extension](https://code.visualstudio.com/remote-tutorials/wsl/getting-started)


### Install [Git] for Windows(https://git-scm.com/)
1. Set Visual Studio Code as the Editor during installation


### Enable [Windows Subsystem for Linux (WSL)](https://code.visualstudio.com/remote-tutorials/wsl/enable-wsl)


### Install [Ubuntu 18.04 LTS](https://code.visualstudio.com/remote-tutorials/wsl/install-linux)
1. Search for/Select Ubuntu 18.04 LTS to install following the instructions at the link above


### Install [Python 3 and pip](https://code.visualstudio.com/remote-tutorials/wsl/install-python)
* Python 3
* Installed into WSL
* NOTE: Step 2 below is an additional step not in the directions linked above
1. Verify everything is up to date
```
$ apt update
```
2. Upgrade WSL package manager <-- THIS STEP NOT in LINK ABOVE!
```
$ sudo apt upgrade
```
3. Verify everything is up to date
```
$ apt update
```
4. Install Python 3 and pip
```
$ sudo apt install python3 python3-pip
```
5. Verify Python 3
```
$ python3 --version
```
6. [Setup VS Code to use WSL's Python](https://code.visualstudio.com/remote-tutorials/wsl/run-in-wsl)
7. [Install VS Code's Python Extension](https://code.visualstudio.com/remote-tutorials/wsl/edit-and-debug)
8. Upgrade pip and setuptools
```
$ python3 -m pip install --user --upgrade setuptools pip
```

### Install [Pipenv](https://pipenv.kennethreitz.org/en/latest/)
* [Real Python article](https://realpython.com/pipenv-guide/) about Pipenv
* Pipenv is Python's [recommended dependancy manager](https://packaging.python.org/tutorials/managing-dependencies/#managing-dependencies)
* [About Virtual Environments, Jupyter Notebooks, and Pipenv](https://towardsdatascience.com/virtual-environments-for-data-science-running-python-and-jupyter-with-pipenv-c6cb6c44a405#f91f-d040f09f69cf)
* [Common Pipenv errors](https://towardsdatascience.com/common-pipenv-errors-3a6f8ce81562)
```
$ python3 -m pip install --user pipenv
```
