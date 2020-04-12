# Installing on Ubuntu 18.04LTS
## Currently installing Ubuntu 18.04LTS now . . .

These are my steps

### Assuming you're on Windows 10 and don't have an Ubuntu install yet . . .
1. Use diskmanager to shrink your boot disk (I shrank it 60000 or ~60gb)
1. Download Ubuntu 18.04LTS ISO and Rufus
1. Use Rufus to install ISO to a USB drive
1. Reboot into BIOS
  1. Set Secure Boot to Other-OS or Off
1. Reboot into USB stick
1. Install Ubuntu
  1. Choose `Install Ubuntu`
    - NOTE: If you have an NVIDIA video card you may experience display corruption without the proprietary drivers
       - Fix by adding `nomodeset` to the end of the linke that starts with `linux` in setparams for Ubuntu Install (press `e` while *Install Ubuntu* is highlighted to get access
  1. Normal installation, download updates while installing
  1. Choose *Something else*
    - Choose the free space we just allocated and create a new ext4 filesystem at the /(root) mount point
       - Type: Primary
       - Location: Beginning of this space
       - Use as: EXT4 journaling file filesystem
       - Mount point = /
    - Select `Windows Boot Manager` as device for boot loader installation and click `Install Now`
