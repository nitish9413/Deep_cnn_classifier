import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "deepClassifier"
AUTHOR_USERNAME = "nitish9413"
SRC_REPO = "deepClassifier"
AUTHOR_EMAIL = "nitishkatkade94@gmail.com"

setuptools.setup(
    name=f"{SRC_REPO}",
    version=__version__,
    author=f"{AUTHOR_USERNAME}",
    author_email=f"{AUTHOR_EMAIL}",
    description="A package for training deep learning models for image classification",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USERNAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USERNAME}/{REPO_NAME}/issues",
    }
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)