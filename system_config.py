import os
import sys
import pandas as pd

print(sys.executable)

transactions = pd.read_csv("files/transactions.csv")

print(transactions)