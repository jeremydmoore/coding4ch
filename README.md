# coding4ch: Coding for Cultural Heritage

This repository serves as the code-base for utilities useful in cultural heritage imaging and mass digitization projects. It is **VERY** much a work in progress . . . 

This repository was announced and releassed at the [2020 DT West Coast Round Table](https://dtculturalheritage.com/events/dt-west-coast-round-table-pepperdine/) at Pepperdine University in Malibu, CA on March 12, 2020.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. We plan to have instructions for both macOS and Windows 10, but these will be tested on a limited number of computers. Please reach out and ask for assistance or help if you're having trouble with any of these steps.

### Prerequisites for macOS 10.14.6 Mojave (untested on macOS Catalalina 10.15)

This code is written for installation on macOS and has been tested on macOS 10.14.6 Mojave. The assumption is that you do not have a development environment on your computer before beginning these steps (if you don't know what that means, then you're also good to go!).

Homebrew is used to install Pipenv and Tesseract, which may cause issues if you use MacPorts.

### Installing on macOS 10.14.6 Mojave (untested on macOS Catalalina 10.15)

A step by step series of examples to install the requisite programs to setup a development environment to run the code in this repository. All of the software to-be-installed below is either:
1. a commercial program included as part of macOS, but not installed by default
1. an open source program

Install [XCode](https://developer.apple.com/xcode/) from Apple's App Store
*Required to install to gain access to command-line programs on macOS

```
code example
```

Install [XCode Command-Line Tools](https://idmsa.apple.com/IDMSWebAuth/signin?appIdKey=891bd3417a7776362562d2197f89480a8547b108fd934911bcbea0110d07f757&path=%2Fdownload%2Fmore%2F&rv=1) from Apple's Developer site
* May require free Apple developer account
 * Jeremy check if command-line tools can be installed without developer account
* Required to install command-line programs on macOS

```
code example
```

Install [GitHub Desktop](https://desktop.github.com)
* Code repository management software for version control

```
code example
```

Install [Atom](https://atom.io)
* Text editor

```
code example
```

Install [Homebrew](https://brew.sh)
* Package manager for macOS
* Turn off analytics if preferred
```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

Use Homebrew to install Tesseract and Pipenv

```
code example
```

Update Pip and install [Pipenv](https://pipenv.kennethreitz.org/en/latest/)
* [Real Python article](https://realpython.com/pipenv-guide/) about Pipenv

```
code example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo


### Prerequisites for Windows 10 version 1909
These setup instructions were written on a computer running Windows 10 Education, version 1909, OS build 18363.657 (info will be updated to current computer status once prerequisite and install are completed).

### Installing on Windows 10 version 1909

A step by step series of examples to install the requisite programs to setup a development environment to run the code in this repository. All of the software to-be-installed below is either:
1. a commercial program included as part of Windows 10, but not installed by default
1. an open source program

Install the [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install-win10) by opening PowerShell as Administrator and running (and *restart your computer* when prompted):

```
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux
```
| <img height=30% width=30% src="https://github.com/jeremydmoore/coding4ch/blob/master/docs/images/win10_powershell_run_as_administrator.png" /> | <img height=60% width=60% src="https://github.com/jeremydmoore/coding4ch/blob/master/docs/images/win10_activate_windows_subsystem_linux.png" /> | 

Install [Ubuntu 18.04 LTS](https://www.microsoft.com/en-us/p/ubuntu-1804-lts/9n9tngvndl3q?activetab=pivot:overviewtab) from the Windows Store
* May require free Microsoft account

<img height=60% width=60% src="https://github.com/jeremydmoore/coding4ch/blob/master/docs/images/win10_store_ubuntu_1804LTS_install.png" />

Install [GitHub Desktop](https://desktop.github.com)
* Code repository management software for version control


Install [Visual Studio Code](https://code.visualstudio.com/)
* Text editor


Update Pip and install [Pipenv](https://pipenv.kennethreitz.org/en/latest/)
* [Real Python article](https://realpython.com/pipenv-guide/) about Pipenv

```
code example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Contributing

Still to add

From the template: Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

* **Jeremy Moore** - *Initial work*

From the template: See also the list of [contributors (link not yet active)](https://github.com/your/project/contributors) who participated in this project.

## License

Copyright 2020 Jeremy D. Moore

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License. - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* **Billie Thompson** - *README.md template* - [PurpleBooth](https://github.com/PurpleBooth)
