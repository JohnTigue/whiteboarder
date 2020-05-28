import setuptools

with open("Readme.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="whiteboarder", 
    version="0.0.1",
    author="John Tigue",
    author_email="john@tigue.com",
    description="A two-bit image processor",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/johntigue/whiteboarder",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

