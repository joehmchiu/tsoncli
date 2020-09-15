from setuptools import setup

# python setup.py bdist_wheel
# sudo rm -rf build/ dist/ tsoncli.egg-info/ /__pycache__/
def readme():
    with open('README.md') as f:
        return f.read()

setup(name='tsoncli',
      version='0.1',
      description='TSON Command Line Interface',
      long_description=readme(),
      scripts=['bin/tson-cli'],
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Topic :: Text Processing :: Linguistic',
      ],
      keywords='TSON tson cli',
      url='http://github.com/joehmchiu/tsoncli',
      author='Joe Chiu',
      author_email='joehmchiu@gmail.com',
      license='MIT',
      packages=['tsoncli'],
      install_requires=[
          'markdown',
      ],
      test_suite='nose.collector',
      tests_require=['nose', 'nose-cover3'],
      include_package_data=True,
      zip_safe=False
)
