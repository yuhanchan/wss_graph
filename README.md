Credit: The Working Set Size (WSS) tool is created by Brendan Gregg, further details can be found 		http://www.brendangregg.com/wss.html

graph.sh: Use the wss tool to measure and record the working set size of a specific process. Program runs for two times, the first time measures the accumulative memory usage of in a certain amount of time. The second time measures the amount of memory being used every single second.

graph.py: use the data collected in graph.sh, plot the working set size versus time. The blue line represent the accumulative memory usage (The first time measure), and the red line represent the memory used in every second (The second time meaure), which indicates the hottest memory in use.


Usage: sudo ./graph.sh [test program name] [how long to measure]
e.g. sudo ./graph/.sh test.py 5

Note that it would take twice as [how long to measure] to run because it will run the program twice.
