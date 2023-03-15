### Airbnb Clone

#### Description
> This is the first phase of the Airbnb clone: The Console.
> This repository holds a Command Interpreter that makes backend operations
> easier.
> This repository also holds the base classes (i.e the BaseModel class) and
> various other classes that inherits from it (e.g User,Place), and also a storage file that
> temporary holds operation data in place of a Database.
> The Command Interpreter, like a shell, can be activated, take in user input
> and perform certain tasks in manipulating object instances.

#### How to use the Command Interpreter
---
| Commands | Sample Usage                       | Functionality                          |
| -------- | ---------------------------------  | -------------------------------------- |
| `help`   | `help`                             | display all commands available         |
| `help`   |  `help command`                    | displays information about the command |
| `create` | `create <class>`                   | creates a new object                   |
| `show`   | `show User 123-323`                | retrieves an object from the database  |
| `show`   | `User.show("123-454")`             | does the same as above                 |
| `update` | `update User 2223 name "John"`     | updates attribute of an object         |
| `update` | `User.update("22", "name", "john")`| does the same as above                 |
| `all`    | `User.all()`                       | displays all objects in class          |
| `destroy`| `User.destroy(123-123)`            | deletes specified object               |
| `count`  | `User.count()`                     | returns count of objects in class      |
| `quit`   | `quit`                             | exits                                  | 
| `EOF`    | `EOF`                              | prints a new line and exits            |
| `clear`  | `clear`                            | clear screen                           |

#### Installation
```
git clone git@github.com:Sylvan452/AirBnB_clone.git
cd AirBnB_clone
```

#### Usage
Interactive Mode
```
$ ./console.py
(hbnb)help

Documented commands (type help <topic>):
========================================
EOF  all  clear  count  create  destroy  help  quit  show  update

(hbnb)quit
$
```
Non Interactive Mode
```
$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  all  clear  count  create  destroy  help  quit  show  update

(hbnb)
```

### Environment
* Language: Python3
* OS: Ubuntu 20.04 LTS
* Style guidelines: [Pycodestyle (version 2.8)](https://pycodestyle.pycqa.org/en/2.8.0/)
