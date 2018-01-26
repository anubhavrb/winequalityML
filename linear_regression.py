from sklearn import linear_model
from sklearn.metrics import r2_score
from winequality import get_preprocessed_dataset, get_XY

def run_model():

    train, validate, test = get_preprocessed_dataset('winequality-white.csv')

    train_X, train_Y = get_XY(train)
    validate_X, validate_Y = get_XY(validate)

    regr = linear_model.LinearRegression()
    regr.fit(train_X, train_Y)

    pred_Y = regr.predict(validate_X)

    return r2_score(validate_Y, pred_Y)

if __name__ == "__main__":
    print run_model()
