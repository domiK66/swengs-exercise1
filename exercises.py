# Part 1: Strings, lists and control structures


def count_characters(str_under_test):
    """Returns the length of str_under_test"""
    return len(str_under_test)
    


def first_three_letters(str_under_test):
    """Returns the first three letters of str_under_test"""
    return str_under_test[0:3]
    


def last_three_letters(str_under_test):
    """Returns the last three letters of str_under_test"""
    return str_under_test[-3:]
    


def split_words(str_under_test):
    """Splits str_under_test into a list of words"""
    return str_under_test.split()
    


def replace(str_under_test, search_str, replace_by):
    """Replace all occurrences of search_str by string given in replace_by"""
    return str_under_test.replace(search_str, replace_by)
    


def normalize(str_under_test, mode):
    """Performs string normalization

    Keyword arguments:
    mode -- can either be 1,2 or 3. 1 returns the string lower case, 2 upper case and 3 capitalized. Any
    other value raises an ValueError with message "Invalid mode"
    """
    if mode == 1:
        return str_under_test.lower()
    elif mode == 2:
        return str_under_test.upper()
    elif mode == 3:
        return str_under_test.capitalize()
    else:
        raise ValueError("Invalid mode")
    


def find_title(titles, search_str):
    """Searches a search_str in "titles"

    If titles=["Blade Runner","Star wars","Star trek"] and
    search_str="star" the function should return
    ["Star wars","Star trek"]. The search is case-insensitive.
    If no match is found, an empty list is returned.
    """
    result = []
    for i in titles:
        if search_str.lower() in i.lower():
            result.append(i)
    return result
    

# Part 2 - Working with lists and dictionaries


def calculate_mean(numbers):
    """This function returns the mean value of all numbers given in the list.

    Thus, calculate_mean([8,4,10,2]) returns 6.0.
    The function returns None, if the list is empty.

    - If time: Try an alternative solution: 
    install the numpy package via pip, import it and apply the numpy.mean 
    function to calculate the mean value.
    """
    if not numbers: 
        return None
    return sum(numbers) / len(numbers)
    


def min_mean_max(numbers):
    """This function returns a tuple, the smallest element in numbers, the mean value of all
    numbers and the highest number in the list.

    Thus, calculate_mean([8,4,10,2]) should return (2,6.0,10)
    The function returns None, if the list is empty.
    """
    if not numbers: 
        return None
    return (min(numbers), calculate_mean(numbers), max(numbers))
    


def mean_temperature(weather_data):
    """Returns the mean temperature for the weather_data provided.

    This functions takes in a list of tuples providing weather data for a given city for a
    year following this format:
    [ (1, 21) , (2,23) , ... (12,8) ] - whereas the first
    variable indicates the month as integer and the second variable the actual temperature
    The functions returns the mean temperature for this city. 
    Using Python's round function (built-in), the function rounds the result to 1 digit.
    If the input list is empty, None is returned.
    """
    if not weather_data: 
        return None
    years = []
    for i in weather_data:
        years.append(i[1])
    return round(calculate_mean(years), 1)
    


from collections import Counter
def word_count(document):
    """Returns a dictionary with a word count of all words given in document
    (Hint: split the document into word through splitting it by whitespace)
    Thus, if "Los Angeles is bigger than Berlin but Berlin is older than Los Angeles ." is
    provided in string document, the function returns the dictionary:
    {"Los":2, "Angeles":2, "is":2, "bigger:"1","than":2,"Berlin":2,"but":1,"older":1,".":1}
    """
    dict = {}
    for word in document.split():
        if word not in dict:
            dict[word] = 0 
        dict[word] += 1
    return dict
    


def common_words(document, threshold=2):
    """Returns the most common words in document and applies a threshold.

    Thus, if "Los Angeles is bigger than Berlin but Berlin is older than Los Angeles ." is
    provided, the function returns a list of words with occurrences equal or greater as
    the number given in threshold. If threshold is 2, the function would return
    ["Los","Angeles","is","than","Berlin"]
    """
    return list((key) for key, value in word_count(document).items() if value >= threshold)