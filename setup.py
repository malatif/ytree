from setuptools import setup

setup(name="simple_tree",
      version="1.0.0.dev1",
      description="Merger tree and related utilites for Gadget FOF/SUBFIND catalogs and consistent trees outputs.",
      author="Britton Smith",
      author_email="brittonsmith@gmail.com",
      license="BSD",
      keywords=["simulation", "merger-tree", "astronomy", "astrophysics"],
      url="http://bitbucket.org/brittonsmith/simple_tree",
      packages=["simple_tree"],
      include_package_data=True,
      classifiers=[
          "Development Status :: 2 - Pre-Alpha",
          "Environment :: Console",
          "Intended Audience :: Science/Research",
          "Topic :: Scientific/Engineering :: Astronomy",
          "License :: OSI Approved :: BSD License",
          "Operating System :: MacOS :: MacOS X",
          "Operating System :: POSIX :: AIX",
          "Operating System :: POSIX :: Linux",
          "Natural Language :: English",
          "Programming Language :: Python :: 2",
          "Programming Language :: Python :: 2.7",
          ],
          install_requires=['yt', 'h5py', 'numpy'],
      )
