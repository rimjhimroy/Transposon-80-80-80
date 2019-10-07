
import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='transposon80-80-80',  
     version='0.1',
     scripts=['full_blast','query_coverage.py'] ,
     author="Rimjhim Roy Choudhury",
     author_email="rimjhim.roy.ch@gmail.com",
     description="A package to blast transposons against a reference TE database and filter them according to the 80-80-80 rule (Wicker et al. 2007, NRG)",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/rimjhimroy/Transposon80-80-80",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
