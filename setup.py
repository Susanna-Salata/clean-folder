from setuptools import setup, find_namespace_packages

setup(
    name='clean-folder',
    version='1.0.0',
    description='Sorting files in a folder',
    url='https://github.com/Susanna-Salata/clean_folder',
    author='Susanna Salata',
    author_email='susanna.salata@gmail.com',
    license='MIT',
    packages=find_namespace_packages(),
    install_requires=[],
    entry_points={'console_scripts': ['clean-folder = clean_folder.clean:sorter']}
)

