from setuptools import setup

setup(
    name = "omr",
    version = "0.0.22",
    author = "Greg Miller",
    author_email = "gmill002@gmail.com",
    description = ("Bubble Vision: Optical Mark Reader"),
    long_description = open('README.rst').read(),
    url = "https://github.com/GregoryCMiller/omr", 
    packages = ["omr", "test_omr"],
    package_dir = {"omr": "omr", 
                   "test_omr": "test_omr"},    
    scripts = ["omr/exam.py", ], 
    install_requires = ["numpy >= 1.8.0", 
                        "pillow >= 2.2.1",
                        "openpyxl >= 1.6.2"],
)