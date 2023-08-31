from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    this functions returns the list of requirements
    '''
    requirements = []
    with open (file_path) as file_obj:
        requiremnts = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements.txt]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requiremnts
setup(
name= 'MLPROJECT',
version= '0.0.1',
author = 'harshitha',
author_email = 'harshithamanjunath84@gmail.com',
packages = find_packages(),
install_requires = get_requirements('requirements.txt')

)