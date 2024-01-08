# Day 21: 30 days of python programming

'''Python has the module called statistics and we can use this module to do all the statistical calculations. 
However, to learn how to make function and reuse function let us try to develop a program, which calculates the measure of central tendency of a sample (mean, median, mode) and measure of variability (range, variance, standard deviation). 
In addition to those measures, find the min, max, count, percentile, and frequency distribution of the sample. You can create a class called Statistics and create all the functions that do statistical calculations as methods for the Statistics class. Check the output below'''

'''ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

print('Count:', data.count()) # 25
print('Sum: ', data.sum()) # 744
print('Min: ', data.min()) # 24
print('Max: ', data.max()) # 38
print('Range: ', data.range() # 14
print('Mean: ', data.mean()) # 30
print('Median: ', data.median()) # 29
print('Mode: ', data.mode()) # {'mode': 26, 'count': 5}
print('Standard Deviation: ', data.std()) # 4.2
print('Variance: ', data.var()) # 17.5
print('Frequency Distribution: ', data.freq_dist()) # [(20.0, 26), (16.0, 27), (12.0, 32), (8.0, 37), (8.0, 34), (8.0, 33), (8.0, 31), (8.0, 24), (4.0, 38), (4.0, 29), (4.0, 25)]'''

# you output should look like this
'''print(data.describe())
Count: 25
Sum:  744
Min:  24
Max:  38
Range:  14
Mean:  30
Median:  29
Mode:  (26, 5)
Variance:  17.5
Standard Deviation:  4.2
Frequency Distribution: [(20.0, 26), (16.0, 27), (12.0, 32), (8.0, 37), (8.0, 34), (8.0, 33), (8.0, 31), (8.0, 24), (4.0, 38), (4.0, 29), (4.0, 25)]'''

import statistics as stats

class Statistics:
    def __init__(self, data):
        self.data = data

    def count(self):
        return len(self.data)

    def sum(self):
        return sum(self.data)

    def min(self):
        return min(self.data)

    def max(self):
        return max(self.data)

    def range(self):
        return self.max() - self.min()

    def mean(self):
        return stats.mean(self.data)

    def median(self):
        return stats.median(self.data)

    def mode(self):
        mode = stats.mode(self.data)
        count = self.data.count(mode)
        return (mode, count)

    def var(self):
        return stats.variance(self.data)

    def std(self):
        return stats.stdev(self.data)

    def freq_dist(self):
        frequency_dict = {}
        for i in self.data:
            if i in frequency_dict:
                frequency_dict[i] += 1
            else:
                frequency_dict[i] = 1
        
        frequency_list = [(value, key) for key, value in frequency_dict.items()]
        frequency_list.sort(reverse=True)
        return frequency_list

    def describe(self):
        print('Count:', self.count())
        print('Sum: ', self.sum())
        print('Min: ', self.min())
        print('Max: ', self.max())
        print('Range: ', self.range())
        print('Mean: ', self.mean())
        print('Median: ', self.median())
        print('Mode: ', self.mode())
        print('Variance: ', self.var())
        print('Standard Deviation: ', self.std())
        print('Frequency Distribution: ', self.freq_dist())
# implementation
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
data = Statistics(ages)
data.describe()



'''
Create a class called PersonAccount. 
It has firstname, lastname, incomes, expenses properties 
and it has total_income, total_expense, account_info, add_income, add_expense and account_balance methods. 
Incomes is a set of incomes and its description. The same goes for expenses.
'''



class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = []
        self.expenses = []

    def add_income(self, amount, description):
        self.incomes.append((amount, description))

    def add_expense(self, amount, description):
        self.expenses.append((amount, description))

    def total_income(self):
        total = 0
        for income in self.incomes:
            total += income[0]
        return total

    def total_expense(self):
        total = 0
        for expense in self.expenses:
            total += expense[0]
        return total

    def account_balance(self):
        return self.total_income() - self.total_expense()

    def account_info(self):
        print("First name: ", self.firstname)
        print("Last name: ", self.lastname)
        print("Incomes: ", self.incomes)
        print("Expenses: ", self.expenses)
        print("Total Income: ", self.total_income())
        print("Total Expense: ", self.total_expense())
        print("Account Balance: ", self.account_balance())

account = PersonAccount("Lukman", "Aliyu")

account.add_income(300_000_000, "salary")
account.add_income(50_000, "bonus")

account.add_expense(2_000, "books")
account.add_expense(10_000, "fuel")

account.account_info()

