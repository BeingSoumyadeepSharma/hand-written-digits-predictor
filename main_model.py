import numpy as np
import tensorflow as tf
#from sklearn.model_selection import train_test_split

def getData():
    mnist = tf.keras.datasets.mnist
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    x_train = tf.keras.utils.normalize(x_train, axis = 1)
    x_test = tf.keras.utils.normalize(x_test, axis = 1)

    return ((x_train, y_train), (x_test, y_test))

def createModel():
    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Flatten())
    model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
    model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
    model.add(tf.keras.layers.Dense(10, activation=tf.nn.softmax))

    model.compile(optimizer = 'adam', loss = 'sparse_categorical_crossentropy', metrics = ['accuracy'])

    return model

def buildModel(model, x, y, epoch = 5):
    results = model.fit(x, y, epochs = epoch, verbose = 1)
    return (model, results)

if __name__ == "__main__":
    (x_train, y_train), (x_test, y_test) = getData()
    #x_tr, x_val, y_tr, y_val = train_test_split(x_train, y_train, test_size = 0.20, random_state = 2)
    model = createModel()
    (model, results) = buildModel(model, x_train, y_train, epoch = 10)
    print(model.summary())
    print(model.evaluate(x_test, y_test, verbose = 2))
    model.save(".\saved_models\hand_written_number")