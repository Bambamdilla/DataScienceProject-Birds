import os
import tensorflow as tf
import numpy as np
from consts import INPUT_RESOLUTION, BATCH_SIZE, DATA_PATH, BIRD_PATH
#
# trained_model = tf.keras.saving.load_model(DATA_PATH, custom_objects=None, compile=True, safe_mode=True)
#
# img_path = os.path.join(BIRD_PATH, "img\\bird.png")  # TO DO: zmiana nazwy uploadowanego pliku do stałej zmiennej
# image = tf.keras.preprocessing.image.load_img(img_path, target_size=INPUT_RESOLUTION[:2])
# input_arr = tf.keras.preprocessing.image.img_to_array(image)
# input_arr = np.array([input_arr])  # Convert single image to a batch.
# input_arr = input_arr.astype('float32') / 255.  # standaryzacja do 0-1
#
# prediction = trained_model.predict(input_arr)  # prawdopodobieństwo wystąpienia każdej z klas
#
# best_class = np.argmax(prediction, axis=1)  # printuje najbardziej prawdopodobną klasę
# print(best_class)
#
# bird_list = os.listdir(os.path.join(DATA_PATH, "train"))
# bird_list = np.array(bird_list)
# # bird_name = bird_list[best_class-1]  # -1, bo liczy od 1, a indeks zaczyna się od 0
# # print(bird_name)
#
# print(f"Predykowany ptak to {bird_list[best_class]}")
