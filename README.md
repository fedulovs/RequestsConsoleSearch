## Requirements

1. Python 3
2. Requests library
> pip3 install requests

## How to launch

1. Open command line
2. Type the following command

> python3 yousician.py

## Solution

Firstly we ask a user for an input and puts it as query parameter.
Then we make a request with this parameter and X-Application-Name header.
If is_response_successful returns true it takes exercises object from response.
Then a dict of songs is created and appended in cycle with artist as a key and song as a value.
If an artist occurs for the first time we create a new dict with this artist(key) and a list of songs(value).
Afterwards dict of songs is going through sort_and_print method in which we first sort artists by name, 
and then we sort songs of each artist separately. 
Finally, we print artist + song for each song in songs list.

I've also covered a case when we won't have any response because of lost connection with easy try catch.
