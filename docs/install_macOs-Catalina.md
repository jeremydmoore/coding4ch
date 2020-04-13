# Installing on macOS 10.15.4

A step by step series of examples to install the requisite programs to setup a development environment to run the code in this repository. All of the software to-be-installed below is either:
1. a commercial program included as part of macOS, but not installed by default
1. an open source program

### Prerequisites

1. You have administrative access to your system
1. You know how to operate the command line
  - If you don't know how to operate the command line please ask for assistance before beginning

This code is written for installation on macOS and has been tested on macOS 10.15.4 Catalina. The assumption is that you do not have a development environment on your computer before beginning these steps (if you don't know what that means, then you're also good to go!).


## Install Steps

0. Update SHELL to use zsh
1. Install XCode
2. Install XCode Select
3. Install Homebrew
4. Install Python
5. Install pip and virtual environments
6. Install Python packages

Suggested steps:
1. Install GitHub Desktop
2. Install Atom

### 0. [Update SHELL to use zsh](https://support.apple.com/kb/HT208050)
- If you UPGRADED from an earlier version of macOS to to macOS Catalina, then your default Terminal SHELL is BASH
1. Open Terminal, and if you upgraded you should see the following message
```
The default interactive shell is now zsh.
To update your account to use zsh, please run `chsh -s /bin/zsh`.
For more details, please visit https://support.apple.com/kb/HT208050.
```
2. Enter the command given to update to zsh
```
$ chsh -s /bin/zsh
```
3. It will state `Changing shell for <username>.` and ask for your password, type it in, then press `return`
4. Quit Terminal, then open it again and your prompt should have changed from `$` to `%`
5. Quit Terminal
### 1. Install [XCode](https://apps.apple.com/us/app/xcode/id497799835?mt=12) from Apple's App Store
1. Once you have installed XCode, open Terminal and accept the licenses
```
% sudo xcodebuild -license
```
Press the `space` key as you read through the agreement, then type `agree` at the prompt, and press `return`

### 2. Install XCode Select
* May require free Apple developer account

```
% sudo xcode-select --install
```
