from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
   name='txgen',
   version='0.1.0',  
   description='Transaction Generator',
   long_description=long_description,
   long_description_content_type="text/markdown",
   author='Your Name',
   author_email='you@domain.com',
   packages=find_packages(),
   install_requires=[
       'web3',
       'requests',
       'eth-account',
       'python-dotenv'
   ],
   entry_points = {
        'console_scripts': [
            'txgen=app:main'
        ]
    }
)
