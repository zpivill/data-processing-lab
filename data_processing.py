import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

def filter_items(condition, dict_list):
    """
    Return a new list containing only the dictionaries that satisfy
    the given condition function.

    Args:
        condition: A function that takes a dictionary and returns True or False.
        dict_list: A list of dictionaries.

    Returns:
        A list of dictionaries for which condition(item) is True.

    Examples:
        >>> students = [
        ...     {"name": "Alice", "score": 90},
        ...     {"name": "Bob", "score": 70},
        ...     {"name": "Charlie", "score": 85}
        ... ]
        >>> filter_items(lambda s: s["score"] >= 85, students)
        [{'name': 'Alice', 'score': 90}, {'name': 'Charlie', 'score': 85}]

        >>> filter_items(lambda s: s["name"].startswith("A"), students)
        [{'name': 'Alice', 'score': 90}]

        >>> filter_items(lambda s: s["score"] > 100, students)
        []
    """
    # YOUR CODE HERE
    li = []
    for item in dict_list:
        if condition(item):
            li.append(item)
    return li


def aggregate(aggregation_key, aggregation_function, dict_list):
    """
    Aggregate values associated with aggregation_key using the
    provided aggregation function.

    Args:
        aggregation_key: The dictionary key whose values should be aggregated.
        aggregation_function: A function such as sum, max, min, etc.
        dict_list: A list of dictionaries.

    Returns:
        The aggregated result.

    Examples:
        >>> students = [
        ...     {"name": "Alice", "score": 90},
        ...     {"name": "Bob", "score": 70},
        ...     {"name": "Charlie", "score": 85}
        ... ]

        >>> aggregate("score", sum, students)
        245

        >>> aggregate("score", max, students)
        90

        >>> aggregate("score", min, students)
        70

        >>> aggregate(
        ...     "score",
        ...     lambda scores: sum(scores) / len(scores),
        ...     students
        ... )
        81.66666666666667
    """
    # YOUR CODE HERE
    val = [float(item[aggregation_key]) for item in dict_list]
    return aggregation_function(val)
# Print first 5 cities only
for city in cities[:5]:
    print(city)

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
print(aggregate('temperature', lambda temperature: sum(temperature)/ len(temperature),cities))
print()


# Print all cities in Germany

'''
Your code here

'''
print("All cities in Germany")
for names in filter_items(lambda item: item["country"] == 'Germany', cities):
    print(names["city"])
print()
# Print all cities in Spain with a temperature above 12°C

'''
Your code here

'''
print("cities in Spain with a temperature above 12°C")
li = [x for x in filter_items(lambda item: item["country"] == 'Spain', cities)]
for names in filter_items(lambda t: float(t["temperature"]) >12, li):
    print(names["city"])
print()
# Count the number of unique countries

'''
Your code here

'''
print("Count the number of unique countries")
unique_countries = {city["country"] for city in cities}
print(unique_countries)
print(len(unique_countries))
print()
# Print the average temperature for all the cities in Germany

'''
Your code here

'''
print("Print the average temperature for all the cities in Germany")

li = filter_items(lambda item: item["country"] == 'Germany', cities)
print(aggregate('temperature', lambda temperature: sum(temperature)/ len(temperature),li))


print()
# Print the max temperature for all the cities in Italy

'''
Your code here

'''
print("Print the max temperature for all the cities in Italy")
li = filter_items(lambda item: item["country"] == 'Italy', cities)
print(aggregate('temperature', lambda temperature: max(temperature),li))
