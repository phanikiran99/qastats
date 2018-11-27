import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="repPDF",
    version="0.0.1",
    author="Phanikiran Siddineni",
    author_email="phanikiran@gmail.com",
    description="A PDF generator binder package using ReportLab",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/phanikiran/qastats/reppdf",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)