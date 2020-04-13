from pathlib import Path

import pytest

# assume Jhove is installed in default location
jhove_path = Path('/Users/dlisla/jhove/jhove')
image_path = Path.cwd()

def does_jhove_exist(jhove_path=jhove_path):
    return jhove_path.is_file()

def test_does_jhove_exist():
    assert does_jhove_exist() == True

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
    
