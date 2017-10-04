import requests
import json
import numpy
from collections import OrderedDict
import argparse
import sys

def get(x):
    """
    Fetch value from the API

    Example response: {"data": {"y": 89.05135264760057, "x": 3.4}}
    """
    r = requests.get("http://165.227.157.145:8080/api/do_measurement?x={}".format(x))

    if r.status_code == 200:
        #print(json.dumps(r.json()))
        return (r.json())["data"]

    else:
        print("Error {}".format(r.status_code))

def output_gnuplot(data):
    print("# GNU Plot data, use plot.gnu to plot")
    for i in data:
        print("{0} {1}".format(i, numpy.average(data[i])))


if __name__ == "__main__":

    """
    key: x value
    value: [] array of y
    """
    results = OrderedDict()
    avg = dict()
    x_list = list()
    y_list = list()

    parser = argparse.ArgumentParser(description='Try to find the generating polynomial. ML Weekend @ 2017. Petr Stehlik <pe.stehlik@gmail.com>')

    parser.add_argument('--file', '-f', type=str, default=None, dest="file", help='Load data from a file. If not specified data are loaded from REST API.')
    parser.add_argument('--max', type=float, default=10.0, dest="max", help="Specify maximum value for iteration (default: 10)")
    parser.add_argument('--min', type=float, default=-10.0, dest="min", help="Specify minimum value for iteration (default: -10.0)")
    parser.add_argument('--step', type=float, default=1.0, dest="step", help="Specify step for iteration (default: 1.0)")
    parser.add_argument('--dump', '-d', type=str, default=None, dest="dump", help="Dump measured results in a JSON format to specified file")

    args = vars(parser.parse_args())

    if args['file'] == None:
        # Fetch from API and process
        for x in numpy.arange(args["min"],args["max"] + 1.0, args["step"]):
            results[str(x)] = list()

            for y in range(0,5):
                # Measure everything 5 times
                r = get(x)

                if r["y"] == None:
                    # No value for given point, delete and skip
                    del results[str(x)]
                    break

                results[str(r["x"])].append(r["y"])

        if args['dump'] != None:
            # Dump the results
            with open(args['dump'], 'w') as f:
                json.dump(results, f)

    else:
        with open(args['file']) as f:
            # Open specified JSON file and parse it.
            # No verification of the format is done since it is over the scope of this code
            results = json.load(f, object_pairs_hook=OrderedDict)

    for i in results.keys():
        # Create list of X and Y values for polynomial computation
        x_list.append(float(i))
        y_list.append(numpy.average(results[i]))

    # Output results in gnuplot format
    output_gnuplot(results)

    # Compute polynomial up to 10-th power
    polys = numpy.polyfit(x_list, y_list, 10)

    print("# Resulting polynomial: \n# ", end="")
    for i in range(0, len(polys) - 1):
        if not numpy.isclose(polys[i], 0.00000):
            print("%.8f*x**%i + " % (polys[i], 10-i), end="")

    # Print last polynomial member
    print("%.8f" % (polys[-1]))


