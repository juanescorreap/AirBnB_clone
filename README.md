# AirBnB Clone PROJECT
## THE CONSOLE

** AUTHORS :    
**Juan Esteban Correa**
<p align="center">
	    <img align="center" src="https://avatars.githubusercontent.com/u/85306177?v=4" alt="Juan Esteban Correa" height="80" width="80" />
	      <a href="https://github.com/juanescorreap" target="blank"><img align="center" src="https://raw.githubusercontent.com/devicons/devicon/9f4f5cdb393299a81125eb5127929ea7bfe42889/icons/github/github-original.svg" alt="Github Maria Paula" height="30" width="40" /></a>
  </p> <br>

**Angela Vergara** 

  <p align="center">
      <img align="center" src="https://avatars.githubusercontent.com/u/85180677?v=4" alt="Angela Vergara" height="80" width="80" />
        <a href="https://github.com/anversa-pro" target="blank"><img align="center" src="https://raw.githubusercontent.com/devicons/devicon/9f4f5cdb393299a81125eb5127929ea7bfe42889/icons/github/github-original.svg" alt="Github Angela" height="30" width="40" /></a> 
 </p>  <br>


Project developed by Angela Vergara and Juan Esteban Correa as part of the foundations program at Holberton School.

It's purpose is to help the student understand:

How to create a Python package<br />
How to create a command interpreter in Python using the cmd module<br />
What is Unit testing and how to implement it in a large project<br />
How to serialize and deserialize a Class<br />
How to write and read a JSON file<br />
How to manage datetime<br />
What is an UUID<br />
What is *args and how to use it
What is **kwargs and how to use it<br />
How to handle named arguments in a function<br />

### Project Description
The Console program emulates a native console to interpret commands and interact with AirBnB clone classes and methods.
This project aims to strengthen previous concepts and knowledge by applying them in a single project.

### Command Interpreter
Allows the user to interact with the AirBnB clone classes and methods using commands in the form of text lines.

### How to start
To begin to clone the current repository, which contains all files necessary for the program's execution. 
To execute the console, run the console.py file in your terminal; this will initiate the interactive mode. 

### How to use it
All commands are case sensitive:
|  Commands |         Description         |           Input format         |
|----------------|----------------------|------------------------|
|`quit`|Exits the AirBnB console.| `quit`                |
|`EOF`|Exits the program when passing an EOF signal.| `CTRL + D`|
|`empty line`|Shows the prompt in a new line when passing an ENTER.|
|`create`|Creates an instance of one of the available classes (See below).| `create <class name>`|
| `show`| Shows the attributes and their values of an instance. | `show <class name> <instance id>`| 
|`destroy`| Deletes an instance| `destroy  <class name> <instance id>`|
|`all`|Prints all instances of a specified class; if no class is specified, prints all instances.|`all` or `all <class name>`|
|`update`| Creates or updates an attribute's value for a specified instance| `update <class name> <instance id> <attribute name> <attribute value>`|
|`count`| Counts the number of instances from a class.| `<class name>.count()`|

# Available classes

|  Class |         Description         |
|----------------|----------------------------------------------|
|`BaseModel`| Parent class containing all basic attributes and methods|
|`Amenity`| Class defines Amenity and its attributes.|
|`City`| Class defines City and its attributes.|
|`Place`|  Class defines Place and its attributes.|
|`Review`| Class defines Place and its attributes.|
|`State`| Class defines State and its attributes.|
|`User`| Class defines User and its attributes.|


### Examples
#### Create a new instance
`create BaseModel`
#### Update attributes
`update BaseModel 1234-1234-1234 email "aibnb@mail.com"`<br />
`User.update("38f22813-2753-4d42-b37c-57a17f1e4f88", "first_name", "John")`
#### Show instances, all or specific ones.
`all`
`all BaseModel`
`User.all()`

        That's all, thanks for reading!