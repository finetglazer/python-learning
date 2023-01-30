# Define function
def printf(*args):
    str=""
    count=0
    for word in args:
        str += word
        count+=1
    print(str)
    return count

# Call function
one_word = printf("learn")
print(one_word)

many_words = printf("didnt", "write", "the", 'song', 'dont', 'wanna', 'hold', 'back')
print(many_words)