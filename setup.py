import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="scihub.py-jennyfothergill", # Replace with your own username
    version="0.0.1",
    description="A pip installable fork of https://github.com/zaytoun/scihub.py",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zaytoun/scihub.py",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

