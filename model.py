import tensorflow as tf
from consts import INPUT_RESOLUTION

# Model bazowy
base_model = tf.keras.applications.ConvNeXtTiny(
    model_name="convnext_tiny",
    include_top=False,
    include_preprocessing=True,
    weights="imagenet",
    input_shape=INPUT_RESOLUTION
)

base_model.trainable = False

early_stopping = tf.keras.callbacks.EarlyStopping(patience=3, monitor='val_binary_accuracy')

# Sieć neuronowa
inputs = tf.keras.Input(shape=INPUT_RESOLUTION)
x = tf.keras.layers.Rescaling(1. / 255)(inputs)
x = base_model(inputs)  # , training=False
x = tf.keras.layers.GlobalAveragePooling2D()(x)
x = tf.keras.layers.Flatten()(x)  # ?????
x = tf.keras.layers.Dense(525, activation='relu')(x)
x = tf.keras.layers.Dropout(0.5)(x)
outputs = tf.keras.layers.Dense(525, activation='softmax')(x)
model = tf.keras.Model(inputs=inputs, outputs=outputs)

# Kompilacja sieci
model.compile(optimizer=tf.keras.optimizers.Adam(),
              loss="sparse_categorical_crossentropy",
              metrics=['Accuracy'])

print(model.summary())
