from sklearn.linear_model import Lasso
from winequality import get_preprocessed_dataset, get_XY

def run_model(filename):

    train, validate, test = get_preprocessed_dataset(filename)

    train_X, train_Y = get_XY(train)
    validate_X, validate_Y = get_XY(validate)

    clf = Lasso(alpha = 0.1)
    clf.fit(train_X, train_Y)

    return clf.score(validate_X, validate_Y)

if __name__ == "__main__":
    print run_model('winequality-red.csv')
    print run_model('winequality-white.csv')
