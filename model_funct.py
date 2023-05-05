from keras.models import load_model
from keras.preprocessing.text import Tokenizer
from keras.utils import pad_sequences
import tensorflow as tf

model = load_model('senti_model_main.h5')

def get_sequences(title):
    tokenizer = tf.keras.preprocessing.text.Tokenizer(num_words=300, filters=' ', oov_token='UNK')
    tokenizer.fit_on_texts([title])
    
    title_sequences = tokenizer.texts_to_sequences([title])
    title_sequence = title_sequences[0]
    
    padded_title = tf.keras.preprocessing.sequence.pad_sequences([title_sequence], maxlen=71, padding='post')

    return padded_title

def prediction(title):
    preprocessed_title = get_sequences(title)
    prediction_array = model.predict(preprocessed_title)
    return prediction_array

