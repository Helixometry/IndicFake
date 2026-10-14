from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="IndicFake",
    version="1.0.0",
    author="Girish, Mohd Mujtaba Akhtar, Orchid Chetia Phukan, Arun Balaji Buduru",
    description="Neural Audio Codec Deepfakes in Indic Languages with SATYAM",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Helixometry/IndicFake",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
