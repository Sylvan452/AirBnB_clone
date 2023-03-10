git clone https://github.com/Preshfile/AirBnB_clone### Project Description
> This is the Part I of the AirBnB project. We worked on the backend of the project, using the console as an interface with the help of python's cmd module.

> The python objects(data) generated were stored in a json file which is to be accessed wth the help of python's json module.

### Description of the command interpreter
> The interface of the project is synonymous to a bash shell. However, the difference is in it's limited number of commands which were exclusively defined for this project - The AirBnB website clone.

> Therefore, we would refer the command line interpreter as the frontend of this project. This is the medium through which users can interact with the backend which we developed using Python's OOP.

Here are the available commands in this project

Show
Create
Update
Destroy
Count
With regards to the command line usage, in relation to the backend and the storage system, The following actions can be executed:

Creating new objects (ex: a new User or a new Place)
Retrieving an object from a file, a database etc?
Doing operations on objects (count, compute stats, etc?)
Updating attributes of an object
Destroying an object
How to start it
The following instructions will get you a copy of the project up and running on your local machine (Linux distro) exclusively for development and testing purposes.

Installing
To install this program, there is the need to clone the repository from github
includes the shell program and associated dependencies. You will need to clone the repository of the project from Github. This will contain the simple shell program and all of its dependencies. Below are simple steps you can follow to install the program:

        git clone https://github.com/sylvan452/AirBnB_clone.git
Once the cloning is done, you will have a folder containing the the AirBnB project. In this folder, you're expected to see several files with which the program can run. They include:

/console.py : The main executable of the project, the command interpreter.
models/engine/file_storage.py: Class that serializes instances to a JSON file and deserializes JSON file to instances
models/__ init __.py: A unique FileStorage instance for the application
models/base_model.py: Class that defines all common attributes/methods for other classes.
models/user.py: User class that inherits from BaseModel
models/state.py: State class that inherits from BaseModel
models/city.py: City class that inherits from BaseModel
models/amenity.py: Amenity class that inherits from BaseModel
models/place.py: Place class that inherits from BaseModel
models/review.py: Review class that inherits from BaseModel
How to use it
This project is designed to work in two different modes, which includes:

The Interactive mode
The Non-interactive mode.
The console in the interactive mode displays a prompt(hbnb) once a user writes or executes a command.
The prompt appears again after the command is run to wait for a new command.This is an indefinite process so long as the user does not terminate the program.

  $./console.py
    (hbnb) help
        
    Documented commands (type help <topic>):
    ::::::::::::::::::::::::::::::::::
    EOF help quit<br>
        
    (hbnb)
    (hbnb)
    (hbnb) quit
  $
The shell in the Non-interactive mode needs to be run with a command input piped into its execution which enables the command to run once the shell starts operation. In this mode, no input is expected from the user therefore no prompt will appear.

    $ echo "help" | ./console.py
    (hbnb)

    Documented commands (type help <topic>):
    ::::::::::::::::::::::::::::::::::::
    EOF help quit
    (hbnb)
    $
    $ cat test_help
    help
    $
    $ cat test_help | ./console.py
    (hbnb)

    Documented commands (type help <topic>):
    ::::::::::::::::::::::::::::::::::::::
    EOF help quit
    (hbnb)
    $
Format of Command Input
This is necessary when giving command to the console. There ia the need for it to be piped through an echo in case of the non-interactive mode.


In Interactive Mode the commands will need to be written with a keyboard when the prompt appears and will be recognized when an enter key is pressed (new line). As soon as this happens, the console will attempt to execute the command through several means or will show an error message if the command didn't run successfully.
In this mode, the console can be exited using the CTRL + D combination, CTRL + C, or the command quit or EOF.
