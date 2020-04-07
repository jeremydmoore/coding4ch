# Installing on macOS 10.14.6 Mojave (untested on macOS Catalalina 10.15)

A step by step series of examples to install the requisite programs to setup a development environment to run the code in this repository. All of the software to-be-installed below is either:
1. a commercial program included as part of macOS, but not installed by default
1. an open source program

## Prerequisites for macOS 10.14.6 Mojave (untested on macOS Catalalina 10.15)

This code is written for installation on macOS and has been tested on macOS 10.14.6 Mojave. The assumption is that you do not have a development environment on your computer before beginning these steps (if you don't know what that means, then you're also good to go!).

Homebrew is used to install Pipenv and Tesseract, which may cause issues if you use MacPorts.

## Install Steps

1. Install XCode
1. Install XCode Command-Line Tools
1. Install GitHub Desktop
1. Install Visual Studio Code
1. Install Homebrew
1. Install Python
1. Install Pipenv
1. Install development environment using PipFile from this GitHub repository


### Install [XCode](https://developer.apple.com/xcode/) from Apple's App Store
*Required to install to gain access to command-line programs on macOS

```
code example
```

### Install [XCode Command-Line Tools](https://idmsa.apple.com/IDMSWebAuth/signin?appIdKey=891bd3417a7776362562d2197f89480a8547b108fd934911bcbea0110d07f757&path=%2Fdownload%2Fmore%2F&rv=1) from Apple's Developer site
* May require free Apple developer account
 * Jeremy check if command-line tools can be installed without developer account
* Required to install command-line programs on macOS

```
code example
```

### Install [GitHub Desktop](https://desktop.github.com)
* Code repository management software for version control


### Install [Visual Studio Code](https://code.visualstudio.com/)
* Text editor
* [Privacy information](https://code.visualstudio.com/docs/supporting/faq#_how-to-disable-telemetry-reporting)


### Install [Homebrew](https://brew.sh)
* Package manager for macOS
* Turn off analytics if preferred
```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

Use Homebrew to install Python

```
code example
```

### Update Pip and install [Pipenv](https://pipenv.kennethreitz.org/en/latest/)
* [Real Python article](https://realpython.com/pipenv-guide/) about Pipenv
* Pipenv is Python's [recommended dependancy manager](https://packaging.python.org/tutorials/managing-dependencies/#managing-dependencies)

```
code example
```
