import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="blimp-utils",
    version="1.0.0",
    author="Eli Ferrara",
    author_email="eli.ferrara256@gmail.com",
    description="A Python library for the Falcon Flight custom embedded flight controller board.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Ballistyxx/blimp-utils",
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Hardware :: Hardware Drivers",
    ],
    python_requires='>=3.9',
    install_requires=[
        "numpy",
        "RPi.GPIO",
        "smbus2",
    ],
    extras_require={
        "dev": [
            "sphinx>=4.0.0",
            "sphinx-rtd-theme>=1.0.0",
            "myst-parser>=0.15.0",
            "flake8>=3.9.0",
            "ruff>=0.1.0",
            "pytest>=6.0.0",
        ]
    },
    include_package_data=True,
)
