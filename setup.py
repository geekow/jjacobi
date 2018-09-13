import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name="jjacobi",
    version="0.0.1",
    author="Jean Jacobi",
    author_email="jean.jacobi@live.de",
    description="Jean Jacobi Website",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/geekow/jjacobi",
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Undefined at the moment",
        "Operating System :: OS Independent",
    ],
    entry_points={  # Optional
        'console_scripts': [
            'jjacobi=jjacobi.__main__:cli',
        ],
    }
)
