import csv

"""
This file will take in a boat index and return a list of the data for that boat
the indices of the data are as follows:
0: Boat Number
1: Boat Area WP
2: Boat Area WS
3: Boat Curvature
4: Boat Ixx
5: Boat Iyy
6: Boat LCB
7: Boat LCF
8: Boat VCB
9: Boat Volume
10: Boat WL_Length
11: Boat z
12: list of boat input vectors, in order
13: filename of profile image
"""
class readData:
    def __init__(self, boatInt): 
        """input: boatInt, which is the index of the boat in the csv files"""
        self.boatInt = boatInt
        self.filenames = ['Area_WP.csv', 'Area_WS.csv', 'GaussianCurvature.csv', 'Ixx.csv', 'Iyy.csv', 'LCB.csv', 
                          'LCF.csv', 'VCB.csv',  'Volume.csv', 'WL_Length.csv', 'z.csv']
        self.output = [boatInt]

    def csv_to_lists(self, csv_file):
        """input: csv_file, which is the name of the csv file to be read
           output: a list of the rows in the csv file"""
        rows = []
        with open(csv_file, 'r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip the header row
            for row in csv_reader:
                rows.append(row)
        return rows
    
    def read(self): 
        """returns a list of the data for the boat"""
        for filename in self.filenames:
            path = 'GeometricMeasures/' + filename
            self.output.append(self.csv_to_lists(path)[self.boatInt][0])
        self.output.append(self.csv_to_lists('Input_Vectors.csv')[self.boatInt])
        self.output.append('Profile/Profile_Hull_'+ str(self.boatInt) +'.png')
        return self.output
        
if __name__ == "__main__": 
    """prompts user to enter boat index, outputs the data for that boat"""
    boatInt = input("Enter boat index: ")
    data = readData(int(boatInt))
    print(data.read())
