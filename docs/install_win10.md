# Installing on Windows 10 version 1909

A step by step series of examples to install the requisite programs to setup a development environment to run the code in this repository. All of the software to-be-installed below is either:
1. a commercial program included as part of Windows 10, but not installed by default
1. an open source program

## Prerequisites for Windows 10 version 1909
These setup instructions were written on a computer running Windows 10 Education, version 1909, OS build 18363.657 (info will be updated to current computer status once prerequisite and install are completed).

## Installation Steps:
1. Install GitHub Desktop

   * GUI application to manage repositories on GitHub<br/><br/>

   1. Download and install [GitHub Desktop](https://desktop.github.com)

1. Install Visual Studio Code

   * Text editor<br/><br/>

   1. Download and install [Visual Studio Code](https://code.visualstudio.com/)
   1. Read information about [Privacy](https://code.visualstudio.com/docs/supporting/faq#_how-to-disable-telemetry-reporting)
   1. [Install Visual Studio Code Remote - WSL extension](https://code.visualstudio.com/remote-tutorials/wsl/getting-started)

1. Enable Windows Subsystem for Linux (WSL)

   * UNIX development environment<br/><br/>

   1. Enable [Windows Subsystem for Linux (WSL)](https://code.visualstudio.com/remote-tutorials/wsl/enable-wsl)

1. Install Ubuntu 18.04 LTS

   * Long Term Support Linux distribution<br/><br/>

   1. Install [Ubuntu 18.04 LTS](https://code.visualstudio.com/remote-tutorials/wsl/install-linux)
      * Select Ubuntu 18.04 LTS to install


1. Install Git for Windows

   * Version control software<br/><br/>

   1. Download and install [Git for Windows](https://git-scm.com/)
   1. Set Visual Studio Code as the Editor during installation
   1. Setup Git
      1. Open Git BASH
         * Fastest method: press the Windows Key, type bash into the search box, then press enter



1. Install Python and pip into WSL

   * Python 3 programming language
   * pip is [Python's package installer](https://pip.pypa.io/en/stable/)
   * [Tutorial with more information than below, but misses a couple of my steps](https://code.visualstudio.com/remote-tutorials/wsl/install-python)<br/><br/>

   1. Start WSL prompt by running ```wsl``` from the Windows Command Prompt
      * Fastest method: press the Windows Key, type wsl into the search box, then press enter
   1. [Verify Ubuntu package list is up to date](https://askubuntu.com/a/222352)
      * ``` $ sudo apt update ```
   1. [Upgrade Ubuntu packages](https://askubuntu.com/a/99039)
      * ```$ sudo apt full-upgrade```
   1. Verify everything is up to date
      * ```$ sudo apt update```
   1. Install Python 3 and pip
      * ```$ sudo apt install python3 python3-pip```
   1. Verify Python 3 is installed
      * ```$ python3 --version```
   1. Upgrade pip and setuptools
      * ```$ python3 -m pip install --user --upgrade setuptools pip```
   1. Install [pipenv](https://pipenv.kennethreitz.org/en/latest/)
      * ```$ python3 -m pip install --user pipenv```

1. [Setup VS Code to use WSL's Python](https://code.visualstudio.com/remote-tutorials/wsl/run-in-wsl)

1. [Install VS Code's Python Extension](https://code.visualstudio.com/remote-tutorials/wsl/edit-and-debug) for better editing and debugging

1. Install development environment using PipFile from this GitHub repository

## Additional Pipenv resources
* [Real Python article](https://realpython.com/pipenv-guide/) about Pipenv
* Pipenv is Python's [recommended dependancy manager](https://packaging.python.org/tutorials/managing-dependencies/#managing-dependencies)
* [About Virtual Environments, Jupyter Notebooks, and Pipenv](https://towardsdatascience.com/virtual-environments-for-data-science-running-python-and-jupyter-with-pipenv-c6cb6c44a405#f91f-d040f09f69cf)
* [Common Pipenv errors](https://towardsdatascience.com/common-pipenv-errors-3a6f8ce81562)