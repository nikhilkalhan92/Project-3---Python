# importing libraries
import csv  # This library is used to write data into the csv file
import pandas as pd  # used to read the csv&show data for a particular column


class Sales_insight:

    def __init__(self):
        """
        Reads data from csv on given days
        """
        file_read = open('data.csv', 'r')
        self.data = file_read.readlines()[1:]
        self.sales = {}
        self.avg_sales = {}
        self.df = pd.read_csv('data.csv')

    def average(self):
        for line in self.data:
            temp_var = line.split(',')
            # Getting all data present in the iterated line
            val_sum = 0
            for x in temp_var[1:]:
                try:
                    if '\n' in x:
                        x = x[:-1]
                    val_sum += float(x)
                except:
                    break
            if len(temp_var[0]) > 3:
                self.avg_sales[temp_var[0]] = val_sum/len(temp_var[1:])
                # Adding data & dates into the dictionary

        print('average daily sales using all companies :\n')
        # Iterating the dictionary to print avr sales for dates
        for i in self.avg_sales:
            print(f"{i} : {self.avg_sales[i]:.2f}")

    def max_sales(self):
        for line in self.data:
            temp_var = line.split(',')
            val_sum = 0
            for x in temp_var[1:]:
                if len(temp_var[0]) > 3:
                    val_sum += float(x)
            if len(temp_var[0]) > 3:
                self.sales[temp_var[0]] = val_sum

        # bottom section we are using linear search algorithm to get max sales
        max_val = 0
        date = None
        for j in self.sales:
            if self.sales[j] > max_val:
                max_val = self.sales[j]
                date = j
        message = '{}{}{}{}{}'.format(
            'Maximum total sales for all companies',
            ' by day took place on ',
            date,
            ' worth ',
            f'{max_val:.2f}'
        )
        print(message)

    def read_data(self):
        while True:
            date = str(input('Enter Date : '))
            if date not in [
                '11-10-2021',
                '12-10-2021',
                '13-10-2021',
                '14-10-2021',
                '15-10-2021',
                '16-10-2021',
                '17-10-2021',
                '18-10-2021',
            ]:
                # tell user this is invalid input
                print(f'{date} is invalid input\n')
            else:
                break

        data_point = {}
        for line in self.data:
            temp_var = line.split(',')
            if temp_var[0] == date and len(temp_var[0]) > 3:
                data_point['Kenny Omega T Shirt'] = temp_var[1]
                data_point['Young bucks Tshirt'] = temp_var[2]
                data_point['Cody T shirt'] = temp_var[3]
                data_point['Hangman T shirt'] = temp_var[4]
                data_point['Adam Cole T shirt'] = temp_var[5]
                data_point['Chris Jericho T shirt'] = temp_var[6]

        for y in data_point:
            print(f'{y} : {data_point[y]}')

    def add_data(self):
        print('Please input Sales data for following ')
        date = str(input('Enter Date : '))
        kt = str(input('Kenny Omega T Shirt : '))
        yb = str(input('Young bucks Tshirt : '))
        ct = str(input('Cody T shirt : '))
        ht = str(input('Hangman T shirt : '))
        ac = str(input('Adam Cole T shirt : '))
        cj = str(input('Chris Jericho T shirt : '))
        file_open = open('data.csv', 'a', newline='')  # Open file append mode
        writer = csv.writer(file_open)   # Initialising the writer
        writer.writerow([date, kt, yb, ct, ht, ac, cj])  # Writing the row
        file_open.close()
        print('Data added succesfully!')

    def tshirt_search(self):
        tshirt = str(input('Tshirt name : '))
        try:
            print(self.df[tshirt])
        except:
            print('Please check if you have entered correct column name')


class_object = Sales_insight()
print('Welcome to Sale management App')
options_message = """

1) Calculate average sales
2) Get maximum sales
3) Read data for particular day
4) Add Data
5) Search Tshirt
6) Exit
"""
while True:
    print(options_message)
    inp = input('Your input : ')
    if inp not in ['1', '2', '3' , '4', '5', '6']:
        print('invalid input')
        continue
    inp = int(inp)
    print(inp)
    if inp == 1:
        print('I am here')
        class_object.average()
    elif inp == 2:
        class_object.max_sales()
    elif inp == 3:
        class_object.read_data()
    elif inp == 4:
        class_object.add_data()
    elif inp == 5:
        class_object.tshirt_search()
    elif inp == 6:
        break
    else:
        print('Error! Invalid input')
