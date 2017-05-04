# Copyright 2017 Yonder srl. All Rights Reserved.

from Cython.Build import cythonize
import os
import shutil
from setuptools import Extension, find_packages, setup


# MODIFY HERE
PACKAGE_NAME = 'package_name'
VERSION = '0.0.1'
INSTALL_REQUIRES = [
    'setuptools >= 3'
]
DESCRIPTION = 'This package ....'
AUTHOR = 'Yonder s.r.l.'
LICENSE = 'Copyright 2017 Yonder srl. All Rights Reserved.'
#


def build_package_tree_structure(src_dir, dst_dir):
    package_tree_structure = [src_dir]

    if not os.access(dst_dir, os.F_OK):
        os.mkdir(dst_dir)

    for filename in os.listdir(src_dir):
        source = os.path.join(src_dir, filename)
        destination = os.path.join(dst_dir, filename)
        if filename in bare_copy_file_list:
            shutil.copyfile(source, destination)
        if os.path.isdir(source):
            package_tree_structure += \
                build_package_tree_structure(source, destination)
        if filename not in bare_copy_file_list and filename.endswith('.py'):
            shutil.copyfile(
                source, os.path.join(dst_dir, filename.replace('.py', '.pyx')))

    return package_tree_structure


def build_extensions(dst_dir):
    extensions = []
    for filename in os.listdir(dst_dir):
        destination = os.path.join(dst_dir, filename)
        if os.path.isdir(destination):
            extensions += build_extensions(destination)
        if filename.endswith('.pyx'):
            extensions += [Extension(
                str(os.path.join(dst_dir, filename.split('.')[0])),
                [destination]
            )]
    return extensions


def find_and_build_package_list():
    return [package.replace('.', '/') for package in find_packages()]


bare_copy_file_list = ['__init__.py']
source_base_dir = os.path.join('../', PACKAGE_NAME.split('.')[0])
dest_base_dir = os.path.join('./', PACKAGE_NAME.split('.')[0])


_ = build_package_tree_structure(source_base_dir, dest_base_dir)


extensions = build_extensions(dest_base_dir)


setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    license=LICENSE,
    package_dir={PACKAGE_NAME: PACKAGE_NAME},
    packages=find_and_build_package_list(),
    ext_modules=cythonize(extensions),
)
