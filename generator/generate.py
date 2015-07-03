

import pystatsd
import random
import time

print 'starting generator'

statsd = pystatsd.Client('statsd', 8125)

#statsd.timing('python_test.time',500)
#statsd.increment('python_test.inc_int')
#statsd.decrement('python_test.decr_int')
#statsd.gauge('python_test.gauge', 42)


def request(delay):
    statsd.increment('statsd.app.tester.metric.request_counter')
    statsd.timing('statsd.app.tester.metric.request_duration', delay)
    print "3333#####", delay

while True:
    delay = 100 * random.lognormvariate(0, 0.25)
    request(delay)
    time.sleep(1)

