import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__verision__ = "0.0.0"

REPO_NAME = "Quality-Assuarance-Machine-Learning-Project-with-MLFLOW"
AUTHOR_USER_NAME = "AcheampongStephen"
SRC_REPO = "mlproject"
AUTHOR_EMAIL = "acheampongstephen392024@gmail.com"

setuptools.setup(
    name=REPO_NAME,
    version=__verision__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Quality Assurance Machine Learning Project with Mlflow",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)
