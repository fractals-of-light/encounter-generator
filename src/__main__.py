import pandas as pd
import os
import numpy as np


def import_file():
    data_frame = pd.read_csv("../resources\\monster_list_small.csv")
    print(data_frame)



if __name__ == '__main__':
    print("generating encounter")
    import_file()