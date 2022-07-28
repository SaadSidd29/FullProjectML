from setuptools import setup

PROJECT_NAME="housing-predictor"
VERSION="0.0.1"
AUTHOR="Saad"
DESCRIPTION="First Full Project"
PACKAGES=["housing"]

setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=PACKAGES,
    install_requires=get_requirements_list()

)