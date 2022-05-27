# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}
import string
def read_file_content(filename):
    # [assignment] Add your code here 
    with open(filename, 'r') as f:
        content = f.read()
    f.close()
    return content
    

def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    words = text.split()
    counts = {}
    for word in words:

        word = word.translate(str.maketrans('','', string.punctuation))
        word = word.lower()


        if word in counts:
            counts[word] += 1
            counts[word] = counts[word] + 1
        else:
            counts[word] = 1

        return counts


print(count_words())