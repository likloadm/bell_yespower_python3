from setuptools import setup, Extension

bell_yespower_module = Extension('tide_yespower',
                            sources = ['yespower-module.c',
                                       'yespower.c',
                                       'yespower-opt.c',
                                       'sha256.c'
                                       ],
                            extra_compile_args=['-O2', '-funroll-loops', '-fomit-frame-pointer'],
                            include_dirs=['.'])

setup (name = 'tide_yespower',
       version = '1.0.3',
       author_email = 'liklo.adm@gmail.com',
       author = 'liklo_adm',
       url = 'https://github.com/likloadm/tide_yespower_python3',
       description = 'Bindings for yespower-1.0 proof of work used by tidecoin',
       ext_modules = [bell_yespower_module])
