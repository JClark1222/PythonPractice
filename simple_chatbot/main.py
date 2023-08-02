import nltk
from nltk.stem.lancaster import LancasterStemmer 
stemmer = LancasterStemmer()

import numpy
import tflearn
import random
import json
import pickle
import tensorflow as tf

with open("intents.json") as file:
    data = json.load(file)

try:
    with open("data.pickle", "rb") as f:
        words, labels, training, output = pickle.load(f)
except:
    words = []
    labels = []
    docs_x = []
    docs_y = []

    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            wrds = nltk.word_tokenize(pattern)
            words.extend(wrds)
            docs_x.append(wrds)
            docs_y.append(intent["tag"])

            if intent["tag"] not in labels:
                labels.append(intent["tag"])

    words = [stemmer.stem(w.lower()) for w in words if w != "?"]
    words = sorted(list(set(words)))

    labels = sorted(labels)

    #Creating the training and testing output
    training = []
    output = []

    out_empty = [0 for _ in range(len(labels))]

    for x, doc in enumerate(docs_x):
        bag = []

        wrds = [stemmer.stem(w) for w in doc]

        for w in words:
            if w in wrds:
                bag.append(1)
            else:
                bag.append(0)

        output_row = out_empty[:]
        output_row[labels.index(docs_y[x])] = 1

        training.append([bag])
        output.append(output_row)

    training = numpy.array(training)
    output = numpy.array(output)

    with open("data.pickle", "wb") as f:
        pickle.dump((words, labels, training, output), f)

#Building the model using tensorflow
tf.compat.v1.reset_default_graph()

#Neural Network
net = tflearn.input_data(shape=[None, len(training[0]), 46])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
net = tflearn.regression(net)

# Define the path to the directory where checkpoints are saved
'''save_dir = "C:\\Users\\JClark\\coding\\CodingPractice\\simple_chatbot\\"

# Load the model from the checkpoint directory
model = tflearn.DNN(net)
model.load(save_dir)'''

#Training the model
model = tflearn.DNN(net)

try:
    model.load("model.tflearn")
except:
    model.fit(training, output, n_epoch=1000, batch_size=8, show_metric=True)
    model.save("model.tflearn")

#This is where we start to make the predictions
def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]

    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1
    return numpy.array(bag)


#Code that will ask the user for a sentence
def chat():
    print("Start talking with the bot! (Type quit to stop)")
    while True:
        inp = input("You: ")
        if inp.lower() == "quit":
            break
        # results = model.predict(numpy.reshape(bag_of_words(inp, words), 46))
        #results = model.predict([bag_of_words(inp, words)])
        
        results = model.predict(numpy.reshape(bag_of_words(inp, words), (-1, 1, 46)))
        results_index = numpy.argmax(results)
        tag = labels[results_index]
        
        for tg in data["intents"]:
            if tg['tag'] == tag:
                responses = tg['responses']
        
        print(responses)
        print(random.choice(responses))

chat()