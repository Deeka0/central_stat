#include <iostream>
#include <unistd.h>

using namespace std;

double mean(double array[]);
double median(double array[]);



int main()
{
    sleep(3);
    system("clear");
    // double speed[] = {99,86,87,88,111,86,103,87,94,78,77,85,86};
    // int speed[] = {32,111,138,28,59,77,97};
    // int speed[] = {12,5,77, 545, 77};
    double speed[] = {5, 12, 77, 77, 290, 545};

    // double meann = mean(speed);
    // cout << meann << endl;
    double mediann = median(speed);
    cout << mediann << endl;
    return 0;
}


double mean(double array[])
{
    double array_sum;
    int array_length = sizeof(array) / sizeof(double);
    for (int i = 0; array; array_sum+=array[i])
    {
        cout << i;
    }
    double mean = array_sum / array_length;
    return mean;
}


double median(double array[])
{
    // array.sort();
    int array_length = sizeof(array) / sizeof(double);
    int mid = array_length / 2;
//         if isfloat:
//             return float(array[mid])
//         return array[mid]
    return array[mid];
}

// class Stat:
//     """
//     Computations for statistical central tendencies
//     """
    
    
//     def mean(array, floats=None):
//         """
//         Returns the median of an array.
//         If the optional argument is passed, the returned mean is limited according to floating points argument.
        
//         Parameters:
//         - An array of integers or floats
//         - (Optional) Takes an integer as input
//         """
//         mean = sum(array) / len(array)
//         if floats:
//             return round(mean, floats)
//         return mean
    
    
//     def median(array, isfloat=None):
//         """
//         Returns the median of an array.
//         If the optional argument is passed, the median is returned as a float

//         Parameters:
//         - An array of integers or floats
//         - (Optional) Takes a boolean as input
//         """
//         array.sort()
//         mid = len(array) // 2
//         if isfloat:
//             return float(array[mid])
//         return array[mid]
        
    
//     def mode(array, frequency=None):
//         """
//         Returns the mode of a array.
//         If the optional argument is passed, a tuple is returned containing the mode and it's modal frequency.
        
//         Parameters:
//         - An array of integers or floats
//         - (Optional) Takes a boolean as input
//         """
//         explored = []
//         modal = 0
//         mode = None

//         # Analysis 1
//         for i in array:
//             if i not in explored:
//                 num = array.count(i)
//                 if num > modal:
//                     modal = num
//                 explored.append(i)
        
//         # Analysis 2
//         for i in explored:
//             if array.count(i) == modal:
//                 mode = i
//                 if frequency:
//                     return mode, modal
//                 return mode


//     def variance(array, floats=None):
//         """
//         Returns the variance of an array.
//         If the optional argument is passed, the returned variance is limited according to floating points argument.
        
//         Parameters:
//         - An array of integers or floats
//         - (Optional) Takes an integer as input
//         """
//         mean = Stat.mean(array)
//         temp_array = []

//         for i in array:
//             temp_array.append((i - mean) ** 2)
//         if floats:
//             return round((Stat.mean(temp_array)), floats)
//         return Stat.mean(temp_array)


//     def std(array, floats=None):
//         """
//         Returns the standard deviation of an array.
//         If the optional argument is passed, the returned standard deviation is limited according to floating points argument.
        
//         Parameters:
//         - An array of integers or floats
//         - (Optional) Takes an integer as input
//         """
//         if floats:
//             return round((Stat.variance(array) ** .5), floats)
//         return Stat.variance(array) ** .5




// if __name__ == "__main__":
//     os.system("clear")


//     # Mean Test
//     print("\n### Mean Test ###\n".upper())
//     tic = time.time()
//     meanN = np.mean(speed)
//     timeN = time.time() - tic
//     print(f"MeanN: {meanN} RuntimeN: {timeN} seconds")

//     tic = time.time()
//     meanS = Stat.mean(speed)
//     timeS = time.time() - tic
//     print(f"MeanS: {meanS} RuntimeS: {timeS} seconds")
//     if timeN < timeS:
//         print(f"MeanN is faster")
//     else:
//         print(f"MeanS is faster")


//     # Median Test
//     print("\n### Median Test ###\n".upper())
//     tic = time.time()
//     medianN = np.median(speed)
//     timeN = time.time() - tic
//     print(f"MedianN: {medianN} RuntimeN: {timeN} seconds")

//     tic = time.time()
//     medianS = Stat.median(speed)
//     timeS = time.time() - tic
//     print(f"MedianS: {medianS} RuntimeS: {timeS} seconds")
//     if timeN < timeS:
//         print(f"MedianN is faster")
//     else:
//         print(f"MedianS is faster")


//     # Mode Test
//     print("\n### Mode Test ###\n".upper())
//     tic = time.time()
//     modeN = Stat.mode(speed, frequency=True)
//     timeN = time.time() - tic
//     print(f"ModeN: {modeN[0]} RuntimeN: {timeN} seconds")

//     tic = time.time()
//     modeS = Stat.mode(speed, frequency=True)
//     timeS = time.time() - tic
//     print(f"ModeS: {modeS[0]} RuntimeS: {timeS} seconds")
//     print(modeS)
//     if timeN < timeS:
//         print(f"ModeN is faster")
//     else:
//         print(f"ModeS is faster")


//     # Variance Test
//     print("\n### Variance Test ###\n".upper())
//     tic = time.time()
//     varianceN = np.var(speed)
//     timeN = time.time() - tic
//     print(f"VarianceN: {varianceN} RuntimeN: {timeN} seconds")

//     tic = time.time()
//     varianceS = Stat.variance(speed)
//     timeS = time.time() - tic
//     print(f"VarianceS: {varianceS} RuntimeS: {timeS} seconds")
//     if timeN < timeS:
//         print(f"ModeN is faster")
//     else:
//         print(f"ModeS is faster")


//     # Standard Deviation Test
//     print("\n### Standard Deviation Test ###\n".upper())
//     tic = time.time()
//     stdN = np.std(speed)
//     timeN = time.time() - tic
//     print(f"stdN: {stdN} RuntimeN: {timeN} seconds")

//     tic = time.time()
//     stdS = Stat.std(speed)
//     timeS = time.time() - tic
//     print(f"stdS: {stdS} RuntimeS: {timeS} seconds")
//     if timeN < timeS:
//         print(f"ModeN is faster")
//     else:
//         print(f"ModeS is faster")



