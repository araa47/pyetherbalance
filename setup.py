from setuptools import setup 

requirements = ["requests"]

def readme():
    with open('README.md') as f:
        return f.read()


setup(name='pyetherbalance',
      version='0.0.1',
      description='Lightweight Module to get Ethereum and ERC20 token balances',
      long_description=readme(),
      long_description_content_type='text/markdown',
      keywords="ethereum",
      url='http://github.com/araa47',
      author='Akshay Ramasubramanian',
      author_email='araa@connect.ust.hk',
      license='MIT',
      packages=['pyetherbalance'],
      install_requires=requirements,
      zip_safe=False,
      classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries ',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)