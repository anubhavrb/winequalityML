import numpy
import csv

def main():
    fix_acid = [] # fixed acidity
    vol_acid = [] # volatile acidity
    cit_acid = [] # citric acid
    res_sugar = [] # residual sugar
    chlorides = [] # chlorides
    free_so2 = [] # free sulfur dioxode
    total_so2 = [] # total sulfur dioxide
    density = [] # density
    pH = [] # pH
    sulphates = [] # sulphates
    alcohol = [] # alcohol
    quality = [] # quality

    read_file(fix_acid, vol_acid, cit_acid, res_sugar, chlorides, free_so2,
            total_so2, density, pH, sulphates, alcohol, quality)

    standardize_all(fix_acid, vol_acid, cit_acid, res_sugar, chlorides, free_so2,
            total_so2, density, pH, sulphates, alcohol)

    print pH

"""
Function to read in the features and target and store in the appropriate lists.
"""
def read_file(fix_acid, vol_acid, cit_acid, res_sugar, chlorides, free_so2,
        total_so2, density, pH, sulphates, alcohol, quality):

    with open("winequality-red.csv") as csvfile:
        next(csvfile) # skip header row
        readCSV = csv.reader(csvfile, delimiter = ';')

        for row in readCSV:
            fix_acid.append(float(row[0]))
            vol_acid.append(float(row[1]))
            cit_acid.append(float(row[2]))
            res_sugar.append(float(row[3]))
            chlorides.append(float(row[4]))
            free_so2.append(float(row[5]))
            total_so2.append(float(row[6]))
            density.append(float(row[7]))
            pH.append(float(row[8]))
            sulphates.append(float(row[9]))
            alcohol.append(float(row[10]))
            quality.append(float(row[11]))

"""
Function to separately standardize the lists of features using the
standardizations (z-score) method.
"""
def standardize_all(fix_acid, vol_acid, cit_acid, res_sugar, chlorides, free_so2,
        total_so2, density, pH, sulphates, alcohol):

    standardize(fix_acid)
    standardize(vol_acid)
    standardize(cit_acid)
    standardize(res_sugar)
    standardize(chlorides)
    standardize(free_so2)
    standardize(total_so2)
    standardize(density)
    standardize(pH)
    standardize(sulphates)
    standardize(alcohol)

"""
Function that standardizes the input list.
"""
def standardize(data):
    # Use numpy mean and std functions.
    a = numpy.array(data)
    m = numpy.mean(a)
    std_dev = numpy.std(a)
    for i in range(len(data)):
        data[i] = (data[i] - m)/std_dev

if __name__ == "__main__":
    main()
