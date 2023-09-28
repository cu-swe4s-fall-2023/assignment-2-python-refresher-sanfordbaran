import sys


def get_column(file_name, query_column, query_value, result_column=4):
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
               
                
                
            if country_col_value == query_value:

                # convert string representation of a float to an in 
                try:
                    int_fire_metric = int(float(result_col_value)) 
                except ValueError:
                    print(f'Could not convert value to an int:  {result_col_value}')
                    sys.exit(1)

                forest_fires.append(int_fire_metric)


        f.close()  
            
    return forest_fires


def main():
    file_name = 'Agrofood_co2_emission.csv'
    country_column = 1
    country = 'Brazil'
    fires_column = 4
    
    print(f'Here are the fire metrics for {country}')

    fires = get_column(file_name, country_column, country, result_column=fires_column)
    print(fires)
    
    

if __name__ == '__main__':
    main()
    
