"""
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project: My first workshop                                                                          -- #
# -- script: main.py: python script with the main functionality                                          -- #
# -- author: Miriam1999                                                                                  -- #
# -- license: GPL-3.0                                                                                    -- #
# -- repository: https://github.com/Miriam1999/Workshop_1                                                -- #
# -- --------------------------------------------------------------------------------------------------- -- #
"""

import pandas as pd
import numpy as np
import json

# Load file
f = open('orderbooks_05jul21.json')

# Convert JSON into Dictionary
orderbooks_data = json.load(f)
ob_data = orderbooks_data['bitfinex']

# Drop None Keys
ob_data = {i_key: i_value for i_key, i_value in ob_data.items() if i_value is not None}

# Convert to DataFrame and rearange columns
ob_data = {i_ob: pd.DataFrame(ob_data[i_ob])[['bid_size', 'bid', 'ask', 'ask_size']]
          if  ob_data[i_ob] is not None else None for i_ob in list(ob_data.keys())}