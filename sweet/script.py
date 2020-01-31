#!/bin/python3

try:
    from sweet.sweet import Sweet
except ImportError:
    from sweet import Sweet
import sys
import argparse

def main():
    parser = argparse.ArgumentParser(description="""
    S(plit t)weet.
    Split threads into single tweets.
    Tweet separators: '\\n\\n', '.', and ' '.
    Make sure that separators occur in intervals smaller than --max-chars.
    """)
    parser.add_argument('-i', '--input-file', dest='input_file', type=str,
                        help="""
                        The thread file. Default: STDIN.
                        """)
    parser.add_argument('-o', '--output-file', dest='output_file', type=str,
                        help="""
                        The file all tweets are saved to. Default: STDOUT.
                        """)
    parser.add_argument('-m', '--max-chars', dest='max_chars', type=int,
                        default=280,
                        help="""
                        The maximum number of chars each tweet shall have.
                        Default: 280.
                        """)

    args = parser.parse_args()
    if args.input_file:
        with open(args.input_file, "r") as input_file:
            thread = input_file.read()
    else:
        thread = sys.stdin.read()

    if args.max_chars < 1:
        print("Maximum number of chars must be greater than zero. Exiting.",
                file=sys.stderr)
        sys.exit(1)

    sweet = Sweet(args.max_chars)
    tweets = sweet.compose_tweets(thread, sweet.split_v2)

    if args.output_file:
        with open(args.output_file, "w") as output_file:
            output_file.write(tweets)
    else:
        print(tweets)

if __name__=="__main__":
    main()
