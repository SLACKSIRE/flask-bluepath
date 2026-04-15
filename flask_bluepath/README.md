# Flask BluePath

## Table of Contents
- [About](#about)
- [Requirements](#requirements)
- [Getting Started](#getting-started)
- [Module Manager](#module-manager)
- [Credits](#credits)

## About
Flask BluePath is built for the [Flask](https://palletsprojects.com/projects/flask) framework by [Pallets Projects](https://palletsprojects.com/). This package is designed to allow for quick loading of modules by using the name of the module directory as the name of the corresponding Flask blueprint. The Module Manager will review the directory and determine if the criteria have been met for a module, and it will load it as a blueprint.  
This really is a lightweight and simple setup for automating  your blueprint creation. Enjoy!

## Requirements
- Flask
- os
- importlib

## Getting Started
1. Create a 'Modules' directory and copy the example_module from this directory to use as a template.
    - Using Flask config variables, you can set the modules directory to any directory within the application. See [Setting the Modules Directory](#setting-the-modules-directory) for more information.
2. Build your flask module like you would any standard flask app; with the following modifications:
    - All flask 
3. Be sure to **delete** the "example_module" folder prior to production. This module will be loaded as a blueprint if the modules directory is set to default.

## Setting the Modules Directory
Setting the modules directory can be done using the flask configuration dictionary.
```python
# How you set the configuration
app.config[""]
# How Flask_Modules pulls the data
app.config.get("MODULES_DIRECTORY")
```

## Typical Module Structure
📦example_module  
 ┣ 📂static  
 ┃ ┣ 📂css  
 ┃ ┃ ┗ 📜example.css  
 ┃ ┣ 📂images  
 ┃ ┗ 📂js  
 ┃ ┃ ┗ 📜example.js  
 ┣ 📂templates  
 ┃ ┗ 📜example.html  
 ┗ 📜routing.py  

 ## Minimum Module Structure
 📦example_module  
 ┣ 📂templates  
 ┃ ┗ 📜example.html  
 ┗ 📜routing.py  

 ## Module Manager
 The Member Module is the class that is called to initialize the module system.
 ### Parameters
 - **app**: The Flask application object. ***REQUIRED***

 - **rel_dir**: The path to the directory relative to the main flask app.  
 -- Default: "modules"  

 - **include**: A whitelist of modules to include. Utilizing this parameter will automatically exclude all items not on this list.  
 -- Default: []  

 - **exclude**: A blacklist of modules to exclude. Unlike the "include" parameter, this doesn't affect any modules outside of the ones in this list.  
 -- Default: []  

 ### Public Methods
 - **load_module**: Load a module into the module manager
 - **exclude**: Append an existing module to the exclusion list

### Private Methods
- **_print_loading_messages**: print the loading message for Flask-Bluepath.
- **_print_loading_graphics**: print the Flask-Bluepath ascii artwork.
- **_print_exclusion_list**: Print the list of excluded modules.
- **_print_inclusion_list**: Print the list of exclusively included modules.
- **_load_modules_from_directory**: Discover modules within specified directory and
attempt to generate a Flask Blueprint from them.
- **_check_if_directory_matches_module_structure**: Check that a directory contains
the minimum structural requirements to be considered a module.

 ## Calling Static Files from Templatea
 Calling an image from the blueprint (module's) static folder requires using url_for. See below for the syntax, or view the [Official Jinja Documentation](https://jinja.palletsprojects.com/en/stable/).
 ```
 {{ url_for("<module_name>.static") filename="images/example.png" }}
 ```


## Credits
Written by John D McLaughlin (SLACKSIRE) and distributed under the [MIT License](/License.md), a copy of which can be found in the License.md file located within this package.

