from sklearn import linear_model
from winequality import get_preprocessed_dataset, get_XY

def run_model(filename):

    train, validate, test = get_preprocessed_dataset(filename)

    train_X, train_Y = get_XY(train)
    validate_X, validate_Y = get_XY(validate)

    regr = linear_model.LinearRegression()
    regr.fit(train_X, train_Y)

    return regr.score(validate_X, validate_Y)

if __name__ == "__main__":
    total_score = 0
    for i in range(50):
        total_score = total_score + run_model('winequality-red.csv')
    print total_score/50
