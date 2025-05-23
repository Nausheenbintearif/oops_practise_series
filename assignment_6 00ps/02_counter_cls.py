class Counter:
    count = 0  # Class variable to count objects

    def __init__(self):
        Counter.count += 1  # Increment the count when an object is created

    @classmethod
    def show_count(cls):
        print(f"Total object created: {cls.count}")  # Print the total count of objects

# Object creation
c1 = Counter()
c2 = Counter()
Counter.show_count()  # Call the class method to display the count
