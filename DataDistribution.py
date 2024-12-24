import numpy as np
document = input("Enter the document: ")
try:
    with open(document, 'r') as file:
        data = []
        for line in file:
            numbers =[float(value) for value in  line.strip().split(',')]
            data.append(numbers)

        Weather = np.array(data)

        column_std = np.std(Weather, axis=0)
        column_mean = np.mean(Weather, axis=0)

        print("Column mean: ", column_mean)
        print("Column std: ", column_std)

        for weather in Weather:
            for i,indv in enumerate(weather):
                mean =column_mean[i]
                std = column_std[i]
                treshold = mean + (2*std)
                if(indv > treshold):
                    print(f"The day is {indv:.2f} and this is a Heatwave day because the treshhold for the day is {treshold:.2f}")
                else:
                    print(f"The day is {indv:.2f} and this is not a Heatwave because the treshhold for the day is {treshold:.2f}")
                #print(indv, mean, std)
            print("---------------")
except FileNotFoundError:
    print("File not found")
except ValueError as e:
    print(f"Error: {e}")
