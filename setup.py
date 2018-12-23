import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="CENT110",
    version="1.0.0",
    author="Craig Opie",
    author_email="craigopie@gmail.com",
    description="Complete Course Work - 2018.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CraigOpie/CENT110",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
