import re
import numpy as np
import sys

def calculate_stats_on_spreads(spreads):
    print('\tMax: ' + str(max(spreads)))
    print('\t95th: ' + str(np.percentile(spreads, 95)))
    print('\t90th: ' + str(np.percentile(spreads, 90)))
    print('\t75th: ' + str(np.percentile(spreads, 75)))
    print('\t50th: ' + str(np.percentile(spreads, 50)))
    print('\t25th: ' + str(np.percentile(spreads, 25)))
    print('\t10th: ' + str(np.percentile(spreads, 10)))
    print('\t5th: ' + str(np.percentile(spreads, 5)))
    print('\tMin: ' + str(min(spreads)))
    print()
    print('\tMin-Max spread: ' + str(max(spreads) - min(spreads)))
    print('\t95th-5th spread: ' + str(np.percentile(spreads, 95) - np.percentile(spreads, 5)))
    print('\t90th-10th spread: ' + str(np.percentile(spreads, 90) - np.percentile(spreads, 10)))
    print('\t75th-25th spread: ' + str(np.percentile(spreads, 75) - np.percentile(spreads, 25)))

def get_current_spread(line):
    spread_regex = re.compile('(-?\d+\.\d+)% \[')
    return float(spread_regex.search(line).group(1))

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: ' + sys.argv[0] + '[log_file]')
        sys.exit(1)

    log_file = sys.argv[1]

    with open(log_file, 'r') as f:
        data = [x.strip() for x in f.readlines()]

    exchange_pair_regex = re.compile('(\w+\/\w+)')
    data = [d for d in data if exchange_pair_regex.match(d)]
    exchange_pairs = sorted(set([exchange_pair_regex.search(d).group(1) for d in data]))

    data_by_exchange_pairs = {}
    for exchange_pair in exchange_pairs:
        ep_data = [d for d in data if exchange_pair in d]
        spreads = [get_current_spread(d) for d in ep_data]
        print(exchange_pair + str(': (') + str(len(ep_data)) + ' rows)')
        calculate_stats_on_spreads(spreads)
        print()



