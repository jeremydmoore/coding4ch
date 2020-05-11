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

2. Once you have installed XCode, open Terminal and accept the licenses by entering, it will ask for your password
```
$ sudo xcodebuild -license
```
3. Press the `space` key as you read through the agreement, then type `agree` at the prompt.

### 2. Install XCode Select
1. Open Terminal and run the following, it will ask for your password
```
$ sudo xcode-select --install
```
2. A pop-up should appear asking you to click `Install` to install the command-line tools
3. When the software is installed you will receive a new pop-up that says so
4. Quit Terminal

### 3. Install [Homebrew](https://brew.sh)
* Package manager for macOS
1. Download and install Homebrew
```
$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```
2. Decide if you want to turn [analytics](https://docs.brew.sh/Analytics) off
3. Update Homebrew
```
$ brew update
```
4. Make sure Homebrew's path is at the beginning of your computer's PATH

   1. Open your BASH profile in nano
   ```
   $ nano ~/.bash_profile
   ```
   2. Add the 2 lines below to the end of your profile
   ```
   # Homebrew
   export PATH=/usr/local/bin:$PATH
   ```
   3. Save the file with `ctrl + x`, `y`, `enter`

   4. Source the file (i.e. reload it)
   ```
   $ source ~/.bash_profile
   ```

### 4. Install [Python](https://python.org) plus a few extra things
1. Install Python
```
$ brew install python3
```
2. Test that Python 3 was correctly linked
```
$ which python3
```
   - Result should be `/usr/local/bin/python3`
3. Install compiler and image I/O libraries
```
$ brew install cmake pkg-config wget
$ brew install jpeg libpng libtiff openexr
```
4. Optional: Install ImageMagick
```
$ brew install imagemagick
```

### 5. Install pip and virtual environments
1. Download the pip install script with wget
```
$ wget https://bootstrap.pypa.io/get-pip.py
```
2. Run the script with Python
```
$ sudo python3 get-pip.py
```
3. Install Python packages to use virtual environments
```
pip3 install virtualenv virtualenvwrapper
```
  - NOTE: my system did not require me to run this with `sudo`, but some of the install instructions I was looking at did say it may be necessary
4. Add virtual environments to your BASH profile

   1. Open your BASH profile in nano
   ```
   $ nano ~/.bash_profile
   ```
   2. Add the 2 lines below to the end of your profile
   ```
   # virtualenv and virtualenvwrapper
   export WORKON_HOME=$HOME/.virtualenvs
   export VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python3
   source /usr/local/bin/virtualenvwrapper.sh
   ```
   3. Save the file with `ctrl + x`, `y`, `enter`

   4. Source the file (i.e. reload it)
   ```
   $ source ~/.bash_profile
   ```

### 6. Create virtual environment and install Python packages
1. Create a virtual environment named `coding4ch`
```
$ mkvirtualenv coding4ch -p python3
```
   - Your terminal should change to reflect the this new environment by showing `(coding4ch)` before your `$` prompt
2. Install OpenCV
```
$ pip install opencv-contrib-python
```
3. Install image processing libraries
```
$ pip install scikit-image pillow
```
4. Install support libraries
```
$ pip install scikit-learn jupyter matplotlib numpy pandas pytest
```
5. TODO: Verify installation instructions

## Suggested Installations:

### 1. Install [GitHub Desktop](https://desktop.github.com)
* Code repository management software for version control


### 2. Install [Atom](https://atom.io)
* Text editor

### 3. Install Jhove
### 4. Install Exiftool
