import os
import shutil

def train_test_split(BASE_PATH, DESTINATION_PATH, train_size):
    
    CLASS_PATH = os.listdir(BASE_PATH)
    
    if not os.path.isdir(DESTINATION_PATH):
        os.makedirs(DESTINATION_PATH)

    for CLASS in CLASS_PATH:
        DATA_PATHS = os.listdir(os.path.join(BASE_PATH, CLASS))
        TRAIN_SIZE = int(len(DATA_PATHS) * train_size)
        TRAIN_DATA_PATHS = DATA_PATHS[:TRAIN_SIZE]
        TEST_DATA_PATHS = DATA_PATHS[TRAIN_SIZE + 1: ]
        print(len(TRAIN_DATA_PATHS), len(TEST_DATA_PATHS))

        train_destination = os.path.join(DESTINATION_PATH, "train", CLASS) 
        test_destination = os.path.join(DESTINATION_PATH, "test", CLASS) 

        if not os.path.isdir(train_destination):
            os.makedirs(train_destination)

        for DATA_PATH in TRAIN_DATA_PATHS:
            source = os.path.join(BASE_PATH, CLASS, DATA_PATH)
            print("source : ", source)
            print("destination : ", train_destination)
            shutil.copy(source, train_destination)
        
        if not os.path.isdir(test_destination):
            os.makedirs(test_destination)

        for DATA_PATH in TEST_DATA_PATHS:
            source = os.path.join(BASE_PATH, CLASS, DATA_PATH)
            print("source : ", source)
            print("destination : ", test_destination)
            shutil.copy(source, test_destination)
            
            
if __name__ == "__main__":
    train_test_split("Data", "New_Data", 0.80)