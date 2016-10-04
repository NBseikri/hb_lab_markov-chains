from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    # """

    source_material = open(file_path).read()
    return source_material

def make_chains(text_string):

    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """
    chains = {} 

    words = text_string.split()
    for i in range(len(words) - 1):
        #word_after_pair = words[i + 2]
        #value
        word_pair = (words[i], words[i + 1])
        #key
        if word_pair not in chains:
             chains[word_pair] = word_after_pair

    #print word_pair

        #tuple is in dict
        #tuple is not in dict, inlude it as a new addition to the list
    
    # input_text = {}
    # for text in         
    
    # chains = make_chains(input_text)


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = ""

    # your code goes here

    return text


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file('green-eggs.txt')
print input_text

# # Get a Markov chain
chains = make_chains(input_text)
print chains

# # Produce random text
# random_text = make_text(chains)

# #print random_text
# print make_chains(input_text)