# Walkithot - (Let your thoughts walk)
This repository contains the project done by 2 friends titled Walkithot. It is a blog website aimed at helping to bridge the gap of knowledge and information among ALX students and other tech enthusiast and was done as part of the requirements for graduating in ALX. This project implements a frontend interface for smooth user experience, backend interface, or console, to manage program data. Console commands allow the user to create, update, and destroy objects, as well as manage file storage. Using a system of JSON serialization/deserialization, storage is persistent between sessions.

#### Functionalities of this command interpreter:
* Create a new object (ex: a new User )
* Retrieve an object from a file, a database etc...
* Do operations on objects (count, compute stats, etc...)
* Update attributes of an object
* Destroy an object

## Table of Content
* [Environment](#environment)
* [Installation](#installation)
* [File Descriptions](#file-descriptions)
* [Bugs](#bugs)
* [Authors](#authors)
* [License](#license)


## Environment
This project is interpreted/tested on wsl Ubuntu 22.04 LTS using python3 (version 3.4.3)

## Installation
* Clone this repository: `git clone "https://github.com/KayFrimp/WalkiThot_v1"`
* Access Walkithot directory: `cd AirBnB_clone`
* Run walkithot(interactively): `./console` and enter command
* Run walkithot(non-interactively): `echo "<command>" | ./console.py`
* Run walkithot with a mysql database: ` WALKI_MYSQL_USER=walki_dev WALKI_MYSQL_PWD=walki_dev_pwd WALKI_MYSQL_HOST=localhost WALKI_MYSQL_DB=walki_dev_db WALKI_TYPE_STORAGE=db WALKI_API_HOST=0.0.0.0 WALKI_API_PORT=5000 python3 -m api.v1.app`
* The application should now be accessible at http://localhost:5000.
Contributing
* We welcome contributions! If you'd like to contribute to the WalkiThot project, please follow these steps:

* Fork the repository on GitHub.
* Clone your forked repository locally.
* Create a new branch for your feature or bug fix.
* Make your changes and commit them.
* Push your changes to your fork on GitHub.
* Submit a pull request to the main repository.
* Be sure to follow the project's coding standards and guidelines

## File Descriptions
[console.py](console.py) - the console contains the entry point of the command interpreter. 
List of commands this console current supports:
* `EOF` - exits console 
* `quit` - exits console
* `<emptyline>` - overwrites default emptyline method and does nothing
* `create` - Creates a new instance of`BaseModel`, saves it (to the JSON file) and prints the id
* `destroy` - Deletes an instance based on the class name and id (save the change into the JSON file). 
* `show` - Prints the string representation of an instance based on the class name and id.
* `all` - Prints all string representation of all instances based or not on the class name. 
* `update` - Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file). 

#### `models/` directory contains classes used for this project:
[base_model.py](/models/base_model.py) - The BaseModel class from which future classes will be derived
* `def __init__(self, *args, **kwargs)` - Initialization of the base model
* `def __str__(self)` - String representation of the BaseModel class
* `def save(self)` - Updates the attribute `updated_at` with the current datetime
* `def to_dict(self)` - returns a dictionary containing all keys/values of the instance

Classes inherited from Base Model:
* [blog.py](/models/blog.py)
* [comment.py](/models/comment.py)
* [response.py](/models/response.py)
* [user.py](/models/user.py)

#### `/models/engine` directory contains File Storage class that handles JASON serialization and deserialization :
[file_storage.py](/models/engine/file_storage.py) - serializes instances to a JSON file & deserializes back to instances
* `def all(self)` - returns the dictionary __objects
* `def new(self, obj)` - sets in __objects the obj with key <obj class name>.id
* `def save(self)` - serializes __objects to the JSON file (path: __file_path)
* ` def reload(self)` -  deserializes the JSON file to __objects

#### `/tests` directory contains all unit test cases for this project:
[/test_models/test_base_model.py](/tests/test_models/test_base_model.py) - Contains the TestBaseModel and TestBaseModelDocs classes
TestBaseModelDocs class:
* `def setUpClass(cls)`- Set up for the doc tests
* `def test_pep8_conformance_base_model(self)` - Test that models/base_model.py conforms to PEP8
* `def test_pep8_conformance_test_base_model(self)` - Test that tests/test_models/test_base_model.py conforms to PEP8
* `def test_bm_module_docstring(self)` - Test for the base_model.py module docstring
* `def test_bm_class_docstring(self)` - Test for the BaseModel class docstring
* `def test_bm_func_docstrings(self)` - Test for the presence of docstrings in BaseModel methods

TestBaseModel class:
* `def setUpClass(cls)` - Test that the instatiation of a BaseModel works
* `def test_id(self)` - Test id
* `def test_created_at(self)` - Test created_at is a pub. instance attribute of type datetime
* `def test_updated_at(self)` - Test updated_at is a pub. instance attribute of type datetime
* `def test_to_dict(self)` - Test to_dict method

[/test_models/test_blog.py](/tests/test_models/test_blog.py) - Contains the TestBlogDocs class:
* `def setUpClass(cls)` - Set up for the doc tests
* `def test_pycodestyle(self)` - Test that models/blog.py conforms to PEP8
* `def test_pycodestyle(self)` - Test that tests/test_models/test_blog.py conforms to PEP8
* `def test_title(self)` - Test the type of each variables on blog
* `def test_content(self)` - Test for the blog content

[/test_models/test_city.py](/tests/test_models/test_city.py) - Contains the TestCityDocs class:
* `def setUpClass(cls)` - Set up for the doc tests
* `def test_pep8_conformance_city(self)` - Test that models/city.py conforms to PEP8
* `def test_pep8_conformance_test_city(self)` - Test that tests/test_models/test_city.py conforms to PEP8
* `def test_city_module_docstring(self)` - Test for the city.py module docstring
* `def test_city_class_docstring(self)` - Test for the City class docstring
* ` def test_type(self)` -  Test the type in blog

[/test_models/test_engine/test_file_storage.py](/tests/test_models/test_engine/test_file_storage.py) - Contains the TestFileStorageDocs class:
* `def setUpClass(cls)` - Set up for the doc tests
* `def test_pycodestyle(self)` - Test that models/file_storage.py conforms to PEP8
* `def test_pycodestyle(self)` - Test that tests/test_models/test_file_storage.py conforms to PEP8
* `def test_all(self)` - Test all method

[/test_models/test_comment.py](/tests/test_models/test_comment.py) - Contains the TestPlaceDoc class:
* `def setUpClass(cls)` - Set up for the doc tests
* `def test_comment_pycodestyle(self)` - Test that models/comment.py conforms to PEP8.
* `def test_comment_pycodestyle(self)` - Test that tests/test_models/test_comment.py conforms to PEP8.
* `def test_blog_id(self)` - Test for the blog id
* ` def test_comment(self)` - Test for the comments of users

[/test_models/test_response.py](/tests/test_models/test_response.py) - Contains the TestReviewDocs class:
* `def setUpClass(cls)` - Set up for the doc tests
* ` def test_pycodestyle(self)` - Test that models/response.py conforms to PEP8
* `def test_pycodestyle(self)` - Test that tests/test_models/test_response.py conforms to PEP8
* `def test_subclass(self)` - Test that response is a subclass of basemodel
* ` def test_comment_id(self)` - Test for users comment
* ` def test_reply(self)` - Test for users reply

[/test_models/user.py](/tests/test_models/test_user.py) - Contains the TestUserDocs class:
* `def setUpClass(cls)` - Set up for the doc tests
* `def test_pycodestyle(self)` - Test that models/user.py conforms to PEP8
* `def test_pycodestyle(self)` - Test that tests/test_models/test_user.py conforms to PEP8
* `def test_subclass(self)` - Test that user is a subclass of basemodel
* `def test_id(self)` - Test User's id
* ` def test_email(self)` - Test User's email
* `def test_password(self)` - Test User's password
* `def test_first_name(self)` - Test User's first name 
* `def test_last_name(self)` - Test User's last name 
* ` def test_cohort(self)` - Test User's cohort

## Bugs
No known bugs at this time. 

## Authors
Opeyemi Philip - [Github](https://github.com/debby696) / [Twitter](https://twitter.com/idowuop)  LinkedIn Profile: https://www.linkedin.com/in/philip-opeyemi-37b13814b
Kwabena A. Frimpong - [Github](https://github.com/kayfrimp) / [Twitter](https://twitter.com/kwabenaaddaifr1)                
Final Project Blog Article: https://docs.google.com/document/d/1ltbPpYTxzqz5CUaJLVfKOZnimIpulG0M_ajDgZUWmg8/edit?usp=drive_link

Walkithot
## License     
---
