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
char_list = set('golnayi')
lengths = []
sum=0

for i in range(0,len(words)):
    lengths.append(len(words[i]))
    if all((c in set(words[i])) for c in char_list):
        lengths[i] = lengths[i]+7
    lengths[i] = lengths[i]-3
    sum += lengths[i]
print("You scored", sum, "points!")

# https://stackoverflow.com/questions/2528047/how-to-make-a-form-input-field-large
# https://www.digitalocean.com/community/tutorials/processing-incoming-request-data-in-flask#using-form-data
