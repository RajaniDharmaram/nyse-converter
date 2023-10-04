from setuptools import setup

setup(
    name='nyseconverter',
    version='0.1',
    description='NYSE Converter',
    url='https://github.com/RajaniDharmaram/nyse-converter',
    author='Rajani Dharmaram',
    author_email='rajanidharmaram03@gmail.com',
    license='MIT',
    packages=['nyseconverter'],
    install_requires=[
        'dask[complete]<=2023.9.2',
    ],
    entry_points={
        'console_scripts': ['nysec=nyseconverter:main'],
    },
    zip_safe=False)
