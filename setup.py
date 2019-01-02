from setuptools import setup, find_packages


setup(
    name='crawlers',
    version='0.1',
    author='Amy Guy',
    author_email='amy@rhiaro.co.uk',
    url='https://github.com/rhiaro/ocds-memorious-crawlers',
    license='MIT',
    packages=find_packages('src'),
    package_dir={'': 'crawlers/src'},
    namespace_packages=[],
    package_data={
        'ocds-memorious-crawlers': ['config/*.yml']
    },
    zip_safe=False,
    install_requires=[
        'memorious >= 0.8.0'
    ],
    entry_points={}
)