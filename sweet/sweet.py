class Sweet():

    separators = ['\n', '.', ' ']

    def __init__(self):
        pass

    def split(self, thread:str, max_chars:int=280) -> str:
        """
        Split a thread into postable tweets
        """
        if len(thread) <= max_chars:
            return thread
        tweets = [thread]
        for separator in self.separators:
            for i, tweet in enumerate(tweets):
                #print(separator, tweets)
                if len(tweet) > max_chars:
                    tweet_partition = tweet.partition(separator)
                    tweet_ = tweet_partition[0] + tweet_partition[1]
                    tweet_ = tweet_.strip()
                    if len(tweet_partition[0]) > 0:
                        tweets[i] = tweet_
                    if len(tweet_partition[2]) > 0:
                        tweets.insert(i+1, tweet_partition[2].strip())

            passing = True
            for tweet in tweets:
                if len(tweet) > max_chars:
                    passing = False
            if passing:
                break

        composition = ''
        for tweet in tweets:
            composition += str(len(tweet)) + "\n"
            composition += 'x'*int(len(tweet)/10) + '-'*int((max_chars-len(tweet))/10)
            composition += '\n'
            composition += tweet
            composition += '\n\n'

        return composition

