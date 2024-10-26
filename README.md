# Python shuf Implementation
A Python 3 script (shuf.py) that replicates the functionality of the GNU shuf command, allowing for easier customization and extension.

## Features
Options Supported:
- --echo (-e): Accepts input values directly from the command line.
- --input-range (-i): Generates a list of values from a specified range.
- --head-count (-n): Limits the number of results.
- --repeat (-r): Allows repeated output; if used without -n, runs indefinitely.
- --help: Displays usage information.
## Input Handling:
- No arguments or a single -: Reads from standard input.
- Single non-option argument: Reads from the specified file.
## Error Handling: 
- Reports errors for invalid arguments, similar to GNU shuf.
