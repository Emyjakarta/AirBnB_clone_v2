
## Unit Testing

Unit testing is a software testing method by which individual units of source code, sets of one or more computer program modules together with associated control data, usage procedures, and operating procedures, are tested to determine whether they are fit for use. In procedural programming, a unit is often an entire module, but it can be an individual function or procedure. In object-oriented programming, a unit is often an entire interface, such as a class, but it can be an individual method or function.

## *args and **kwargs

*args and **kwargs are special syntax in Python used in function definitions.

*args is used to send a non-keyworded variable length argument list to the function.
python
```
def test_var_args(f_arg, *argv):
    print("first normal arg:", f_arg)
    for arg in argv:
        print("another arg through *argv:", arg)

test_var_args('yasoob', 'python', 'eggs', 'test')
```
**kwargs allows you to pass keyworded variable length of arguments to a function. You should use **kwargs if you want to handle named arguments in a function.
python
```
def greet_me(**kwargs):
    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value))

greet_me(name="yasoob")
```

## ORM

ORM stands for Object-Relational Mapping. It is a programming technique for converting data between incompatible type systems using object-oriented programming languages. This creates, in effect, a "virtual object database" that can be used from within the programming language.
In an ORM-based system, the database tables are mapped to Python classes, where each row in the table corresponds to an instance of the class. This allows you to work with data as if it were Python objects instead of rows in a table.

Here's a brief overview of how ORMs work:

    Database Abstraction: ORMs provide a layer of abstraction between your application and the underlying database. This means you don't have to write raw SQL queries to interact with the database; instead, you can use the ORM's API to perform CRUD (Create, Read, Update, Delete) operations.

    Object-Oriented Mapping: ORMs map database tables to Python classes, where each class represents a table, and the class attributes represent the columns in the table. This allows you to work with data using an object-oriented approach, which can make your code more readable and maintainable.

    Query Building: ORMs provide a way to build complex database queries using an object-oriented syntax, which can be more intuitive and less error-prone than writing raw SQL.

    Database Portability: ORMs can help make your application more portable across different database management systems (DBMS), as the ORM handles the underlying differences between the DBMS implementations.

    Lazy Loading and Eager Loading: ORMs often provide ways to control how data is loaded from the database, using techniques like lazy loading (loading data only when it's needed) and eager loading (loading related data upfront).

Some popular ORM libraries for Python include SQLAlchemy, Django ORM, and Peewee. By using an ORM, you can focus on writing application-level code rather than worrying about the details of the underlying database implementation, which can improve developer productivity and code maintainability.

## Mapping a Python Class to a MySQL table

In SQLAlchemy, you can map a Python class to a MySQL table using the declarative_base function.
python
```
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)

    def __repr__(self):
       return "<User(name='%s', fullname='%s', nickname='%s')>" % (
                            self.name, self.fullname, self.nickname)
```

## Handling 2 different storage engines with the same codebase
To handle different storage engines (e.g., MyISAM and InnoDB) with the same codebase, you can use conditional logic in your code to handle the differences. For example, you could use different table definitions or different SQL queries depending on the storage engine being used.

Alternatively, you could use an ORM like SQLAlchemy, which provides a layer of abstraction between your application and the underlying database. This allows you to write code that is largely storage engine-agnostic, and the ORM will handle the differences behind the scenes.

Another approach is to use a database abstraction layer (DBAL) like PyMYSQL or MySQL-Connector-Python, which provide a consistent API for interacting with the database, regardless of the storage engine being used.

The specific approach you choose will depend on the complexity of your application and the degree of control you need over the underlying database implementation.
In SQLAlchemy, you can use the create_engine function to create an engine that connects to a specific database. You can then use this engine to create a session that you can use to interact with the database.
python
```
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine1 = create_engine('mysql://user:pass@localhost/db1')
engine2 = create_engine('mysql://user:pass@localhost/db2')

Session1 = sessionmaker(bind=engine1)
Session2 = sessionmaker(bind=engine2)

session1 = Session1()
session2 = Session2()
```

## Environment Variables

Environment variables are a way to store configuration settings for your application. They are accessible from your application at runtime.

In Python, you can use the os module to access environment variables.
python
```
import os

db_host = os.getenv('DB_HOST', 'localhost')
db_user = os.getenv('DB_USER', 'root')
db_pass = os.getenv('DB_PASS', '')
```
In this example, os.getenv is used to get the value of the DB_HOST, DB_USER, and DB_PASS environment variables. If these environment variables are not set, the default values 'localhost', 'root', and '' are used.
