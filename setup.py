from setuptools import setup,find_packages
from typing import List

#Declaring variables
Project_name = "Housing-Prediction"
Version = "0.0.7"
Author = "Umang Mudgal"
Requirement_File_Name = "requirements.txt"

def get_requirements_list()->List[str]:
    """
    Description: This function is going to return list
    requirement mention in requirements.txt

    return This function is going to return a list which 
    contain name of libraries mentioned in requirements.txt file
    """
    with open(Requirement_File_Name) as requirement_file:
        return requirement_file.readlines().remove("-e .")


setup(
    name = Project_name,
    version = Version,
    author = Author,
    description="This is housing Price prediction project",
    packages= find_packages(),
    install_requires=get_requirements_list()
)
