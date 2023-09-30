import sys
import numpy as np


def get_column(file_name, query_column, query_value, result_column=4):
    """
    Retrieves Forest Fire data given a particular country 

    Parameters
    ----------
    file_name : str
        The file name of the comma-delimitted data file
    query_column : int
        The column number that lists all of the countries
    query_value : str
        The name of the country whose fire data you want
    result_column
        The column number that contains the fire data (from year 1990 through 2020) for all countries

    Returns
    -------
    list
        a list of ints that contains the fire data metric for each recorded year (from year 1990 through 2020) for the specified country
    """      
    
    forest_fires = []
    

    try:
        f = open(file_name, 'r')
    except FileNotFoundError:
        print(f'FileNotFoundError:  {file_name}') 
        sys.exit(1)
    else:   
        for line in f:
            items = line.strip().split(',')  

            try:
                country_col_value = items[query_column - 1]
            except IndexError:
                print(f'The Country Column index is out of range: {query_column}')
                sys.exit(1) 
                
                
            try:
                result_col_value = items[result_column - 1]
            except IndexError:
                print(f'The Fire Column index is out of range: {result_column}')
                sys.exit(1)
               
                
            # for all the rows that are of the specified country....  
            if country_col_value == query_value:

                # convert string representation of a float, then to an int 
                try:
                    int_fire_metric = int(float(result_col_value)) 
                except ValueError:
                    print(f'Could not convert value to an int: Trying to convert value {result_col_value}')
                    sys.exit(1)

                forest_fires.append(int_fire_metric)


        f.close()  
            
    return forest_fires


def mean(list_of_ints):
    """
    Gets the mean of a list of integers (using numpy)

    Parameters
    ----------
    list_of_ints : [] int
        Python list of integers

    Returns
    -------
    mean : float
        The mean of the inputted list of integers
    """        
    return np.mean(list_of_ints)



def median(list_of_ints):
    """
    Gets the median of a list of integers (using numpy)

    Parameters
    ----------
    list_of_ints : [] int
        Python list of integers

    Returns
    -------
    median : float
        The median of the inputted list of integers
    """ 
    return np.median(list_of_ints)



def standard_deviation(list_of_ints):
    """
    Gets the standard deviiation of a list of integers (using numpy)

    Parameters
    ----------
    list_of_ints : [] int
        Python list of integers

    Returns
    -------
    standard deviation : float
        The standard deviation of the inputted list of integers
    """ 
    return np.std(list_of_ints)




def main():
    """
    Makes sure that all of the functions: get_column(), mean(), median(), and standard_deviation() run

    Parameters
    ----------
    no parameters

    Returns
    -------
    nothing
    """ 
    
    file_name = 'Agrofood_co2_emission.csv'
    country_column = 1
    country = 'United States of America'
    fires_column = 4
    
    print(f'Here are the fire metrics for {country}')

    fires = get_column(file_name, country_column, country, result_column=fires_column)
    print(fires)
    print()
    print(f'Forest Fires Mean: {mean(fires)}')
    print()
    print(f'Forest Fires Median: {median(fires)}')
    print()
    print(f'Forest Fires Standard Deviation: {standard_deviation(fires)}')
    
    

if __name__ == '__main__':
    main()
    
