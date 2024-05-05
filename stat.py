from collections import Counter


class Stat(Counter):
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
        
    
    def mode_beta1(self, array, frequency=None):
        """
        Returns the mode of a array.
        If the optional argument is passed, a tuple is returned containing the mode and it's modal frequency.
        
        Parameters:
        - An array of integers or floats
        - (Optional) Takes a boolean as argument
        """
        array = list(array) # To convert numpy ndarrays
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
            

    def mode_beta2(self, array, frequency=None):
        """
        Returns the mode of a array.
        If the optional argument is passed, a tuple is returned containing the mode and it's modal frequency.
        
        Parameters:
        - An array of integers or floats
        - (Optional) Takes a boolean as argument
        """
        array = list(array) # To convert numpy ndarrays
        explored = []
        counts = []

        for i in array:
            if i not in explored:
                counts.append(array.count(i))
                explored.append(i)
        
        modal = max(counts)
        mode = explored[(counts.index(modal))]

        if frequency:
            return mode, modal
        return mode
    

    def mode(self, array):
        """
        Returns the mode of a array.
        
        Parameters:
        - An array of integers or floats
        """
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
        temp_array = [(i - mean) ** 2 for i in array]
        
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

