#!/usr/bin/env python3

import argparse
import queue
import sys
import threading
import urllib.error
import urllib.parse
import urllib.request

sys.exit("Use the -h parameter to learn about using the program.") if len(sys.argv[1:]) == 0 else True

description = "DirForcer is a brute-forcing tool designed to brute force an URL " \
              "and get a list of accessible directories from it."
parser = argparse.ArgumentParser(description=description)
parser.add_argument("-t", "--target", type=str, help="Target URL")
parser.add_argument("-w", "--wordlist", type=str, help="Path to the wordlist.")
parser.add_argument("-e", "--extension", help="An extension list to use while brute forcing. OPTIONAL "
                                              "default: [ .php , .bak .orig, .inc ]",
                    action="store_true")
args = parser.parse_args()

thread_count = 25
target_url = args.target
wordlist = args.wordlist
extensions = [".php", ".bak", ".orig", ".inc"]
if args.extension:
    extensions = args.extension

resume = None
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"


# Open the wordlist and read each word from it. Put the words in the wordlist into a queue (words_queue)
def build_wordlist(wordlist_file):
    try:
        file = open(wordlist_file, "r")
    except OSError:
        sys.exit("Wordlist not found in the location. Are you in the same directory as it?")

    raw_words = file.readlines()
    file.close()

    found_resume = False
    words_queue = queue.Queue()

    for word in raw_words:
        word = word.rstrip()

        if resume is not None:

            if found_resume:
                words_queue.put(word)
            else:
                if word == resume:
                    found_resume = True
                    print("Resuming wordlist from: %s" % resume)

        else:
            words_queue.put(word)

    return words_queue


# Brute force the URL using the directory list from build_wordlist and add extensions(optional)
def bruter(words, extension_file=None):
    while not words.empty():
        attempt = words.get()
        attempt_list = []

        # check if there is a file extension. If there is a file extension, we're brute forcing a file.
        # If there isn't an extension, we're brute forcing a path.
        if "." not in attempt:
            attempt_list.append("/%s/" % attempt)
        else:
            attempt_list.append("/%s" % attempt)

        # Is there an extension list?
        if extension_file:
            for extension in extension_file:
                attempt_list.append("/%s%s" % (attempt, extension))

        # Actual brute force part
        for brute in attempt_list:
            url = "%s%s" % (target_url, urllib.parse.quote(brute))

            try:
                headers = {"User-Agent": user_agent}
                r = urllib.request.Request(url, headers=headers)

                response = urllib.request.urlopen(r)

                if len(response.read()):
                    print("[%d] => %s" % (response.code, url))

            except urllib.error.URLError as e:
                if hasattr(e, "code") and e.code != 404:
                    print("!!! %d => %s" % (e.code, url))

                pass


word_queue = build_wordlist(wordlist)

for i in range(thread_count):
    t = threading.Thread(target=bruter, args=(word_queue, extensions,))
    t.start()
