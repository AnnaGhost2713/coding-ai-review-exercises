## Defaultdict 

#### Code before: 
def group_students(records): 
    groups = {}

    for student, course in records:
        if course not in groups:
            groups[course] = []

        groups[course].append(student)
    return groups

#### With Defaultdict: 
from collections import defaultdict
#### What does it do? 
#### If the key in the dict. doesnt exist yet, it will create a new key with the default value (in this case, an empty list) instead of raising a KeyError.
def group_students(records):
    groups = defaultdict(list)

    for student, course in records:
        groups[course].append(student)
    return groups


#### Code before: 
def count_words(text):
    word_counts = {}

    for word in text.split():
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    return word_counts

#### With Defaultdict:
from collections import defaultdict
def count_words(text):
    word_counts = defaultdict(int)

    for word in text.split():
        word_counts[word] += 1

    return word_counts


#### Version 1: 
def count_words_normal(text: str) -> dict[str, int]: 
    word_counts = {}

    for word in text.split():  
        if word in word_counts: 
            word_counts[word] += 1
        else: 
            word_counts[word] = 1 
    
    return word_counts


#### Version 2: 
from collections import defaultdict

def count_words_defaultdict(text: str) -> dict[str, int]:
    word_counts = defaultdict(int)

    for word in text.split(): 
        word_counts[word] += 1
    
    return dict(word_counts)





