# Movie-Theater-Seating-Challenge

## How to run:
1. You can run on command line with an input filepath as arguement:

    $ python3 seatAssigner.py [input_filepath]

2. You can also run the script "run" to test up to all input files at once,
    where all input files listed in the script are included in this repo

    $ chmod +x run
    $ ./run

For each, the output filename is printed to stdout

### Assumptions
1. Reservation requests would be served in order - led to greedy approach
    
2. People want to sit in a "better" row (rankings in code), and they would
   rather than sit in a more favorible row with others than sit in a less
   favorable row by themselves

3. Groups over 20 would be treated as seperate groups in given input file

#### Improvements: 
1. Attempt to rearrange rows if greedy algo is cause of group not fitting

2. Stagger people row to row for optimal view from their seat

