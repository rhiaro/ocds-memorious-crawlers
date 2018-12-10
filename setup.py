from setuptools import setup, find_packages


setup(
    name='ocds-memorious-crawlers',
    version='0.1',
    author='Amy Guy',
    author_email='amy@rhiaro.co.uk',
    url='https://github.com/rhiaro/ocds-memorious-crawlers',
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'examples', 'test']),
    namespace_packages=[],
    package_data={
        'ocds-memorious-crawlers': ['config/*.yml']
    },
    zip_safe=False,
    install_requires=[
        'memorious >= 0.4',
        'xlrd',
        'attrs',
    ],
    entry_points={
        'memorious.plugins': [
            'ocds-memorious-crawlers = crawlers:init'
        ]
    }
)