from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="geography_toolkit",  
    version="0.1.0",  
    author="BABABODI Zakiyou",
    author_email="zakiyoubababodi@gmail.com",
    description="Un package Python pour la géographie",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Zakiyou/world_geo_data.git",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
