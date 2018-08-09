import face_recognition
import pickle
import os
import yaml


WEB_SERVER_CONFIG="db_config.yml"
HOST_KEY="HOST"
USER_KEY="USER"
PORT_KEY="PORT"
PASSWORD_KEY="PASSWORD"
DATBASE_KEY="DATABASE"
ID_KEY="ID"
ENCODING_KEY="ENCODING"
root_directory=os.getcwd()
DATABASE_NAME="employee_database.pkl"
known_images_path = os.path.join(os.getcwd(), "known_images")

with open(WEB_SERVER_CONFIG) as web_config:
    config = yaml.load(web_config)
    host=config[HOST_KEY]
    datbase=config[DATBASE_KEY]
    user=config[USER_KEY]
    port=config[PORT_KEY]
    password=config[PASSWORD_KEY]

class Person:
    def __init__(self, person_id, encoding, first=None, last=None):
        self.person_id=person_id
        self.first=first
        self.last=last
        self.encoding=encoding



def collect_filepaths():
    global known_images_path
    # Create list with all file paths
    known_images_names=os.listdir(known_images_path)
    print("images names: ", known_images_names)
    known_images_paths = [os.path.join(known_images_path, file_) for file_ in known_images_names]
    print("images paths: ", known_images_paths)
    known_images=[[filename, file_path] for filename, file_path in zip(known_images_names, known_images_paths)]
    print("list that will be traversed: ", known_images)
    return known_images


def populate_database(known_images):
    global root_directory
    known_database=[]
    #Train the api with known images
    for known_image in known_images:
        # Load a sample picture and learn how to recognize it.
        image_data = face_recognition.load_image_file(known_image[1])
        face_encoding = face_recognition.face_encodings(image_data)[0]
        person={}
        person[ID_KEY]=known_image[0]
        person[ENCODING_KEY]=face_encoding
        known_database.append(person)
    database=open(DATABASE_NAME, "wb")
    pickle.dump(known_database, database)
    database.close()

if __name__=="__main__":
    known_images=collect_filepaths()
    populate_database(known_images)













