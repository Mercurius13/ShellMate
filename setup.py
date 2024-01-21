from setuptools import setup, find_packages

setup(
    name='ShellMate',  # Replace with your package's name
    version='1.0.0',  # Replace with your package's version
    author='Siddhant',  # Replace with your name
    author_email='siddhant@zodevelopers.com',  # Replace with your email
    description='ShellMate: A GPT-Powered CLI Tool for Explaining and Finding Shell Commands',  # Provide a short description
    long_description=open('readme.md').read(),  # Long description read from the README.md
    long_description_content_type='text/markdown',  # Markdown is supported
    url='https://github.com/SidmoGoesBrrr/ShellMate',  # Replace with the URL of your project
    packages=find_packages(),  # Automatically find packages in the project
    install_requires=[
        # List your project's dependencies here
        # e.g., 'requests', 'openai'
    ],
    entry_points={
        'console_scripts': [
            'shellmate=shellmate_module.main:main',  # Adjust to your package structure
        ],
    },
    classifiers=[
        # Choose appropriate classifiers from https://pypi.org/classifiers/
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Minimum version requirement of the python
)
