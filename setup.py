from setuptools import setup, find_packages

setup(
    name="authorizer",
    version="0.0.5",
    packages=find_packages(),
    install_requires=["pycryptodome"],
    author="Aman Kalmanbetov",
    author_email="kalmanbetovaman@gmail.com",
    description="Authorizer for Payments Gateway server and Payments Gateway clients",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://@github.com/kalmanbetov/authorizer",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
