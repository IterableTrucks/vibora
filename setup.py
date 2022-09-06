import re
import pathlib
from setuptools import setup, Extension, find_packages
from Cython.Build import cythonize

# Loading version
here = pathlib.Path(__file__).parent
txt = (here / 'vibora' / '__version__.py').read_text()
version = re.findall(r"^__version__ = '([^']+)'\r?$", txt, re.M)[0]


setup(
    name="vibora",
    version=version,
    description='Fast, asynchronous and efficient Python web framework',
    author='Frank Vieira',
    author_email='frank@frankvieira.com.br',
    url='https://vibora.io',
    license='MIT',
    python_requires='>=3.6',
    classifiers=[
        'Intended Audience :: Developers',
        'Development Status :: 4 - Alpha',
        'Environment :: Web Environment',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6'
    ],
    extras_require={
        'dev': ['flake8', 'pytest', 'tox'],
        'fast': ['ujson', 'uvloop']
    },
    ext_modules=cythonize([
        Extension(
            "vibora.parsers.*",
            [
                "vibora/parsers/*.pyx",
                "vendor/http-parser-2.8.1/http_parser.c",
            ],
            extra_compile_args=['-O3'],
            include_dirs=['.', '/git/vibora/vibora']
        ),
        Extension(
            "vibora.router.router",
            ["vibora/router/router.py"],
            extra_compile_args=['-O3'],
            include_dirs=['.']
        ),
        Extension(
            "vibora.responses.responses",
            ["vibora/responses/responses.pyx"],
            extra_compile_args=['-O3'],
            include_dirs=['.']
        ),
        Extension(
            "vibora.protocol.*",
            ["vibora/protocol/*.pyx"],
            extra_compile_args=['-O3'],
            include_dirs=['.']
        ),
        Extension(
            "vibora.request.request",
            ["vibora/request/request.pyx"],
            extra_compile_args=['-O3'],
            include_dirs=['.']
        ),
        Extension(
            "vibora.cache.cache",
            ["vibora/cache/cache.py"],
            extra_compile_args=['-O3'],
            include_dirs=['.']
        ),
        Extension(
            "vibora.headers.headers",
            ["vibora/headers/headers.py"],
            extra_compile_args=['-O3'],
            include_dirs=['.']
        ),
        Extension(
            "vibora.schemas.extensions.*",
            ["vibora/schemas/extensions/*.pyx"],
            extra_compile_args=['-O3'],
            include_dirs=['.', 'vibora/schemas']
        ),
        Extension(
            "vibora.components.components",
            ["vibora/components/components.pyx"],
            extra_compile_args=['-O3'],
            include_dirs=['.']
        ),
        Extension(
            "vibora.multipart.parser",
            ["vibora/multipart/parser.pyx"],
            extra_compile_args=['-O3'],
            include_dirs=['.']
        )
    ]),
    packages=find_packages()
)
