from sklearn.linear_model import SGDClassifier
from sklearn.metrics import r2_score
from winequality import get_preprocessed_dataset, get_XY

def run_model():

    train, validate, test = get_preprocessed_dataset('winequality-red.csv')

    train_X, train_Y = get_XY(train)
    validate_X, validate_Y = get_XY(validate)

    clf = SGDClassifier(loss = "hinge", penalty = "l2", shuffle = False)
    clf.fit(train_X, train_Y)

    pred_Y = clf.predict(validate_X)

    return r2_score(validate_Y, pred_Y)

if __name__ == "__main__":
    print run_model()
