from setuptools import setup, find_packages

setup(
    name="authorizer",
    version="0.0.4",
    packages=find_packages(),
    install_requires=["pycryptodome"],
    author="Andy",
    author_email="andy@dont_spam_me.co",
    description="A simple example private package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/nydasco/package_publishing",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
