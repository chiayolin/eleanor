# eleanor: simple language processor

# init
verbs = [ "is", "are" ]
possesive_determiner = [ "your", "my", "his", "her", "their", "they"]
memory = dict()

# iterate through an array and return the index of
# which the token occurs in the array:
def scan(array, tokens):
    for i in range(0, len(array)):
        if array[i] in tokens:
            return i
    return None

# extreme simple sentence processor prototype
def essp():
    raw_str = input().lower().split(" ")

    index_verb = scan(raw_str, verbs)
    index_pd = scan(raw_str, possesive_determiner)
    # learning or retrieving information base on the index values 
    # of the verb and the the possesive determiner (e.g. verb before 
    # a PD would become a question):
    if index_verb != None and index_pd != None and index_verb > index_pd:
        # learnin: add an element into the main dictionary, using the 
        # "possesive determiner" as the key value to the sub-dictionary 
        # created using whatever "subject" as a key value. finally, link 
        # the value of the object to the key value of the sub-dictionary
        # (index_pd = position of the possesive determiner,
        # raw_str[index_pd + 1] = subject, raw_str[index_verb + 1] = object):
        if not (raw_str[index_pd] in memory.keys()):
            memory[raw_str[index_pd]] = dict() # create a sub-dict if the key doesn't exist
        memory[raw_str[index_pd]][raw_str[index_pd + 1]] = raw_str[index_verb + 1:]
        # print(raw_str[index_pd], raw_str[index_pd + 1], raw_str[index_verb], *raw_str[index_verb + 1:]) 
    
    elif raw_str[0] == "\memory":
            print(memory)
    
    else:
        if raw_str[index_pd + 2:] == memory[raw_str[index_pd]][raw_str[index_pd + 1]]:
            print("yes,", raw_str[index_pd], raw_str[index_pd + 1], \
                raw_str[index_verb], *raw_str[index_pd + 2:])
        else:
            print("no,", raw_str[index_pd], raw_str[index_pd + 1], raw_str[index_verb], \
                "not", *raw_str[index_pd + 2:], "because", raw_str[index_pd], \
                    raw_str[index_pd + 1], raw_str[index_verb], \
                        *memory[raw_str[index_pd]][raw_str[index_pd + 1]])
# start 
while 1:
    essp()
