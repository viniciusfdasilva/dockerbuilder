from tqdm import tqdm
from time import sleep

class Utils():

    @staticmethod
    def get_progress():
        for i in tqdm(range(100)):
            sleep(0.2)
        
