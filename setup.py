from setuptools import setup

with open("README.md", "r") as arq:
    readme = arq.read()

setup(
    
    name = 'SapFlowSavvy',
    version = '0.3',
    author = 'Nathan Almeida',
    author_email = 'neitan96@outlook.com',
    license='GPLv3',
    packages = ['PySavvyApi'],
    description = 'Toolkit de automatização para SAP Gui',
    long_description = readme,
    long_description_content_type="text/markdown",
    keywords='sap sapgui sapscript',
    url = 'https://github.com/Neitan96/SAPFlowSavvy',
    install_requires=['win32com', 'pywinauto', 'pymsgbox']
)