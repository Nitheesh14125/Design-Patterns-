class AIModel :
    def train(Self,data):
        print(f"Training the model with the {data} data")
    
    def predict(self,input):
        print(f"Predicting output by the {input} data ")


class Storing:
    def save_file(self,filename):
        print(f"Saving file with the {filename}")

    def load_filedata(self,filename):
        print(f"Loading filedata in {filename}")



a1 = AIModel()
a1.train(10)
a1.predict(21)


s1 = Storing()
s1.save_file("Nitheesh_data")
s1.load_filedata("Nitheesh_Data")