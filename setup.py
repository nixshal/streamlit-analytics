from pathlib import Path
import re
from setuptools import setup

here = Path(__file__).resolve().parent

# Read version from streamlit_analytics/__init__.py
version_re = r"^__version__ = ['\"]([^'\"]*)['\"]"
init_text = (here / "streamlit_analytics" / "__init__.py").read_text()
version = re.findall(version_re, init_text)[0]

# Read README.md.
readme = (here / "README.md").read_text()

setup(
    name="streamlit-analytics",
    version=version,
    author="Johannes Rieke",
    author_email="johannes.rieke@gmail.com",
    description="Track & visualize user inputs to your streamlit app",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/jrieke/streamlit-analytics",
    license="MIT",
    python_requires=">=3.6",
    install_requires=["streamlit"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
    ],
)
