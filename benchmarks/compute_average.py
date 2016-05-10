__author__ = 'Hao'

import os
from statistics import *

ALGORITHMS = ["FIFO", "LFU", "LRU"]


def get_value_from_string(s):
    if s == "NaN":
        return None
    else:
        try:
            value = float(s)
            return value
        except:
            return None


def parse_line(line):
    words = line.split()
    if len(words) == 0:
        return False

    elif words[0] == "running":
        return "running-time", get_value_from_string(words[3])

    elif words[0] == "throughtput":
        return "throughtput", get_value_from_string(words[2])

    elif words[0:3] == ["average", "sparql", "time"]:
        return "average-sparql-time", get_value_from_string(words[4])

    elif words[0:3] == ["average", "explanation", "time"]:
        return "average-explanation-time", get_value_from_string(words[4])

    elif words[0:3] == ["average", "filter", "time"]:
        return "average-filter-time", get_value_from_string(words[4])

    elif words[0:3] == ["average", "filtered", "triples"]:
        return "average-filtered-triples", get_value_from_string(words[4])

    elif words[0] == "eviction":
        return "eviction-rate", get_value_from_string(words[3])

    elif words[0] == "maxTripleUsed":
        return "maxTripleUsed", get_value_from_string(words[2])

    else:
        return False



def main():
    # print("Hello world!")

    summary = {}

    for algorithm in ALGORITHMS:
        for root, dirs, filenames in os.walk(algorithm):

            this_algorithm = ""

            for filename in filenames:
                with open(algorithm + "/" + filename) as file:
                    for line in file:

                        if line[0:3] in ALGORITHMS or line[0:4] in ALGORITHMS:
                            this_algorithm = line.strip()
                            continue

                        else:
                            if parse_line(line):
                                print(this_algorithm, end=": ")
                                print(parse_line(line))
                                this_par, this_val = parse_line(line)
                                if this_algorithm not in summary:
                                    summary[this_algorithm] = {}
                                    summary[this_algorithm][this_par] = [this_val]
                                elif (this_algorithm in summary) and (this_par not in summary[this_algorithm]):
                                    summary[this_algorithm][this_par] = [this_val]
                                else:
                                    summary[this_algorithm][this_par].append(this_val)


    print(summary)
    #
    # for alg in summary:
    #     print(alg)
    #     for par in summary[alg]:
    #         print("    " + par, end=": ")
    #         # print(summary[alg][par])
    #         print(str(mean([x for x in summary[alg][par] if x is not None])))


if __name__ == "__main__":
    main()

