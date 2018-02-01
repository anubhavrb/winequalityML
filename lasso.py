from sklearn.linear_model import Lasso
from winequality import get_preprocessed_dataset, get_XY
from sklearn.model_selection import GridSearchCV

def run_model(filename):

    train, validate, test = get_preprocessed_dataset(filename)

    parameters = {'alpha': [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1.0]}

    train_X, train_Y = get_XY(train)
    validate_X, validate_Y = get_XY(validate)

    lasso = Lasso(max_iter = 10000)
    clf = GridSearchCV(lasso, parameters)
    clf.fit(train_X, train_Y)

    return clf.score(validate_X, validate_Y)

if __name__ == "__main__":
    total_score = 0
    for i in range(50):
        total_score = total_score + run_model('winequality-red.csv')
    print total_score/50
