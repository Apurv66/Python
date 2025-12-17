import pickle

with open("data.pkl", "rb") as f:
    data = pickle.load(f)  # Loads the Python object from the file

print(data)
