from sklearn import linear_model
from winequality import get_preprocessed_dataset, get_XY

def run_model(filename):

    total_score = 0
    for i in range(50):
        train, validate, test = get_preprocessed_dataset(filename)

        train_X, train_Y = get_XY(train)
        validate_X, validate_Y = get_XY(validate)

        regr = linear_model.LinearRegression()
        regr.fit(train_X, train_Y)

        total_score = total_score + regr.score(validate_X, validate_Y)

    return total_score/50

if __name__ == "__main__":
    print run_model('winequality-white.csv')
