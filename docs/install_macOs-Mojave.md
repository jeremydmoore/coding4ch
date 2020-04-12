# Installing on macOS 10.14.6 Mojave

A step by step series of examples to install the requisite programs to setup a development environment to run the code in this repository. All of the software to-be-installed below is either:
1. a commercial program included as part of macOS, but not installed by default
1. an open source program

### Prerequisites

1. You have administrative access to your system
1. You know how to operate the command line
  - If you don't know how to operate the command line please ask for assistance before beginning

This code is written for installation on macOS and has been tested on macOS 10.14.6 Mojave. The assumption is that you do not have a development environment on your computer before beginning these steps (if you don't know what that means, then you're also good to go!).


## Install Steps

1. Install XCode
1. Install XCode Select
1. Install Homebrew
1. Install Python
1. Install pip and virtual environments
1. Install Python packages

Suggested steps:
1. Install GitHub Desktop
1. Install Atom


### 1. Install [XCode](https://developer.apple.com/xcode/)
1. You will need to install XCode from the Apple's developer store as the version in the App Store no longer works on Mojave
   - **Latest Mojave version: 11.3.1**
1. Once you have installed XCode, open Terminal and accept the licenses

```
$ sudo xcodebuild -license
```
Press the `space` key as you read through the agreement, then type `agree` at the prompt.

### 2. Install XCode Select
I installed the command line tools a different way, but apparently this is the quickest method
```
$ sudo xcode-select --install
```


### 3. Install [Homebrew](https://brew.sh)
* Package manager for macOS
1. Download and install Homebrew
```
$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```
1. Decide if you want to turn analytics off (add link) << TODO
1. Update Homebrew
```
$ brew update
```
1. Make sure Homebrew's path is at the beginning of your computer's PATH
   1. Open your BASH profile in nano
   ```
   $ nano ~/.bash_profile
   ```
   1. Add the 2 lines below to the end of your profile
   ```
   # Homebrew
   export PATH=/usr/local/bin:$PATH
   ```
   1. Save the file with `ctrl + x`, `y`, `enter`
   1. Source the file (i.e. reload it)
   ```
   $ source ~/.bash_profile
   ```

### 4. Install [Python](https://python.org) plus a few extra things
1. Install Python
```
$ brew install python3
```
1. Test that Python 3 was correctly linked
```
$ which python3
```
   - Result should be `/usr/local/bin/python3`</br></br>
1. Install compiler and image I/O libraries
```
$ brew install cmake pkg-config wget
$ brew install jpeg libpng libtiff openexr
```
1. Optional: Install ImageMagick
```
$ brew install imagemagick
```

### 5. Install pip and virtual environments

```
code example
```

### 6. Install Python packages

## Suggested Installations:

### 1. Install [GitHub Desktop](https://desktop.github.com)
* Code repository management software for version control


### 2. Install [Atom](https://atom.io)
* Text editor
