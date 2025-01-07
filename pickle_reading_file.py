import pickle

data = {'us':[1, 2, 3], 'uk':[4, 5, 6], 'ps':[7, 8, 9]}
with open("data.pkl", "wb") as file:
    pickle.dump(data, file)

print("Dictionary written to file using pickle.")

# Read dictionary from file
with open("data.pkl", "rb") as file:
    loaded_data = pickle.load(file)

print("Loaded dictionary:", loaded_data)