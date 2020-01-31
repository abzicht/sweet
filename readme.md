# S(plit T)weet

This is a python based tool for splitting threads into multiple tweets, making
it easier and faster to post long stories on
[twitter.com](https://twitter.com).

## Usage

Examples:

```bash
# Read a thread from thread.txt and print the split tweets to STDOUT
sweet -i thread.txt

# Read a thread from STDIN and print the split tweets to STDOUT
cat thread.txt | sweet

# Read a thread from STDIN and store the split tweets at tweets.txt
cat thread.txt | sweet -o tweets.txt

# Read a thread from STDIN and print the split tweets to STDOUT
# Instead of the default tweet length (280), use 140
cat thread.txt | sweet -m 140
```

```python
from sweet.sweet import Sweet

with open('thread.txt', 'r') as thread_file:
    thread = thread_file.read()

sweet = Sweet(max_chars = 280)
tweets = sweet.compose_tweets(thread, sweet.split_v2)

print(tweets)
```

## Description

`sweet` splits tweets based on a defined set of separators. The separators are:
`\n\n`, `.`, and ` `. They are used in this order. There are multiple
algorithms 

## Algorithms

There are multiple algorithms, called `split_v1`, `split_v2`, etc. Each behaves
differently and splits tweets in a different manner. Implement a split
algorithm by defining a function that takes a string as input and returns a
list of strings. Pass that function to `sweet` with the `compose_tweets`
function.

Example:

```
from sweet.sweet import Sweet

with open('thread.txt', 'r') as thread_file:
    thread = thread_file.read()

def split_algorithm(thread:str) -> list:
    tweets = []
    ...
    return tweets

sweet = Sweet()
tweets = sweet.compose_tweets(thread, split_algorithm)
print(tweets)
```

## Installation

```bash
git clone https://gitub.com/abzicht/sweet
cd sweet
python3 setup.py install --user
```
