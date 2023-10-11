[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/oQi7O4AA)


# Instructions:

### To do just run the functionality from src:
    cd src
    bash run.sh  

### To run the unit tests:
    cd test/unit
    python -m unittest test_my_utils.py     
    
### To run the functional tests:
    bash test/func/test_print_fires.sh
    
### To run the python code-style checks:
    pycodestyle $(git ls-files "*.py") 
    
### Path to the Test data:
    test/data/Agrofood_co2_emission_ft.csv  
<br/>

### Summary of Commits:

1. my_utils.py:
> implement the get_column() function  

2. print_fires:
> correctly call the get_column() function

3. my_utils.py:
> improve get_column() to use a named argument for the result_column that defaults to 4

4. print_fires.py:
> update to correctly use the new get_column function

5. print_fires.py:
> update to use argpase to collect the 4 inputs to the get_column function via the command line

6. my_utils.py:
> update get_column() to return a list of integers

7. print_fires.py and my_utils.py:
> added main functions to both of these modules

8. my_utils.py:
> added Exception Handling and Exit return codes

9. my_utils.py:
> fully documented the function get_column

10. my_utils.py
> add the new functions mean(), median() and standard_deviation()

11. test_my_utils.py
> added this file that has all of the unit tests for functions in my_utils.py

12. Agrofood_co2_emission_ft.csv
> added this data file for functional tests

13. test_printfires.sh
> added this file to do functional testing

14. test_my_utils.py
> Refined and reworked these unit tests

15. tests_and_checks.yml
> Added this continuous integration workflow file

16. environment.yml
> Add this environment file used in the contiunous integration workflow

17. tests_and_checks.yml
> Remove the pull-request event, so that this can happen if you get a pycodestyle failure






