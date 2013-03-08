import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
CHANGES = open(os.path.join(here, 'HISTORY.rst')).read()

requires = [
    'pyramid',
    'skosprovider>=0.1.2'
    ]

tests_requires = [
    'nose',
    'coverage'
    ]

testing_extras = tests_requires + []

setup(name='pyramid_skosprovider',
      version='0.1.0-dev',
      license='MIT',
      description='Integration of skosprovider in pyramid',
      long_description=README + '\n\n' +  CHANGES,
      classifiers=[
        'Intended Audience :: Developers',
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Framework :: Pyramid',
        ],
      author='Koen Van Daele',
      author_email='koen_van_daele@telenet.be',
      url='https://github.com/koenedaele/pyramid_skosprovider',
      keywords='pyramid skos skosprovider',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires = requires,
      tests_require = tests_requires,
      extras_require = {
        'testing': testing_extras
        },
      test_suite='pyramid_skosprovider',
      )