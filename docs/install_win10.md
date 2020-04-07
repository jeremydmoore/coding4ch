# Installing on Windows 10 version 1909

A step by step series of examples to install the requisite programs to setup a development environment to run the code in this repository. All of the software to-be-installed below is either:
1. a commercial program included as part of Windows 10, but not installed by default
1. an open source program

## Prerequisites for Windows 10 version 1909
These setup instructions were written on a computer running Windows 10 Education, version 1909, OS build 18363.657 (info will be updated to current computer status once prerequisite and install are completed).

### Installation Steps:
1. Install Windows Subsystem for Linux
1. Install Ubuntu 18.04 LTS
1. Install GitHub Desktop
1. Install Visual Studio Code
1. Install Python
1. Install Pipenv
1. Install development environment using PipFile from this GitHub repository

### Install the [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install-win10) by opening PowerShell as Administrator and running (and *restart your computer* when prompted):

```
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux
```
| <img height=30% width=30% src="https://github.com/jeremydmoore/coding4ch/blob/master/docs/images/win10_powershell_run_as_administrator.png" /> | <img height=60% width=60% src="https://github.com/jeremydmoore/coding4ch/blob/master/docs/images/win10_activate_windows_subsystem_linux.png" /> | 

### Install [Ubuntu 18.04 LTS](https://www.microsoft.com/en-us/p/ubuntu-1804-lts/9n9tngvndl3q?activetab=pivot:overviewtab) from the Windows Store
* May require free Microsoft account

<img height=60% width=60% src="https://github.com/jeremydmoore/coding4ch/blob/master/docs/images/win10_store_ubuntu_1804LTS_install.png" />

### Install [GitHub Desktop](https://desktop.github.com)
* Code repository management software for version control


### Install [Visual Studio Code](https://code.visualstudio.com/)
* Text editor
* [Privacy information](https://code.visualstudio.com/docs/supporting/faq#_how-to-disable-telemetry-reporting)
1. [Setup VS Code](https://code.visualstudio.com/remote-tutorials/wsl/getting-started) for use with Windows Subsystem for Linux

Use  to install Python

```
code example
```

### Update Pip and install [Pipenv](https://pipenv.kennethreitz.org/en/latest/)
* [Real Python article](https://realpython.com/pipenv-guide/) about Pipenv

```
code example
```
