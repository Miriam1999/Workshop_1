"""
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project: My first workshop                                                                          -- #
# -- script: main.py: python script with the main functionality                                          -- #
# -- author: Miriam1999                                                                                  -- #
# -- license: GPL-3.0                                                                                    -- #
# -- repository: https://github.com/Miriam1999/Workshop_1                                                -- #
# -- --------------------------------------------------------------------------------------------------- -- #
"""

import data as dt
import functions as fn
import numpy as np

# Read input data
data_ob = dt.ob_data

# Order books total amount
n_books = len(list(data_ob.keys()))
print(f"The amount of order books is: {n_books}")

# OrderBook Metrics
data_1 = fn.f_descriptive_ob(data_ob = data_ob) 

# Cell 3
print(f"Expected median time for a new Order Book: {data_1['median_ts_ob']}")

# Cell 4
print(f"Expected median time for a new Order Book: {data_1['Orderbook Imbalance']}")

# -- Revision exercises
data_ob[list(data_ob.keys())[1]]['bid_size'][0]

book_0 = data_ob[list(data_ob.keys())[0]].copy()

book_0.index = book_0.index.astype(np.int64)

# List comprehension [element1, element2, element3...]
new_list = [i + 1e3 for i in list(book_0['bid_size'])]

# Dictionary comprehension {'key 1': object, 'key 2': object...}
new_key = {'key_' + str(i): list(book_0['bid_size'])[i] for i in range(0, len(list(book_0['bid_size'])))}