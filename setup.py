from setuptools import setup, find_packages

setup(
    name='py3sort',
    version='0.1.8',
    packages=find_packages(),
    install_requires=[],
    author='Ashhad Ahmed',
    author_email='ashhadahmed776@gmail.com',
    description='A Python package providing efficient sorting algorithms like Bubble Sort, Insertion Sort, Merge Sort, Selection Sort, Heap Sort, and Quick Sort.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Ashhad776/py3sort',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
