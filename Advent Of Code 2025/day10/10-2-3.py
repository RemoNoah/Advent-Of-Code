mat = [[1, 0, 1], 
       [1, 1, 0]]

target = [7,3] 

#wieghts = for every button (will always be 1 for this problem)
c = [-1,-1,-1]





# a | b | x | t
# 0 | 1 | 1 | 7
# 1 | 0 | 1 | 3
#--------------
# -1 | -1 | -1 | 0 <- weights = [-1, -1, -1]

def print_matrix(matrix, target, weights):
    print("Matrix:")
    for i in range(len(matrix)):
        print(matrix[i], "|", target[i])
    print(str(weights) + " <- weights")
    print("--------------------")


def select_pivot_colummn(weights):
    # Select the pivot based on the weights
    # If there are multiple maximum weights, select the first one
    return weights.index(min(weights))


def select_pivot_row_index(matrix, pivot_column, target):
    # Select the pivot elements based on the pivot column and the target values
    pivot_row_index = 0
    pivot_value = float('inf')  # Initialize pivot_value to infinity for comparison

    for dimension in range(len(matrix)):
        # Get the possible pivot element for the current dimension
        possible_pivot_element = matrix[dimension][pivot_column]
        
        # Check if the possible pivot element is greater than 0 to avoid division by zero
        if possible_pivot_element != 0:
            pivot = target[dimension]/abs(possible_pivot_element)
            
            if pivot < pivot_value:
                pivot_row_index = dimension
                pivot_value = pivot 

    return pivot_row_index, pivot_value


def substract_pivot_row_from_other_rows(matrix, pivot_row_index, pivot_column, target, weights):
    # Subtract the pivot row from all other rows in the matrix
    updated_matrix = []
    updated_weights = weights.copy()
    updated_target = []
    dimension = len(matrix)
    
    for row in range(dimension):
        # if the current row is the pivot row, we skip it
        # if other row column is already 0, we can skip the substraction
        if row != pivot_row_index and matrix[row][pivot_column] != 0:
                has_changed = True
                updated_row = []
                # Subtract the pivot row from the current row
                for col in range(len(matrix[row])):
                    updated_row.append(int(matrix[row][col] - matrix[pivot_row_index][col]))
                updated_matrix.append(updated_row)
                
                #update the target value for the current row
                target[row] = int(target[row] - target[pivot_row_index])
                updated_target.append(target[row])
        else:
            updated_matrix.append(matrix[row])
            updated_target.append(target[row])
  
        #update the weights by substracting the pivot row from the weights
        for i, value in enumerate(matrix[pivot_row_index]):
            updated_weights[i] = int(updated_weights[i] + value)

    return updated_matrix, updated_weights, updated_target


def check_if_solution_found(weights):
    # Check if the solution is found
    return all(weight >= 0 for weight in weights)

def part2(matrix, target, weights):
    solution = 0
    
    while not check_if_solution_found(weights):
        print_matrix(matrix, target, weights)
        selected_pivot_column = select_pivot_colummn(weights)
        selected_pivot_row_index, pivot_value = select_pivot_row_index(matrix, selected_pivot_column, target)
        solution += pivot_value
        matrix, weights, target = substract_pivot_row_from_other_rows(matrix, selected_pivot_row_index, selected_pivot_column, target, weights)
    
    print_matrix(matrix, target, weights)
    print(f'Solution found: {solution}')


part2(mat, target, c)