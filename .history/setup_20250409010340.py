from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    with open(file_path, 'r') as file:
        requirements = [line.strip() for line in file if line.strip()]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name='my_package',
    version='0.1',
    author='Ankit Gochhayat',
    author_email='ankit.gochhayat2004@gmail.com',
    description='Customer segmentation package',
    license='MIT',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    python_requires='>=3.7',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)
