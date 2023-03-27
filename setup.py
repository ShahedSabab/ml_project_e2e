#!/usr/bin/env python

from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    this function will returen the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [r.replace('\n', '') for r in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    
    return requirements


setup(name='ml_project',
      version='0.0.1',
      author='Shahed Anzarus Sabab',
      author_email='sababsa@myumanitoba.ca',
      packages = find_packages(),
      install_requires = get_requirements('requirements.txt')
     )