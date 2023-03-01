from setuptools import setup, find_packages

setup(
    name="dirnamer",
    version="0.1",
    author="Matthew Barton",
    author_email="99matthewbarton@gmail.com",
    description="Renames everything in a directory to the folder name or supplied name plus ID (ie. folder_name1, folder_name2)",
    packages = ["dirnamer"],
    entry_points = {
        "console_scripts": ['dirnamer = dirnamer.dirnamer:main']
    },
)
