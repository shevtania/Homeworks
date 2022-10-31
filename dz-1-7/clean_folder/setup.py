from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='0.1',
    description='Code for sorting trash',
    url='https://github.com/shevtania/Homeworks/blob/main/sort.py',
    author='shev',
    author_email='shevtania@outlook.com',
    license='MIT',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['clean-folder = clean_folder.clean:input_dir']}
)