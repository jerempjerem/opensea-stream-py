from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = ['pip>=21.1', 'termcolor>=1.1.0', 'discord-webhook>=0.16.3', 'realtime>=0.0.4']

test_requirements = ['pytest>=3', ]

setup(
    author="Jerem",
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Environment :: Web Environment',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet',
        'Topic :: Internet :: WWW/HTTP :: HTTP Servers',
        'Topic :: Office/Business :: Financial',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities'
        
    ],
    description="A python SDK for receiving updates from the OpenSea Stream API - pushed over websockets",
    install_requires=requirements,
    license="MIT license",
    long_description=readme,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords=['opensea', 'nft', 'non fungible token', 'crypto', 'stream'],
    maintainer='Jerem',
    name='opensea-stream',
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    test_suite='tests',
    url='https://github.com/jerempjerem/opensea-stream-py',
    project_urls={
        'Source': 'https://github.com/jerempjerem/opensea-stream-py'
    },
    version='0.1.0',
    zip_safe=False,
)

