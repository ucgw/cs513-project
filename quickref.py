#!/usr/bin/env python3

import sys
import os
import csv

content = {
  'data': [],
  'header': []
}

no_headers = os.environ.get('NOHEAD', None)

Usage = f'Usage: {sys.argv[0]} <csv filename> <record start index> <record count> [<field1>,...]\n'

def print_headers():
  for f in content['header']:
    print(f'{f}')

def print_record_count():
  record_count = len(content['data'])
  print(f'records: {record_count}')

def print_records(start,count,fields=[]):
  indexes = []
  field_index = None
  headers = content['header']
  if isinstance(fields, list) is True:
    indexes = [idx for (idx,f) in enumerate(headers) if f[1] in fields]

  if len(indexes) > 0:
    if no_headers is None:
      sys.stdout.write('====\n')
      for idx in indexes:
        field_name = content['header'][idx]
        sys.stdout.write(f"{field_name[1]} | ")
      sys.stdout.write('\n')
      sys.stdout.write('====\n')
    for record in content['data'][start:(start+count)]:
      for idx in indexes:
        sys.stdout.write(f'{record[idx]} | ')
      sys.stdout.write('\n')
  else:
    if no_headers is None:
      sys.stdout.write('====\n')
      for idx in range(0,len(content['header'])):
        field_name = content['header'][idx]
        sys.stdout.write(f"{field_name[1]} | ")
      sys.stdout.write('\n')
      sys.stdout.write('====\n')
    for record in content['data'][start:(start+count)]:
      for idx in range(0,len(content['header'])):
        sys.stdout.write(f'{record[idx]} | ')
      sys.stdout.write('\n')

try:
  filename = sys.argv[1]
  with open(filename) as csvfh:
    header_seen = False
    headers = []
    csv_reader = csv.reader(csvfh)
    for row in csv_reader:
      if header_seen is True:
        content['data'].append(row)
      else:
        headers = row
        header_seen = True
  for idx,field_name in enumerate(headers):
    content['header'].append([idx,field_name])
except Exception as err:
  sys.stderr.write(f'Error Caught: {err}\n\n')
  sys.stderr.write(f'{Usage}\n')
  sys.exit(1)

start_idx = None
count = None
fields = []

try:
  start_idx = int(sys.argv[2])
  count = int(sys.argv[3])
  fields = sys.argv[4:]
except Exception:
  pass

if isinstance(start_idx, int) is False or \
   isinstance(count, int) is False:
  sys.stderr.write(f'Error: start and count inputs need to be numbers\n\n')
  sys.stderr.write(f'{Usage}\n')
  sys.exit(1)

if no_headers is None:
  print_headers()
  print_record_count()
print_records(start_idx, count, fields)
