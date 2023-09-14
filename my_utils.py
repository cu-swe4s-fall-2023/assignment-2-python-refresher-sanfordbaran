def get_column(file_name, query_column, query_value, result_column):
    forest_fires = []
    
    with open(file_name, 'r') as f:
        for line in f:
            items = line.strip().split(',')           
            if items[query_column - 1] == query_value:
                forest_fires.append(items[result_column - 1])
    
    return forest_fires
