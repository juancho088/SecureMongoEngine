from setuptools import setup, find_packages
import os

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name = "SecureMongoEngine",
    version = "0.1",
    packages = find_packages(),
    install_requires = ['mongoengine>=0.8.7','pycrypto>=2.6.1'],

    # metadata for upload to PyPI
    author = "Juan Urrego",
    author_email = "js.urrego@novcat.co",
    description = "It is a library for MongoEngine that you can use to encrypt certain fields of your models.",
    long_description = README,
    license = "Apache License",
    keywords = "mongo mongoengine python secure encryption cypher pycrypto",
    url = "https://github.com/juancho088/SecureMongoEngine",   
)

