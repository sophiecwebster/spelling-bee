# read in file of words (can be in a column separated by linebreaks)
samplefile = open("./sample-words.txt", "r+")

# at this point, they're in a string
L = samplefile.read()

# remove linebreaks and replace with a classic comma and space
M = L.replace("\n", ", ")
# make them into a list, delineated by comma and space
words = list(M.split(", "))

# --------- here's another way to make a comma separated list --- #
# --------- but it's not as effective! --- #

# def convert(lst):
#     return(lst[0].split())
#
# lst = ["Golly Noggin Logo"]
# print(convert(lst))
# print(type(lst))


# create list of words to check
# words = ["golly", "noggin", "logo", "annoying"]
# ^ engage if you don't have a txt file in mind
# need to check length of word
# need to check which letters the words contain

# going to need to insert letters and melt down into a set
char_list = set('conifed')
chars=', '.join(char_list)
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
key_letter = "i"
upper_key = key_letter.upper()
lower_key = key_letter.lower()
lengths = []
sum=0

# remove the 7 pertinent letters from the alphabet
# we'll use this to check if a submitted word is valid
slimmed_alpha = [ele for ele in alpha if all(ch not in ele for ch in chars)]

for i in range(0, len(words)):
    for b in range(0, len(slimmed_alpha)):
        # this weeds out words containing out-of-bounds letters
        if slimmed_alpha[b] in words[i]:
            # how can i get it to delete the word instead?
            # create copy of list?
            words[i] = 'foo'
        else:
            words[i] = words[i]
print(words)

for i in range(0,len(words)):
    # this logic weeds out words not containing the keystone letter
    if lower_key in words[i]:
        words[i] = words[i]
    elif upper_key in words[i]:
        words[i] = words[i]
    else:
        # using 'foo' will ensure it doesn't
        print(words[i], "doesn't contain the letter", upper_key, "ding dong!")
        words[i] = 'foo'
    # now, this adds the length of words to an empty list called 'lengths'
    lengths.append(len(words[i]))
    # if all 7 letters are accounted for, 7 pt bonus
    if all((c in set(words[i])) for c in char_list):
        lengths[i] = lengths[i]+7
    # tally the score from the length
    lengths[i] = lengths[i]-3
    sum += lengths[i]

print("You scored", sum, "points!")

# https://stackoverflow.com/questions/2528047/how-to-make-a-form-input-field-large
# https://www.digitalocean.com/community/tutorials/processing-incoming-request-data-in-flask#using-form-data
