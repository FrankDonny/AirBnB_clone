# **AIRBNB_CLONE PROJECT**
    Find the collaborators of this project in the AUTHOR file.
    
    The project is a clone of the original AIRBNB web app but with minimum features
    compared to the original web app

    This version of the project is the base of the upcoming project involving the 
    AIRBNB CLONE


# COMMAND INTERPRETER DESCRIPTION
    The console.py interprets only the commands assigned to this project.
    This is how to use the console.py

# HOW TO START THE CONSOLE:
     * Execute the Console.py, the shell will start with a prompt "(hbnb)".
     * NB: The console works both in interactive and non-interactive modes.
            Interactive Mode Example:
            *$ ./console.py
                (hbnb) help

                Documented commands (type help <topic>):
                ========================================
                EOF  help  quit

                (hbnb) 
                (hbnb) 
                (hbnb) quit $

            Non-interactive Mode Example:
            $ echo "help" | ./console.py
                (hbnb)

                Documented commands (type help <topic>):
                ========================================
                EOF  help  quit
                (hbnb) 
                $
                $ cat test_help
                help
                $
                $ cat test_help | ./console.py
                (hbnb)

                Documented commands (type help <topic>):
                ========================================
                EOF  help  quit
                (hbnb) $

# HOW TO USE THE CONSOLE:
     * Type the "create" command to create a new instance of the BaseModel and return its id.
          (USAGE: create BaseModel)
     * Type the "show" command to print the string representation of an instance based on its class name and id.
          (USAGE: show BaseModel 34d3586d-5f20-4196-8910-3f6009b4425f).
     * Type the "destroy" command to delete an instance based on its class name and id and save into the json file.
          (USAGE: destroy BaseModel 34d3586d-5f20-4196-8910-3f6009b4425f).
     * Type the "all" command to print all string representation of all instances either based on the class name or not.
          (USAGE: all). Prints all instances
          (USAGE: all BaseModel). Prints all instances based on BaseModel class
     * Type the "update" command to update an instance by adding a new attribute and value
          (USAGE: update BaseModel 34d3586d-5f20-4196-8910-3f6009b4425f email "myemail@mail.com")
           This adds the attribute "email" to the BaseModel instance with a value "myemail@mail.com"

