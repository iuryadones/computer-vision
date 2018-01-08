from sklearn.neighbors import KNeighborsClassifier

data = [[1,2],[2,2],[3,2]]
labels = ['i','u', 'a']

print("[INFO] training classifier...")
model = KNeighborsClassifier(n_neighbors=1)
model.fit(data, labels)
print("[INFO] evaluating...")

print(model.predict([[2, 2]]))
