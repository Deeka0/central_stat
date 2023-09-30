class Stat:
    """
    Computations for statistical central tendencies.

    Includes:
    - Mean
    - Median
    - Mode
    - Variance
    - Standard Deviation
    """
    
    
    def mean(self, array, floats=None):
        """
        Returns the median of an array.
        If the optional argument is passed, the returned mean is limited according to floating points argument.
        
        Parameters:
        - An array of integers or floats
        - (Optional) Takes an integer as input
        """
        mean = sum(array) / len(array)
        if floats:
            return round(mean, floats)
        return mean
    
    
    def median(self, array, isfloat=None):
        """
        Returns the median of an array.
        If the optional argument is passed, the median is returned as a float.

        Parameters:
        - An array of integers or floats
        - (Optional) Takes a boolean as input
        """
        array.sort()
        mid = len(array) // 2
        if isfloat:
            return float(array[mid])
        return array[mid]
        
    
    def mode(self, array, frequency=None):
        """
        Returns the mode of a array.
        If the optional argument is passed, a tuple is returned containing the mode and it's modal frequency.
        
        Parameters:
        - An array of integers or floats
        - (Optional) Takes a boolean as input
        """
        explored = []
        modal = 0
        mode = None

        # Analysis 1
        for i in array:
            if i not in explored:
                num = array.count(i)
                if num > modal:
                    modal = num
                explored.append(i)
        
        # Analysis 2
        for i in explored:
            if array.count(i) == modal:
                mode = i
                if frequency:
                    return mode, modal
                return mode


    def variance(self, array, floats=None):
        """
        Returns the variance of an array.
        If the optional argument is passed, the returned variance is limited according to floating points argument.
        
        Parameters:
        - An array of integers or floats
        - (Optional) Takes an integer as input
        """
        mean = Stat.mean(array)
        temp_array = []

        for i in array:
            temp_array.append((i - mean) ** 2)
        if floats:
            return round((Stat.mean(temp_array)), floats)
        return Stat.mean(temp_array)


    def std(self, array, floats=None):
        """
        Returns the standard deviation of an array.
        If the optional argument is passed, the returned standard deviation is limited according to floating points argument.
        
        Parameters:
        - An array of integers or floats
        - (Optional) Takes an integer as input
        """
        if floats:
            return round((Stat.variance(array) ** .5), floats)
        return Stat.variance(array) ** .5


