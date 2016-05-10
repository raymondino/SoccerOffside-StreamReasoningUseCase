__author__ = 'Hao'

import os
from pprint import *
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
        return "throughput", get_value_from_string(words[2])

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

    all = {}

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
                                # print(this_algorithm, end=": ")
                                # print(parse_line(line))
                                this_par, this_val = parse_line(line)
                                if this_algorithm not in all:
                                    all[this_algorithm] = {}
                                    all[this_algorithm][this_par] = [this_val]
                                elif (this_algorithm in all) and (this_par not in all[this_algorithm]):
                                    all[this_algorithm][this_par] = [this_val]
                                else:
                                    all[this_algorithm][this_par].append(this_val)


    # pprint(all)

    ALGORITHM_CATEGORIES = ["FIFO", "LFU", "LRU", "DL"]

    SUMMARY_PARAMETERS = [
        "throughput",
        "eviction-rate",
        "average-sparql-time",
        "average-explanation-time",
        "average-filter-time"
    ]

    PARAMETER_MAPPING = {
        "throughput": "Throughput",
        "eviction-rate": "Eviction",
        "average-sparql-time": "SPARQL(s)",
        "average-explanation-time": "Explanation(s)",
        "average-filter-time": "DL filtering(s)"
    }

    summary = dict((k, dict((k1,[]) for k1 in ALGORITHM_CATEGORIES)) for k in SUMMARY_PARAMETERS)
    # summary = dict((k, dict((k1,[]) for k1 in ALGORITHM_CATEGORIES)) for k in PARAMETER_MAPPING.keys())


    for alg in all:

        # print(alg)
        which_categories = [x for x in ALGORITHM_CATEGORIES if x in alg]
        # print(which_categories)

        for which_category in which_categories:
            for which_parameter in all[alg]:
                if which_parameter in SUMMARY_PARAMETERS:
                    # print(all[alg][which_parameter])
                    summary[which_parameter][which_category] += all[alg][which_parameter]





            #     mean([x for x in all[alg][par] if x is not None])

    # pprint(summary)

    for parameter in summary:
        for category in summary[parameter]:
            # print(parameter + " " + category + str(summary[parameter][category]))
            if len(summary[parameter][category]) == 0:
                summary[parameter][category] = 0
            else:
                summary[parameter][category] = mean([x for x in summary[parameter][category] if x is not None])


    # pprint(summary)

    # Now let's print out the table

    print(" & " + " & ".join(ALGORITHM_CATEGORIES), end=" \\\\ \n")
    for parameter in SUMMARY_PARAMETERS:
        line = [PARAMETER_MAPPING[parameter]]
        for algorithm in ALGORITHM_CATEGORIES:
            line.append(str(round(summary[parameter][algorithm], 2)))
        print(" & ".join(line), end=" \\\\ \n")




if __name__ == "__main__":
    main()

