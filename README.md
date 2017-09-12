# python-packaging

#### If you are frustrated by organizing your Python packages with all modules in the same directory, along with the setup.py script, you are the right place.

The setup.py script in the `deploy` directory allows you to generate and install a structured Python package with pip.
It provides two useful behaviours, usually not included in standard setup scripts.
The first is the ability to produce a Python library which includes a main package and its sub-packages as reported below.
The second is the use of Cython for compiling the code of the output library.
Below you can find two different structures that can be used with the supplied `setup.py`. The first one corresponds to a simple project which includes also sub-packages (NOTE: it is possible to handle projects without sub-packages as it is possible to add as many nested sub-packages as you like. 
Remember, you must add the `__init__.py` file in each package/sub-package folder, otherwise the included modules will not be added to the output library.
The second example allows for more complex library generation in particular when you want the add different packages under the same 
`namespace`. 

### First Example
```
git-module
├── README.md    
│
├───bin
│   ├── test_package
│   │   ...
│   
├───deploy
│   ├── setup.py
│   
├───package_name
│   ├── __init__.py
│   ├── Module1.py
│   │   ...
│   ├───sub_package_name1
│       ├── __init__.py
│       ├── ...
│
│   ...
```
### Second Example 
```
git-namespace
├── README.md
├── package1
│   ├── deploy
│   │   └── setup.py
│   └── namespace
│       ├── __init__.py
│       └── package_name1
│           └── __init__.py
├── package2
│   ├── bin
│   │   └── package1_test.py
│   ├── deploy
│   │   └── setup.py
│   └── namespace
│       ├── __init__.py
│       └── package_name2
│           ├── __init__.py
│           ├── Module1.py
│           └── Module2.py
```


## Usage 

First of all, you need to create a project with a directory structure similar to those reported above.   
You can add as many directories as you need in the root as the `bin` in our example. The mandatory elements are `deploy` and `package_name`, in the first example, and also the directory `namespace`, in the second example. 

Copy the `setup.py` provided in this project into the folder `deploy`.
Edit each of them, set the variable `PACKAGE_NAME` with the name of the package (`package_nameX`). 
If you are using a directory structure as in the second example `PACKAGE_NAME` must be set to `namespace.package_nameX` e.g. `namespace.package1`.

### Prepare and Install the package

To generate and install a package run the following commands from the `deploy` directory.

* If present, remove old copies/versions of the package:

```
pip uninstall $PACKAGE_NAME
```

* Create a binary distribution package which then can be installed with `pip`:

```
python setup.py bdist_wheel --universal
```

* Install the package:

```
pip install dist/$PACKAGE_LONG_NAME.whl
```

The script has been tested with:
- Python 2.7.6
- Cython 0.23.1
- pip 1.5.4
- setuptools 3.3
