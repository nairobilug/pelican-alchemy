from setuptools import setup


setup(
    name='alchemy',
    version='2.2',
    description='A functional, clean, responsive Pelican theme',
    url='https://github.com/nairobilug/pelican-alchemy',
    author='Nairobi GNU/Linux Users Group',
    license='MIT',
    platforms='any',
    entry_points={},
    packages=['alchemy'],
    include_package_data=True,
    install_requires=[
        'pelican',
    ],
    zip_safe=False,
)
