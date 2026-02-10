class AIModel:
    def train(self,data):
        print(f"Training model by {data}")

    def predict(self,input):
        print(f"Prediciting output by the {input}")

    def save_file(self,filename):
        print(f"Saving model to file by filename {filename}")
    
    def load_file(self,filename):
        print("Loading file data from {filename}")



sample = AIModel()

sample.train(10)