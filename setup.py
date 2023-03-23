from setuptools import setup, find_packages
def get_requirements():
    with open('requirements.txt') as f:
        
        R=f.read().splitlines()
        R.remove('-e .')
        print(R)
        return R
setup(
    name='ml project',
    version='0.1',
    description='by baheeg.com',
    author='Ahmed Khorshid',
    packages=find_packages(),
    install_requires=get_requirements(),
    
       
    )