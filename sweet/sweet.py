class Sweet():

    separators = ['\n\n', '.', ' ']

    def __init__(self, max_chars:int=280):
        self.max_chars = max_chars
        pass

    def compose_tweets(self, thread:str, split) -> str:
        """
        Create a string containing all single tweets and some meta information.
        Format:
        "
            Tweet x/y, 92/280 chars, xxxxxxxxx------------------
            {tweet}
            ...
        "

        PARAMETERS:
        thread  the thread that will be split into tweets
        split   the split algorithm. Example: Sweet().split_v1

        RETURNS:
        string  A string of the previously specified format
        """
        if len(thread) <= self.max_chars:
            return thread
        thread = self.__tidy__(thread)
        tweets = split(thread)
        composition = ''
        for i, tweet in enumerate(tweets):
            composition += 'Tweet {}/{}, '.format(i+1, len(tweets))
            composition += '{}/{} chars, '.format(len(tweet), self.max_chars)
            composition += 'x'*int(len(tweet)/10)
            composition += '-'*int((self.max_chars-len(tweet))/10)
            composition += '\n'
            composition += tweet
            composition += '\n\n'
        return composition

    def __tidy__(self, thread:str) -> str:
        thread_ = ''
        for line in thread.split('\n\n'):
            line = line.replace('\n', ' ')
            line = line.replace('  ', ' ')
            thread_ += line + '\n\n'
        return thread_


    def split_v1(self, thread:str) -> list:
        """
        Split a thread into postable tweets
        """
        if len(thread) <= self.max_chars:
            return thread
        tweets = [thread]
        for separator in self.separators:
            for i, tweet in enumerate(tweets):
                if len(tweet) > self.max_chars:
                    tweet_partition = tweet.partition(separator)
                    tweet_ = tweet_partition[0] + tweet_partition[1]
                    tweet_ = tweet_.strip()
                    if len(tweet_partition[0]) > 0:
                        tweets[i] = tweet_
                    if len(tweet_partition[2]) > 0:
                        tweets.insert(i+1, tweet_partition[2].strip())
            passing = True
            for tweet in tweets:
                if len(tweet) > self.max_chars:
                    passing = False
            if passing:
                break
        return tweets

    def split_v2(self, thread:str) -> list:
        """
        Split a thread into postable tweets
        """
        if len(thread) <= self.max_chars:
            return thread
        tweets = []
        sep_index = 0
        while len(thread) > 0:
            thread_index = self.max_chars
            while thread_index > 0 and len(thread) > self.max_chars:
                if thread[thread_index] == self.separators[sep_index]:
                    tweets += [thread[0:thread_index+1].strip()]
                    thread = thread[thread_index+1:]
                    thread_index = self.max_chars
                    sep_index = 0
                thread_index -= 1
            if sep_index + 1 >= len(self.separators):
                    tweets += [thread[0:self.max_chars+1].strip()]
                    thread = thread[self.max_chars+1:]
                    sep_index = 0
            else:
                sep_index = min(sep_index + 1, len(self.separators)-1)
        return tweets
