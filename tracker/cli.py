import argparse

import main

def parse_args():
  parser = argparse.ArgumentParser()
  parser.add_argument("file")
  parser.add_argument("exchange")
  return parser.parse_args()


if __name__ == '__main__':
  from sys import path
  from os.path import dirname as dir

  path.append(dir('.'))

  args = parse_args()
  main.generate_report(args.file, args.exchange)
