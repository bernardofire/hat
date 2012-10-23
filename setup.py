from setuptools import setup, find_packages
import os

version = '0.0.1'
here = os.path.abspath(os.path.dirname(__file__))
long_description = open(os.path.join(here, 'README.mkd')).read()

setup(name='hat',
      version=version,
      description='highlighted cat with pygments',
      long_description=long_description,
      classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Utilities'
      ],
      keywords='highlight cat',
      author='Bernardo B. Marques',
      author_email='bernardo.fire@gmail.com',
      url='http://github.com/bernardofire/hat',
      license='MIT',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'pygments'
      ],
      entry_points="""
      [console_scripts]
      hat = hat:hat
      """,
      )
