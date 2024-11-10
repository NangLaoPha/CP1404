# CP1404 Practical Exercises - Programming II

## Overview
This repository contains practical exercises for CP1404 - Programming II, focused on reinforcing object-oriented programming (OOP), clean code practices, and software development fundamentals. Each practical task is designed to enhance coding skills, with an emphasis on implementing classes, handling files, and applying design principles in Python.

### Author
Developed by Nang Lao Pha as part of the CP1404 coursework.

## Practical 07 - Classes and Object-Oriented Design
Practical 07 builds on previous knowledge of classes, expanding into more complex OOP design patterns and practices, particularly for managing and interacting with multiple objects and data files. Below are brief descriptions of each main file in this practical:

[Practical 07 Repository](https://github.com/NangLaoPha/CP1404/tree/master/prac_07)

### File Descriptions
- **`guitar.py`**: Defines a `Guitar` class with attributes like name, year, and cost, along with methods to calculate a guitar's age, check if it is vintage, and support sorting by year.

- **`language_file_reader.py`**: A script for reading data on programming languages from a file, creating instances of the `ProgrammingLanguage` class (defined in `programming_language.py`), and displaying the data.

- **`myguitar.py`**: Uses the `Guitar` class to load, display, and manage a list of guitars from `guitars.csv`. This script includes functions to sort guitars by age, add new entries, and save updates to the file.

- **`programming_language.py`**: Contains the `ProgrammingLanguage` class, which models attributes such as typing, reflection, pointer arithmetic, and year of creation. This class supports analyzing programming languages based on these properties.

- **`project_management.py`**: A project management tool that loads and manages a list of `Project` objects. It supports functionalities like displaying projects, filtering by start date, updating completion status, and saving project data to files.

- **`project.py`**: Defines the `Project` class with attributes such as name, start date, priority, completion percentage, and cost. Methods within this class help to check project completion status and update project details.

## Key Lessons on Clean Code
Throughout the CP1404 subject, key principles of clean code have been emphasized:
- **Consistent Naming Conventions**: Adopting meaningful and uniform naming conventions enhances code readability and maintenance.
- **Single Responsibility Principle**: Breaking down functionality into well-defined methods and classes that focus on a single responsibility, aiding clarity and modularity.
- **Robust Error Handling and Validation**: Ensuring that programs handle unexpected input gracefully, improving user experience and software reliability.

## Resources
For additional guidance and information:
- [Programming Patterns](https://github.com/CP1404/Starter/wiki/Programming-Patterns): A resource on programming patterns utilized in CP1404.
- [CP1404 Practicals Repository](https://github.com/CP1404/Practicals): The official repository with instructions and resources for CP1404 practicals.

## Formatting
Before committing any code, please ensure formatting adheres to best practices. PyCharm’s **Reformat Code** tool can help maintain consistency.
