def count_words(text: str) -> dict[str, int]:
       
    """
    Return a dictionary counting how often each word appears.

    Example:

    "hello world hello"

    ->
    {
        "hello": 2,
        "world": 1
    }
    """

    wordcount = {} 

    for word in text.split(): 
        if word in wordcount: 
            wordcount[word] += 1
        else: 
            wordcount[word] = 1
    
    return wordcount




def remove_duplicates(numbers: list[int]) -> list[int]:
    """
    Remove duplicates while preserving order.

    Example:

    [3,1,2,3,2,4]

    →

    [3,1,2,4]
    """

    list_without_duplicates = []

    for number in numbers: 
        if number not in list_without_duplicates: 
            list_without_duplicates.append(number)


    return list_without_duplicates


### better option performance wise to use a set to track seen numbers

def remove_duplicates(numbers: list[int]) -> list[int]:
    """
    Remove duplicates while preserving order.

    Example:

    [3,1,2,3,2,4]

    →

    [3,1,2,4]
    """

    seen = set()
    list_without_duplicates = []

    for number in numbers:
        if number not in seen:
            seen.add(number)
            list_without_duplicates.append(number)

    return list_without_duplicates



def group_students(records):
    """
    Input:

    [
        ("Anna","AI"),
        ("Tom","AI"),
        ("Lisa","Robotics"),
        ("Ben","AI")
    ]

    Output:

    {
        "AI": ["Anna","Tom","Ben"],
        "Robotics": ["Lisa"]
    }
    """

    grouped_students = {}

    for student, course in records: 
        if course not in grouped_students:
            grouped_students[course] = []
            if student not in grouped_students[course]:
                grouped_students[course].append(student)
        else: 
            grouped_students[course].append(student)
    
    return grouped_students 

## leaner version: 

def group_students(records):

    grouped_students = {}

    for student, course in records: 
        if course not in grouped_students: 
            grouped_students[course] = []

        grouped_students[course].append(student)
        
    return grouped_students 