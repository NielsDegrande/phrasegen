"""Setup script for Phrasegen."""

from setuptools import setup, find_packages


def read_file(file_name: str) -> str:
    """Read file and return its content.

    :param file_name: Name of file to be read.
    :return: Content of file, unprocessed.

    """
    with open(file_name, "r") as file_:
        return file_.read()


setup(
    name="phrasegen",
    version="2.0.0",
    description="Generate random phrases, for fun.",
    long_description=read_file("README.md"),
    long_description_content_type="text/markdown",
    url="https://github.com/NielsDegrande/phrasegen.git",
    # Overview: https://pypi.python.org/pypi?:action=list_classifiers.
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3.7",
    ],
    keywords=["phrase", "generator"],
    packages=find_packages(exclude=("tests",)),
    platforms=["Any"],
    python_requires=">=3.7",
    install_requires=read_file("requirements.txt").splitlines(),
    # Entangles setup.py with development concerns: use Tox instead.
    extras_require={"dev": read_file("requirements_dev.txt").splitlines()},
    include_package_data=True,
    entry_points={"console_scripts": ["phrasegen = phrasegen.cli:main"]},
    project_urls={"Source": "https://github.com/NielsDegrande/phrasegen.git"},
    license="Other/Proprietary",
)
