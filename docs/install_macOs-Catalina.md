# Installing on macOS 10.15.4

A step by step series of examples to install the requisite programs to setup a development environment to run the code in this repository. All of the software to-be-installed below is either:
1. a commercial program included as part of macOS, but not installed by default
1. an open source program

### Prerequisites for macOS 10.14.6 Mojave (untested on macOS Catalalina 10.15)

1. You have administrative access to your system
1. You know how to operate the command line
  - If you don't know how to operate the command line please ask for assistance before beginning

This code is written for installation on macOS and has been tested on macOS 10.15.4 Catalina. The assumption is that you do not have a development environment on your computer before beginning these steps (if you don't know what that means, then you're also good to go!).


## Install Steps

1. Install XCode
1. Install XCode Select
1. Install GitHub Desktop
1. Install Atom
1. Install Homebrew
1. Install Python
1. Install


### 1. Install [XCode](https://developer.apple.com/xcode/) from Apple's App Store
1. Once you have installed XCode, open Terminal and accept the licenses

```
$ sudo xcodebuild -license
```
Press the `space` key as you read through the agreement, then type `agree` at the prompt.

### 2. Install XCode Select
* May require free Apple developer account

```
$ $ sudo xcode-select --install
```

### 3. Install [GitHub Desktop](https://desktop.github.com)
* Code repository management software for version control


### 4. Install [Atom](https://atom.io)
* Text editor


### 5. Install [Homebrew](https://brew.sh)
* Package manager for macOS
* Turn off analytics if preferred
```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

### 6. Install [Python](https://python.org) using Homebrew

```
code example
```

### Update Pip and install necessary libraries

```
code example
```
