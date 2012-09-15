try:
    import setuptools
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
from setuptools import setup, find_packages

version = '0.0.1'
readme = open('README.rst').read()

setup(name='hat',
      version=version,
      description='Highlight for cat and git diff',
      long_description=readme,
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.6',
          'Topic :: Software Development :: Documentation',
          'Topic :: Software Development :: Libraries'
      ],
      keywords='cat highlight git diff',
      author='Bernardo Barreto Marques',
      author_email='bernardo.fire@gmail.com',
      url='www.github.com/bernardofire/hat',
      license='MIT License',
      packages=find_packages()
      )
