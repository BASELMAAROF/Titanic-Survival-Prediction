#Import libraries
from flask import Flask, render_template
import pandas as pd 
import matplotlib.pyplot  as plt 
import seaborn as sns 
import os
#print("Libraries loaded successfully!")


app = Flask(__name__)


@app.route("/")
def home():



# Load Titanic data
    df = pd.read_csv("train.csv")

# Print the dataset
    print(df.head())


# Basic info
#print(df.info())


# Count of Survived people
#print(df["Survived"].value_counts())

    #Create graph
    sns.countplot(x="Survived",data=df)
    plt.title("Survival Count")

    # save the graph into static folder
    graph_path = os.path.join('static', 'survival_graph.png')
    plt.savefig(graph_path)
    plt.close()


    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)




#plt.show()

# Plot and save
#s.countplot(x="Survived", data=df)
#plt.title("Survival Count")
#plt.savefig("survival_graph.png")  # Save the figure
#plt.close()  # Close the plot




