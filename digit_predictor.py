import tensorflow as tf
import numpy as np

class DigitPredictor():

    def __init__(self):
        self.model = tf.keras.models.load_model("E:\Projects\hand-written-digits\saved_models\hand_written_number")
    
    def digitPredict(self, finalArray):
        prediction = self.model.predict(finalArray)
        final_prediction = np.argmax(prediction, axis = 1)
        return int(final_prediction)