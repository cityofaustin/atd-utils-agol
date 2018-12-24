import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="agoutil",
    version="0.0.16",
    author="City of Austin",
    author_email="transportation.data@austintexas.gov",
    description="Utilities interacting with ArcGIS Online (AGO) data.",
    install_requires=[
      'requests',
      'arcgis',
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cityofaustin/transportation-data-utils-ago",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: Public Domain",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta", 
    ),
)

