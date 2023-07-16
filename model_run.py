import tensorflow as tf
from data import train_ds, test_ds, valid_ds
from consts import *
from model import model, early_stopping

# Trening modelu
history1 = model.fit(train_ds,
                     batch_size=BATCH_SIZE,
                     epochs=EPOCHS,
                     callbacks=[early_stopping],
                     validation_data=valid_ds,
                     use_multiprocessing=True)

# Fakultatywnie
# history2 = model.fit(test_ds,
#                      batch_size=BATCH_SIZE,
#                      epochs=EPOCHS,
#                      callbacks=[early_stopping],
#                      validation_data=valid_ds,
#                      use_multiprocessing=True)

# Ewaluacja modelu po treningu
print(model.evaluate(valid_ds))

# Zapis modelu do pliku
tf.keras.saving.save_model(model, DATA_PATH, overwrite=True, save_format=None)
