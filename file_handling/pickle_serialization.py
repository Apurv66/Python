import pickle

data = ["apple", "banana", "cherry"]

with open("data.pkl", "wb") as f:
    pickle.dump(data, f)   # Saves the Python object into a file
