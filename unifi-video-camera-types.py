from pymongo import MongoClient

#Creating a pymongo client
client = MongoClient('localhost', 7441)

#Getting the database instance
db = client['av']
cameras = db['camera']
camera_types = {}
for camera in cameras.find():
    try:
        camera_types[camera["model"]] += 1
    except:
        camera_types[camera["model"]] = 1
print camera_types
