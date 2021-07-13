import math
import numpy as np
import pandas as pd
def calculate_axis_ticks(max_value, max_ticks = 10, min_ticks = 5, axis_length = 50):


    def floor(number, bound=1):
        return bound * np.floor(number / bound)

    def nearest_floor_round(number):
        return floor(number, 10 ** (len(str(number))-1))

    n_ticks = nearest_floor_round(max_value) /  (10 ** (len(str(max_value)) -1 ))
    for i in range(10):
        if n_ticks < min_ticks:
            n_ticks *= 2
        else:
            break
    for i in range(10):
        if n_ticks > max_ticks:
            n_ticks /= 2
            n_ticks = int(n_ticks)
        else:
            break

    axis_ticks = np.arange(0, max_value + 1, nearest_floor_round(max_value) / n_ticks, dtype = int) # add one to include endpoint 
    #axis_ticks_str = [str(t) for t in axis_ticks]
    if np.sum([len(str(t)) for t in axis_ticks]) > axis_length:
        print("Warning: axis length exceeded by tick numbers")

    
    return axis_ticks


def axis_ticks_from_df(df, value_column, frame_index, max_ticks = 10, min_ticks = 5, axis_length = 100):

    max_value = df[df["frame_index"] == frame_index][value_column].max()
    print(df[df["frame_index"] == frame_index][value_column])
    print(max_value)
    axis_ticks = calculate_axis_ticks(int(max_value), min_ticks = min_ticks, max_ticks=max_ticks, axis_length= axis_length)

    return axis_ticks


if __name__=='__main__':

    for i in [101, 10001, 2222, 3433, 5555, 9800, 10000, 13001, 20000, 25000, 27000,]:
        axis_ticks = calculate_axis_ticks(i, min_ticks = 2, max_ticks=10)

        print(i, axis_ticks)

    #df = pd.read_csv('../data/enhanced_global_covid_data.csv')
    #print("df:")
    #print(df)

    #axis_ticks = axis_ticks_from_df(df, "n_infected", frame_index = 5000)

    #print("axis_ticks from df:")
    #print(axis_ticks)

    axis_ticks = calculate_axis_ticks(101000, max_ticks = 5, min_ticks = 3, axis_length = 100)

    print(axis_ticks)
