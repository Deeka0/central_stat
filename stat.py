import numpy as np
import statistics
from os import system
from time import perf_counter
from collections import Counter


class Stat(Counter):
    """
    Computations for statistical central tendencies.

    Features:
    - Mean
    - Median
    - Mode
    - Variance
    - Standard Deviation
    """
    def mean(self, array: list[int | float], floating_points: int | None = None) -> float:
        """
        Computes the mean of an array.

        - array: An array of floats or integers.
        - floating_points: Limits returned results to floating points accuracy.
        """
        mean_value: float = sum(array) / len(array)
        return round(mean_value, floating_points) if floating_points else mean_value


    def median(self, array: list[int | float]) -> int | float:
        """
        Computes the median of an array.

        - array: An array of floats or integers.
        """
        array.sort()
        mid_point: int = len(array) // 2
        return array[mid_point]


    def mode_beta1(self, array: list[int | float], show_frequency: bool = False):
        """
        Computes the mode of a array.

        - array: An array of floats or integers.
        - show_frequency: a tuple is returned containing the modal value and it's modal frequency.
        """
        array: list[int | float] = list(array) # To convert numpy ndarrays
        explored: list[int | float] = []
        modal_frequency: int = 0
        modal_value: int | float | None = None

        # Analysis 1
        for i in array:
            if i not in explored:
                char_count: int = array.count(i)
                if char_count > modal_frequency:
                    modal_frequency = char_count
                explored.append(i)

        # Analysis 2
        for i in explored:
            if array.count(i) == modal_frequency:
                modal_value = i
                return modal_value, modal_frequency if show_frequency else modal_value


    def mode_beta2(self, array: list[int | float], show_frequency: bool = False) -> int | float | tuple[int | float, int]:
        """
        Computes the mode of a array.

        - array: An array of floats or integers.
        - show_frequency: a tuple is returned containing the modal value and it's modal frequency.
        """
        array: list[int | float] = list(array) # To convert numpy ndarrays
        explored: list[int | float] = []
        counts: list[int] = []

        for i in array:
            if i not in explored:
                counts.append(array.count(i))
                explored.append(i)
        
        modal_frequency: int = max(counts)
        modal_value: int | float = explored[(counts.index(modal_frequency))]

        return modal_value, modal_frequency if show_frequency else modal_value


    def mode(self, array: list[int | float]) -> int | float:
        """
        Computes the mode of a array.

        - array: An array of floats or integers.
        """
        pairs: list[tuple[int | float, int]] = Counter(iter(array)).most_common(n=1)
        return pairs[0][0]


    def variance(self, array: list[int | float], floating_points: int | None = None) -> float:
        """
        Computes the variance of an array.

        - array: An array of floats or integers.
        - floating_points: Limits returned results to floating points accuracy.
        """
        mean: float = self.mean(array=array)
        temp_array: list[int | float] = [(_ - mean) ** 2 for _ in array]

        if floating_points:
            return round((self.mean(array=temp_array)), floating_points)

        return self.mean(array=temp_array)


    def std(self, array: list[int | float], floating_points: int | None = None) -> float:
        """
        Computes the standard deviation of an array.

        - array: An array of floats or integers.
        - floating_points: Limits returned results to floating points accuracy.
        """
        if floating_points:
            return round(self.variance(array=array) ** .5, floating_points)

        return self.variance(array=array) ** .5



if __name__ == "__main__":

    # speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
    # speed = [32,111,138,28,59,77,97]
    # speed = [12,5,77, 545, 77]
    speed = [99,86,87,88,111,86,103,87,94,78,77,85,86,99,99,99,99]
    # speed = np.linspace(1, 1000000, 10000000)
    # speed = [n**2 for n in range(1, 100000001)]

    # Instantiation
    mine = Stat()
    system("clear")






    # Mean Test

    # Statistics module
    print("\n### Mean Test ###\n".upper())
    tic = perf_counter()
    mean_from_Statistics_module = statistics.mean(speed)
    time_from_Statistics_module = perf_counter() - tic
    print(f"mean_from_Statistics_module: {mean_from_Statistics_module} at {time_from_Statistics_module} second(s)".replace("_", " ").upper())

    # Numpy module
    tic = perf_counter()
    mean_from_Numpy_module = np.mean(speed)
    time_from_Numpy_module = perf_counter() - tic
    print(f"mean_from_Numpy_module: {mean_from_Numpy_module} at {time_from_Numpy_module} second(s)".replace("_", " ").upper())

    # Stat module
    tic = perf_counter()
    mean_from_Stat_module = mine.mean(array=speed)
    time_from_Stat_module = perf_counter() - tic
    print(f"mean_from_Stat_module: {mean_from_Stat_module} at {time_from_Stat_module} second(s)".replace("_", " ").upper())

    # Speed calculation
    times = [time_from_Statistics_module, time_from_Numpy_module, time_from_Stat_module]
    times_list = ["Statistics module", "Numpy module", "Stat module"]
    print(f"{times_list[times.index(min(times))]} wins ✅".upper())






    # Median Test

    # Statistics module
    print("\n### Median Test ###\n".upper())
    tic = perf_counter()
    median_from_Statistics_module = statistics.median(speed)
    time_from_Statistics_module = perf_counter() - tic
    print(f"median_from_Statistics_module: {median_from_Statistics_module} at {time_from_Statistics_module} second(s)".replace("_", " ").upper())

    # Numpy module
    tic = perf_counter()
    median_from_Numpy_module = np.median(speed)
    time_from_Numpy_module = perf_counter() - tic
    print(f"median_from_Numpy_module: {median_from_Numpy_module} at {time_from_Numpy_module} second(s)".replace("_", " ").upper())

    # Stat module
    tic = perf_counter()
    median_from_Stat_module = mine.median(array=speed)
    time_from_Stat_module = perf_counter() - tic
    print(f"median_from_Stat_module: {median_from_Stat_module} at {time_from_Stat_module} second(s)".replace("_", " ").upper())

    # Speed calculation
    times = [time_from_Statistics_module, time_from_Numpy_module, time_from_Stat_module]
    times_list = ["Statistics module", "Numpy module", "Stat module"]
    print(f"{times_list[times.index(min(times))]} wins ✅".upper())






    # Mode Test

    # Statistics module
    print("\n### Mode Test ###\n".upper())
    tic = perf_counter()
    mode_from_Statistics_module = statistics.mode(speed)
    time_from_Statistics_module = perf_counter() - tic
    print(f"mode_from_Statistics_module: {mode_from_Statistics_module} at {time_from_Statistics_module} second(s)".replace("_", " ").upper())

    # Stat module
    tic = perf_counter()
    mode_from_Stat_module = mine.mode(array=speed)
    time_from_Stat_module = perf_counter() - tic
    print(f"mode_from_Stat_module: {mode_from_Stat_module} at {time_from_Stat_module} second(s)".replace("_", " ").upper())

    tic = perf_counter()
    mode_from_Stat_module_beta_1 = mine.mode_beta1(array=speed, show_frequency=True)
    time_from_Stat_module_beta_1 = perf_counter() - tic
    print(f"mode_from_Stat_module_beta_1: {mode_from_Stat_module_beta_1} RuntimeSB1: {time_from_Stat_module_beta_1} second(s)".replace("_", " ").upper())

    tic = perf_counter()
    mode_from_Stat_module_beta_2 = mine.mode_beta2(array=speed, show_frequency=True)
    timeS_from_Stat_module_beta_2 = perf_counter() - tic
    print(f"mode_from_Stat_module_beta_2: {mode_from_Stat_module_beta_2} RuntimeSB2: {timeS_from_Stat_module_beta_2} second(s)".replace("_", " ").upper())

    # Speed calculation
    times = [time_from_Statistics_module, time_from_Stat_module, time_from_Stat_module_beta_1, timeS_from_Stat_module_beta_2]
    times_list = ["Statistics module", "Stat module", "Stat module Beta 1", "Stat module Beta 2"]
    print(f"{times_list[times.index(min(times))]} wins ✅".upper())






    # Variance Test

    # Statistics module
    print("\n### Variance Test ###\n".upper())
    tic = perf_counter()
    variance_from_Statistics_module = statistics.variance(speed)
    time_from_Statistics_module = perf_counter() - tic
    print(f"variance_from_Statistics_module: {variance_from_Statistics_module} at {time_from_Statistics_module} second(s)".replace("_", " ").upper())

    # Numpy module
    tic = perf_counter()
    variance_from_Numpy_module = np.var(speed)
    time_from_Numpy_module = perf_counter() - tic
    print(f"variance_from_Numpy_module: {variance_from_Numpy_module} at {time_from_Numpy_module} second(s)".replace("_", " ").upper())

    # Stat module
    tic = perf_counter()
    variance_from_Stat_module = mine.variance(array=speed)
    time_from_Stat_module = perf_counter() - tic
    print(f"variance_from_Stat_module: {variance_from_Stat_module} at {time_from_Stat_module} second(s)".replace("_", " ").upper())

    # Speed calculation
    times = [time_from_Statistics_module, time_from_Numpy_module, time_from_Stat_module]
    times_list = ["Statistics module", "Numpy module", "Stat module"]
    print(f"{times_list[times.index(min(times))]} wins ✅".upper())






    # Standard Deviation Test

    # Statistics module
    print("\n### Standard Deviation Test ###\n".upper())
    tic = perf_counter()
    std_from_Statistics_module = statistics.stdev(speed)
    time_from_Statistics_module = perf_counter() - tic
    print(f"std_from_Statistics_module: {std_from_Statistics_module} at {time_from_Statistics_module} second(s)".replace("_", " ").upper())

    # Numpy module
    tic = perf_counter()
    std_from_Numpy_module = np.std(speed)
    time_from_Numpy_module = perf_counter() - tic
    print(f"std_from_Numpy_module: {std_from_Numpy_module} at {time_from_Numpy_module} second(s)".replace("_", " ").upper())

    # Stat module
    tic = perf_counter()
    std_from_Stat_module = mine.std(array=speed)
    time_from_Stat_module = perf_counter() - tic
    print(f"std_from_Stat_module: {std_from_Stat_module} at {time_from_Stat_module} second(s)".replace("_", " ").upper())

    # Speed calculation
    times = [time_from_Statistics_module, time_from_Numpy_module, time_from_Stat_module]
    times_list = ["Statistics module", "Numpy module", "Stat module"]
    print(f"{times_list[times.index(min(times))]} wins ✅".upper())


