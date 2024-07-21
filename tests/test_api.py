import os
import sys
import datetime

sys.path.insert(1,  os.getcwd() + "\\code\\")
import api





top = api.get_top_stories()
story = api.get_item(top[0])



print(story)


d = {"hi"   : "1234",
     "hello"    :   "zibi"}

print(d)

print(d["hi"])
print(d.get("hello"))
print(d.get("mo",""))

dt = datetime.datetime.now()
print(dt)

print(dt.month)

# dt = datetime.datetime.fromtimestamp
# print(dt)

# print(dt.month)
print(dt.weekday())



# importing the required libraries
import matplotlib.pyplot as plt
import numpy as np

# define data values
x = [1, 2, 3, 4] # X-axis points
#x = np.array([1, 2, 3, 4]) # X-axis points
y = [2,15,6,8] # Y-axis points

plt.plot(x, y) # Plot the chart
plt.show() # display



# daytes = [0,1,2,3,4,5,6]
daytes = [6,1,4,3,2,5,0]
grades = [53,48,95,43,82,1,0.2]

pack = {}

for i in range(7):
    pack[daytes[i]] = grades[i]
    
print(pack)


unpack = list(zip(pack.keys(), pack.values()))
print(unpack)

unpack.sort()

print(unpack)


# importing the module
import pandas as pd
from IPython.display import display


import pandas as pd
import numpy as np
import matplotlib as mpl
import tkinter as tk

stat = {
    "strings": ["Adam", "Mike"],
    "ints": [1, 3],
    "floats": [1.123, 1000.23]
}
data = pd.DataFrame(stat)

#df.style \
  # .format(precision=3, thousands=".", decimal=",") \
  # .format_index(str.upper, axis=1) \
  # .relabel_index(["row 1", "row 2"], axis=0)

# plt.table(cellText=stat.values(),
#                       rowLabels=stat.values(),
#                       rowColours=stat.keys(),
#                       colLabels=None,
#                       loc='bottom')

root = tk.Tk()
root.title("Data Display")

# Assuming data is a pandas DataFrame
for i, row in data.iterrows():
    for j, value in enumerate(row):
        label = tk.Label(root, text=str(value))
        label.grid(row=i, column=j)

root.mainloop()

import pandas as pd


# def display_data(data):
#     root = tk.Tk()
#     root.title("Data Display")

#     # Assuming data is a pandas DataFrame
#     for i, row in data.iterrows():
#         for j, value in enumerate(row):
#             label = tk.Label(root, text=str(value))
#             label.grid(row=i, column=j)

#     root.mainloop()

# # Load your data (replace with your data source)
# data = pd.read_csv("top_comments.csv")

# display_data(data)
