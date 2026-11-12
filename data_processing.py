import csv, os


class CityCollection:

    def __init__(self, cities):
        self.cities = list(cities)

    @classmethod
    def from_csv(cls, filename):
        location = os.path.dirname(os.path.realpath(__file__))
        with open(os.path.join(location, filename)) as f:
            return cls(dict(r) for r in csv.DictReader(f))

    def __iter__(self):
        return iter(self.cities)

    def __len__(self):
        return len(self.cities)

    def filter(self, condition):
        return CityCollection(c for c in self.cities if condition(c))

    def where_country(self, country):
        return self.filter(lambda c: c["country"] == country)

    def aggregate(self, key, aggregation_function):
        values = [float(c[key]) for c in self.cities]
        return aggregation_function(values)

    def average(self, key):
        return self.aggregate(key, lambda v: sum(v) / len(v))

    def unique(self, key):
        return {c[key] for c in self.cities}

    def names(self):
        return [c["city"] for c in self.cities]


def main():
    cities = CityCollection.from_csv("Cities.csv")

    print("First 5 cities:")
    for city in list(cities)[:5]:
        print(city)
    print()

    print("The average temperature of all the cities:")
    print(cities.average("temperature"))
    print()

    print("All cities in Germany")
    for name in cities.where_country("Germany").names():
        print(name)
    print()

    print("Cities in Spain with a temperature above 12°C")
    spain_warm = cities.where_country("Spain").filter(lambda c: float(c["temperature"]) > 12)
    for name in spain_warm.names():
        print(name)
    print()

    print("Count the number of unique countries")
    countries = cities.unique("country")
    print(countries)
    print(len(countries))
    print()

    print("Average temperature for all the cities in Germany")
    print(f"{cities.where_country('Germany').average('temperature'):.2f}")
    print()

    print("Max temperature for all the cities in Italy")
    print(cities.where_country("Italy").aggregate("temperature", max))


if __name__ == "__main__":
    main()