import os
import cv2
import matplotlib.pyplot as plt
import tensorflow as tf
import pandas as pd

from consts import INPUT_RESOLUTION, BATCH_SIZE, DATA_PATH

# Wczytanie danych
pd.set_option('display.max_columns', None)
df = pd.read_csv(os.path.join(DATA_PATH, 'birds.csv'))
df_train = df.loc[df['data set'] == 'train']

df = pd.read_csv(os.path.join(DATA_PATH, 'birds.csv'))
df_test = df.loc[df['data set'] == 'test']

df = pd.read_csv(os.path.join(DATA_PATH, 'birds.csv'))
df_val = df.loc[df['data set'] == 'valid']

# Sprawdzenie poprawności wczytania obrazu
image = cv2.imread(os.path.join(DATA_PATH, "train\\ZEBRA DOVE\\6.jpg"))
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Konwersja kolorow BGR do RGB w celu prawidłowego wyświetlania
plt.imshow(image_rgb)
# plt.show()

train_ds = tf.keras.utils.image_dataset_from_directory(
  os.path.join(DATA_PATH, 'train'),
  validation_split=0.8,
  subset='training',
  seed=123,
  image_size=(INPUT_RESOLUTION[0], INPUT_RESOLUTION[1]),
  batch_size=BATCH_SIZE)

valid_ds = tf.keras.utils.image_dataset_from_directory(
  os.path.join(DATA_PATH, 'valid'),
  validation_split=None,
  subset=None,
  seed=123,
  image_size=(INPUT_RESOLUTION[0], INPUT_RESOLUTION[1]),
  batch_size=BATCH_SIZE)

test_ds = tf.keras.utils.image_dataset_from_directory(
  os.path.join(DATA_PATH, 'test'),
  validation_split=None,
  subset=None,
  seed=123,
  image_size=(INPUT_RESOLUTION[0], INPUT_RESOLUTION[1]),
  batch_size=BATCH_SIZE)
