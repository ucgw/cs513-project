#!/usr/bin/env python3

import pandas as pd
import sys
import re

df = None

try:
  filename = sys.argv[1]
  df = pd.read_csv(filename)
except Exception as err:
  sys.stderr.write(f'Error Caught: {err}\n\n')
  sys.stderr.write(f'Usage: {sys.argv[0]} <csv filename>\n')
  sys.exit(1)

print(df['id'])
#print(dir(df))
