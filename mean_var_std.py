import numpy as np

def calculate(list):
    """
    Calculate mean, variance, standard deviation, max, min, and sum
    for a 3x3 matrix from a list of 9 numbers.
    
    Args:
        list: A list containing 9 numbers
        
    Returns:
        dict: Dictionary containing statistics for rows, columns, and flattened matrix
        
    Raises:
        ValueError: If the list doesn't contain exactly 9 numbers
    """
    # Check if the list contains exactly 9 elements
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    # Convert list to 3x3 numpy array
    matrix = np.array(list).reshape(3, 3)
    
    # Calculate statistics
    calculations = {
        'mean': [
            matrix.mean(axis=0).tolist(),  # mean of columns (axis=0)
            matrix.mean(axis=1).tolist(),  # mean of rows (axis=1)
            matrix.mean().item()           # mean of flattened matrix
        ],
        'variance': [
            matrix.var(axis=0).tolist(),   # variance of columns
            matrix.var(axis=1).tolist(),   # variance of rows
            matrix.var().item()            # variance of flattened matrix
        ],
        'standard deviation': [
            matrix.std(axis=0).tolist(),   # std dev of columns
            matrix.std(axis=1).tolist(),   # std dev of rows
            matrix.std().item()            # std dev of flattened matrix
        ],
        'max': [
            matrix.max(axis=0).tolist(),   # max of columns
            matrix.max(axis=1).tolist(),   # max of rows
            matrix.max().item()            # max of flattened matrix
        ],
        'min': [
            matrix.min(axis=0).tolist(),   # min of columns
            matrix.min(axis=1).tolist(),   # min of rows
            matrix.min().item()            # min of flattened matrix
        ],
        'sum': [
            matrix.sum(axis=0).tolist(),   # sum of columns
            matrix.sum(axis=1).tolist(),   # sum of rows
            matrix.sum().item()            # sum of flattened matrix
        ]
    }
    
    return calculations
