from setuptools import setup, find_packages

with open('README.md') as f:
    long_description = f.read()

setup(
    name='aio-prometheus-client',
    version='0.0.3',
    packages=find_packages(include=['aio_prometheus_client']),
    python_requires='>3.10.0',

    install_requires=[
        'httpx',
    ],

    license='LGPL',
    url='https://github.com/lexdene/python-aio-prometheus-client',
    description='Prometheus Http Client for Asyncio',
    long_description_content_type='text/markdown',
    long_description=long_description,
)
