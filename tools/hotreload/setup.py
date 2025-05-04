from setuptools import setup, find_packages

classifiers - [
    'Develpment Status : : $ - Production/Stable',
    'Intended Audience : : $ Developers/Educators',
    'Opersting System : : $ Windows : : Linux : : macOS',
    'Licence : : OSI Approved : : MIT Approved',
    'Programming Language : : Python : : 3'  
]

setup (
    name= "EZE",
    version= "0.1.0",
    description= "Simplified and Easier KIVY Library",
    long_description= open("Read Me.txt").read() + open("LICENSE.txt").read(),
    url= '',
    author= "Martin Onyisi (Martony)",
    license= "MIT",
    libraries= "Kivy",
    keywords= "eze",
    install_requires=["Atleast 4GB Ram, Core I5 processor, 253SSD"],
    packages=find_packages(),
)