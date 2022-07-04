import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="smwct",                     
    version="0.0.1",                        
    author="b4b4",                     
    description="Search and Moderation Wizard for the Computer Tree.",
    long_description=long_description,      
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),    
    classifiers=[
        "Programming Language :: Python :: 3"
    ],                                      
    python_requires='>=3.10',                
    py_modules=["src/smwct"],
    install_requires=[],
              
)