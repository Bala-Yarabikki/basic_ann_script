from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="src",
    version="0.0.1",
    author="bala",
    description="A small package for ANN implementation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Bala-Yarabikki/basic_ann_script.git",
    author_email="balachowdary777@gmail.com",
    packages=["src"],
    python_requires=">=3.7",
    install_requires=[
        'matplotlib',
        'tensorflow',
        'matplotlib',
        'numpy',
        'pandas',
        'seaborn'

    ]
)
