import platform
from pathlib import Path

import pytest

# get OS -- currently only working with macOS
operating_platform = platform.platform()

if operating_platform.lower().startswith('darwin'):
    # it's macOS and we'll assume Jhove is installed in default location
    jhove_path = Path.home().joinpath('jhove/jhove')
else:
    # if it's not macOS, but I don't know where to look for jhove yet
    pass

image_path = Path.cwd()

def does_jhove_exist(jhove_path=jhove_path):
    return jhove_path.is_file()

def test_does_jhove_exist():
    assert does_jhove_exist() == True
    print(jhove_path)

jhove_module_list = ['tif', 'tiff', 'jpeg2000']
def jhove(image_path, jhove_module):
    if jhove_module.lower() not in jhove_module_list:
        print(f'jhove_module "{jhove_module}" not in jhove_module_list')
        print(jhove_module_list)
        return

@pytest.mark.skipif(does_jhove_exist()==False, reason="jhove not installed in default location")
def test_jhove():
    assert 'tiff' in jhove_module_list
    assert 'TIF' not in jhove_module_list
