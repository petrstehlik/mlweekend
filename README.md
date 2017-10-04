# Machine Learning Weekend Entry Task

## Entry task story
Taken from [4. 10. 2017]: https://github.com/kiwicom/mlweekend

Since the summer was kind of boring, you applied for a temporary contract on the dark web. It turned out that you’re the only data scientist in the team; the others are mostly hackers doing industrial espionage. Long story short, after some work on their side, they provided you with VPN access to a factory in Kazakhstan. They’ve enabled you to call the endpoint of one of the machines where a secret mathematical formula is hidden. Your goal is to get the formula. Unfortunately, the machine works like a black box — you can just send an _x_-value to it

`/api/do_measurement?x=4` (the IP will be specified in the e-mail)

    to measure the _y_-value within the resulted JSON

    `{"data": {"y": 188.58938971580736, "x": 4.0}}`

    It looks like that the machine is just a working prototype, so the readings are a bit fuzzy and it’s probably a good idea to do more measurements to get some reasonable data. Also for some intervals of _x_, the _y_-values are missing; feel free to interpolate.

    Your task is do the measurements, get the secret formula _f_ where _y = f(x)_ and send it to the organisers (with a graph included). Please use Numpy and attach (or link) all the code you’ve used.

    Send your solution to <a href="mailto:mlweekend@kiwi.com">mlweekend@kiwi.com</a> no later than midnight on Sunday, October 22. We'll send you our evaluation by Tuesday, October 24. The sooner you send your solution, the sooner we'll let you know.

## About the Code
The code utilizes only numpy and requests modules. Other than that is custom work. The heavy lifting (polynomial fitting) is done using numpy.polyfit. There is no need for interpolation if you data sample is big enough :) such as one here `dump_20k.json`. For demo purposes the polynomial is plotted in `res_20k.svg` together with used values using GNU Plot.

## Usage
Use `-h` argument to learn about possible options or just read the code!

In short the code can obtain data from the REST API, process it and dump it or you can give it an existing dump of data. It is up to you but the format is quite strict.
