from setuptools import setup, find_packages
setup(
    name = "test",
    version = "0.1",
    author = "hongjin.cao",
    author = "hongjin.cao@qunar.com",
    url = "http://gitlab.corp.qunar.com/hongjin.cao/newproject/tree/master",
    packages=find_packages(),
    install_requires = ['requests']
)

# 引用的package写在install_requires中。

