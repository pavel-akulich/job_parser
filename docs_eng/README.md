# Project: Job Parser
[Russian](../README.md) | **English**

## Project Description
The Vacancy Parser project is a console application that allows you to receive information about vacancies from different platforms, save it to a file and work with it conveniently (delete, output to the console, receive by criteria).
## Components of the project
The project consists of the following components:

1. **Class for working with the API of sites with vacancies:**
   - An abstract class `GeneralAPI` has been created, in which the methods `get_vacancies` and `parse` are defined, the first receives data via the API, and the second converts them into a structured format.
   - Implemented classes-heirs of the abstract class - `HeadHunterAPI` and `SuperJobAPI`, they are able to connect to the API of the corresponding platforms and get vacancies according to the specified criteria.

2. **Class for working with vacancies:**
   - The `Vacancy` class has been created, which represents a vacancy with the following attributes: the name of the vacancy, a link to the vacancy, salary from, salary to, employer, city and responsibilities.
   - The class contains the magic method `__str__`, which allows you to display information about the vacancy in a readable form.
   - The class also contains magic methods for comparing 2 vacancy based on salary, such as: `__lt__`, `__le__`, `__gt__`, `__ge__`, `__eq__`.

3. **A class for working with vacancy storage:**
      - Created abstract class `GeneralStorage`, which defines methods for saving, receiving, deleting vacancies, as well as methods for obtaining vacancies by salary, city and method for obtaining top N vacancies.
      - The successor classes can be implemented for different storage formats, this project implements the classes `JsonSaver` for saving to JSON format and `CSVSaver` for saving to CSV format.
   
4. **Functions for user interaction:**
    - The main function `user_interaction` is implemented to interact with the user through the console.
    - Additional functions that are part of the `user_interaction` function are implemented in the `utils.py `.
    - The user can choose which platforms he wants to get vacancies from, enter search parameters, get top N vacancies, get vacancies according to the parameters he needs, and more.
   
## Technologies
- The project is developed in the Python programming language. A third-party library `requests` is used to work with the API.
- The project uses the `poetry` tool to manage the virtual environment.
- All the necessary dependencies to the project are in the file `pyproject.toml `.

## Instructions for using the program
The entire interface and all user interaction takes place in English.

All interaction with the application takes place by entering numbers to select an action.

Before launching the application, familiarize yourself with how to use it.

1. Run the application by running the command `python main.py ` or by clicking `Run 'main'` for the file `main.py `.

2. In the suggested menu, select one of the options by entering the appropriate number:
   - 1 - Vacancy search
   - 2 - Saving vacancies to a file
   - 3 - Deleting a vacancy from a file
   - 4 - Getting a vacancy from file based on salary
   - 5 - Getting a vacancy from file based on the city
   - 6 - Getting top N vacancies from a file
   - 7 - Getting all vacancies from a file
   - 0 - Completion of the program
   
3. Follow the instructions in the console to perform the selected operation.

## Notes
- The project can be further developed and expanded for wider use.
- To work with API platforms `hh.ru ` and `superjob.ru ` the corresponding API keys are required to be added to the environment variables.
- The `API_KEY` variable stores the API key for the platform `superjob.ru`.