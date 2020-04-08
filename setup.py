from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    long_description = readme_file.read()

setup(
    name='DirForcer',
    version='1.0',
    description='A brute forcing tool for finding directories on a website',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    python_requires="~=3.5",
    url='',
    license='Apache',
    classifiers=[
        'Environment :: Console',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    author='Ada Donder',
    author_email='adadonderr@gmail.com',
    keywords="Directory Brute Forcer"
)
