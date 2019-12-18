import sys

from setuptools import find_packages, setup

## base requirements
install_requires = open("requirements.txt").read().strip().split("\n")

extras = {
    "dev": [
        "black",
        "graphviz >= 0.8, < 0.14",
        "jinja2 >= 2.0, < 3.0",
        "mypy >= 0.600, < 0.800",
        "Pygments >= 2.2, < 3.0"
    ]
}

if sys.version_info < (3, 6):
    extras["dev"].remove("black")

extras["all_extras"] = sum(extras.values(), [])


setup(
    name="prefect-legacy-api-docs",
    install_requires=install_requires,
    extras_require=extras,
    scripts=[],
    include_package_data=True,
    python_requires=">=3.5.2",
    description="The Prefect Core automation and scheduling engine.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://www.github.com/PrefectHQ/prefect",
    license="Apache License 2.0",
    author="Prefect Technologies, Inc.",
    author_email="help@prefect.io",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development :: Libraries",
        "Topic :: System :: Monitoring",
    ],
)
