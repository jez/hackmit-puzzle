# HackMIT Puzzle 2014

Just a little repository where we can collaborate on code samples.

Currently, you can check out the [HACK-ASCII](/HACK-ASCII) directory to 
try and figure out what all these lines of random hex data mean. I've 
made a few tests to try different things, and the format of them should
become pretty apparent. I tried to write some doc strings.

## Usage

To run the tests for HACK-ASCII, once you've cloned the repo, cd into 
HACK-ASCII and run `./puzzletester.py`. That's it.

## Notes about `map.pdf`
This is the QR puzzle.

First, I took the pdf that was linked [here](www.mediafire.com/view/fjydb0mnj60ek7q/map.pdf),
downloaded it, and ran it through [this tool](http://pdf2jpg.net/) to get a bunch of jpgs.

I took the jpgs, then ran the following commands:

```
$ convert +append map-page-0{01,02,03,04,05}.jpg out1.jpg
$ convert +append map-page-0{06,07,08,09,10}.jpg out2.jpg
$ convert +append map-page-0{11,12,13,14,15}.jpg out3.jpg
$ convert +append map-page-0{16,17,18,19,11}.jpg out4.jpg
$ convert +append map-page-0{21,22,23,24,25}.jpg out5.jpg

$ convert -append out{1,2,3,4,5}.jpg out.jpg

```

And there you go.
