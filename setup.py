from setuptools import find_packages, setup


setup(
    name="simplex",
    version="0.0.1",
    packages=find_packages(exclude=["tests.*", "tests", "figs", "examples"]),
    author="Killian Sheriff",
    author_email="ksheriff@mit.edu",
    description="A python package that implement the geometric object of a simplex.",
    long_description="",
    long_description_content_type="text/markdown",
    license="MIT",
    keywords=[],
    url="https://github.com/killiansheriff/simplex",
    install_requires=[
        "numpy",
     
    ],
    include_package_data=True,
)
