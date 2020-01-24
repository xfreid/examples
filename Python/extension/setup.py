from distutils.core import setup, Extension

def main():
    setup(name="fei_pe",
          version="1.0.0",
          description="Python interface for fei's C++ extension library functions",
          author="fei",
          author_email="fei@gmail.com",
          ext_modules=[Extension("fei_pe", ["hello_world.cpp"])])

if __name__ == "__main__":
    main()
