from sklearn.linear_model import SGDRegressor
from winequality import get_preprocessed_dataset, get_XY
from sklearn.model_selection import GridSearchCV

def run_model(filename):

    train, validate, test = get_preprocessed_dataset(filename)

    parameters = {'eta0': [0.001, 0.002, 0.005, 0.01], 'alpha': [0.00001, 0.00002, 0.00005, 0.0001]}

    train_X, train_Y = get_XY(train)
    validate_X, validate_Y = get_XY(validate)

    #clf = SGDRegressor()

    sgd = SGDRegressor()
    clf = GridSearchCV(sgd, parameters)
    clf.fit(train_X, train_Y)

    #return clf.score(validate_X, validate_Y)
    return clf.score(validate_X, validate_Y)

if __name__ == "__main__":
    total_score = 0
    for i in range(50):
        total_score = total_score + run_model('winequality-white.csv')
    print total_score/50
