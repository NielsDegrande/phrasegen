from setuptools import setup, find_packages

# Add development requirement here.
dev_requirements = [
    "black",
    "coverage",
    "flake8",
    "flake8-blind-except",
    "flake8-bugbear",
    "flake8-builtins",
    "flake8_commas",
    "flake8-docstrings",
    "flake8-import-order",
    "flake8-logging-format",
    "flake8-module-name",
    "flake8-rst-docstrings",
    "mypy",
    "pylint",
    "pytest",
]

# Read README.md to add as long_description.
with open("README.md") as file_:
    long_description = file_.read()

# Read the production requirements.
with open("requirements.txt") as file_:
    requirements = file_.read().splitlines()

# Read the development requirements.
with open("requirements_dev.txt") as file_:
    dev_requirements = file_.read().splitlines()

setup(
    name="phrasegen",
    version="1.0.0",
    description="Generate random phrases, for fun.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/NielsDegrande/phrasegen.git",
    # Overview: https://pypi.python.org/pypi?:action=list_classifiers.
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3.7",
    ],
    keywords=["phrase", "generator"],
    packages=find_packages(include=("phrasegen",)),
    python_requires=">=3.7",
    install_requires=requirements,
    extras_require={"dev": dev_requirements},
    include_package_data=True,
    entry_points={"console_scripts": ["phrasegen = main:main"]},
    project_urls={"Source": "https://github.com/NielsDegrande/phrasegen.git"},
)
