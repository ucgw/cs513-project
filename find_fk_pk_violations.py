#!/usr/bin/env python3

import sys
import os

no_headers = os.environ.get('NOHEAD', None)

Usage = f'Usage: {sys.argv[0]} <FK filename> <PK filename> [skip empty]\n'

fk_set = set([])
pk_set = set([])

debugline = None
debugline_number = 0
skip_emptyline = False

try:
  FK_filename = sys.argv[1]
  PK_filename = sys.argv[2]

  if len(sys.argv) == 4:
    skip_emptyline = True

  with open(FK_filename) as fkfh:
    line = fkfh.readline()
    while line:
      line = line.strip()
      debugline_number += 1
      debugline = f'file: {FK_filename} line no: {debugline_number}  :{line}:'
      if skip_emptyline is True:
        if line == '':
          line = fkfh.readline()
          continue
      fk_set.add(int(line))
      line = fkfh.readline()
      debugline = None

  debugline = None
  debugline_number = 0

  with open(PK_filename) as pkfh:
    line = pkfh.readline()
    while line:
      line = line.strip()
      debugline_number += 1
      debugline = line
      debugline = f'file: {PK_filename} line no: {debugline_number}  :{line}:'
      pk_set.add(int(line))
      line = pkfh.readline()
      debugline = None

except Exception as err:
  sys.stderr.write(f'Error Caught: {err}\n\n')
  if debugline is not None:
    sys.stderr.write(f'DEBUG LINE: {debugline}\n')
  sys.stderr.write(f'{Usage}\n')
  sys.exit(1)

# foreign keys that exist in set but not in
# primary keys set
fk_notin_pk = fk_set.difference(pk_set)

fk_unique_count = len(fk_set)
pk_unique_count = len(pk_set)
fk_notin_pk_count = len(fk_notin_pk)

if no_headers is None:
  print(f'unique FKs: {fk_unique_count}')
  print(f'unique PKs: {pk_unique_count}')
  print(f'FKs not in PKs: {fk_notin_pk_count}')

for fk in fk_notin_pk:
  print(fk)
