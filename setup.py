from setuptools import setup

# sudo rm -rf build/ dist/ tsoncli.egg-info/ /__pycache__/
# python setup.py bdist_wheel
# python3 -m twine upload dist/*
def readme():
    with open('README.md') as f:
        return f.read()

setup(name='tsoncli',
      version='0.3',
      description='TSON Command Line Interface',
      long_description=readme(),
      scripts=['bin/tson-cli'],
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Topic :: Text Processing :: Linguistic',
      ],
      python_requires='>=3.6',
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
