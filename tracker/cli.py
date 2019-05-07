import argparse

import orchestrator


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
    print("Generating report for {} based on data in {}.\n\n".format(args.exchange.capitalize(), args.file))
    results = orchestrator.generate_report(args.file, args.exchange, 'csv')
    print('\n'.join(results))
