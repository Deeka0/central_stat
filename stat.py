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
        Returns the mean of an array.
        If the optional argument is passed, the returned mean is limited according to floating points argument.
        
        Parameters:
        - An array of integers or floats
        - (Optional) Takes an integer as argument
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
        - (Optional) Takes a boolean as argument
        """
        array.sort()
        mid = len(array) // 2
        if isfloat:
            return float(array[mid])
        return array[mid]
        
        
    def mode(array):
        """
        Returns the mode of a array.
        
        Parameters:
        - An array of integers or floats
        """
        from collections import Counter
        pairs = Counter(iter(array)).most_common(1)
        try:
            return pairs[0][0]
        except IndexError:
            raise Exception


    def variance(self, array, floats=None):
        """
        Returns the variance of an array.
        If the optional argument is passed, the returned variance is limited according to floating points argument.
        
        Parameters:
        - An array of integers or floats
        - (Optional) Takes an integer as argument
        """
        mean = self.mean(array)
        temp_array = []

        for i in array:
            temp_array.append((i - mean) ** 2)
        if floats:
            return round((self.mean(temp_array)), floats)
        return self.mean(temp_array)


    def std(self, array, floats=None):
        """
        Returns the standard deviation of an array.
        If the optional argument is passed, the returned standard deviation is limited according to floating points argument.
        
        Parameters:
        - An array of integers or floats
        - (Optional) Takes an integer as argument
        """
        if floats:
            return round((self.variance(array) ** .5), floats)
        return self.variance(array) ** .5
