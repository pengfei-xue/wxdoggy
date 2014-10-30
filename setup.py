from setuptools import setup, find_packages


setup(name='Wxdoggy',
    version='1.0.0',
    description='Weixin API wrapper',
    author='Pengfei.X',
    author_email='pengphy@gmail.com',
    packages=['wxdoggy',],
    install_requires = ['requests>=2.4.3'],
    license = 'BSD',
    keywords = 'weixin api',
)
