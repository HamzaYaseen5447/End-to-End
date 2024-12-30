from setuptools import find_packages, setup
from typing import List

hypen_e_dot = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines() # this will read the lines in requirements.txt one by one
        requirements = [req.replace('\n', '') for req in requirements] # to replace the next line with blank 

    if hypen_e_dot in requirements:
        requirements.remove(hypen_e_dot)
    
    return requirements

# Consider as meta data information of entire project 
setup(
    name = 'ML Projects',
    version = '0.0.1',
    author = 'Hamza',
    author_email = 'hamzayaseen614268@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)