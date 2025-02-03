from setuptools import setup, find_packages
from typing import List

E_dot = "-e ."
def get_requirements(file_path:str)->List[str]:
    '''
    this function returns a list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.remove("\n", "") for req in requirements]

        if E_dot in requirements:
            requirements.remove(E_dot)
    return requirements


setup(
    name="FoodDeliveryTimeEstimation",
    version="0.0.1",
    author="Dhanesh",
    author_email="dhaneshsakre@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)