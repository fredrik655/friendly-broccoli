from distutils.core import setup, Extension

module1 = Extension(name='my_c_module',
                    sources=['c_test_2.c'],
                    include_dirs=[], # list of directories to search for C/C++ header files
                    library_dirs=[], # list of directories to search for static libraries
                    runtime_library_dirs=[], # list of directories to search for shared libraries
                    libraries=[] # list of library names
                    )

setup(name = 'my_c_module',version = '1.0',description = '...',ext_modules = [module1])