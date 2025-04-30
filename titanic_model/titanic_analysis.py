import pandas as pd 
import matplotlib.pyplot  as plt 
import seaborn as sns

# Load Titanic data
df = pd.read_csv("train.csv")

# Print the dataset
#print(df.head())

                                            # step 2: Basic Data Exploration

# Data types and missing values
#print(df.info())


# Get the number of rows and columns
#print(df.shape)


#Get some basic statistical details of the numerical columns.
#print(df.describe())


#identify which columns have missing values and how many.
#print(df.isnull().sum())


                                                    # Step 4: Data Cleaning
# Handle Missing Data:



df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
df.drop(columns=['Cabin'], inplace=True)




print(df.isnull().sum())



#print(df.info())



# Check the current column names
#print(df.columns)


                                                     #Step 5: Exploratory Data Analysis (EDA)

# 1.Visualizing Age Distribution:                            


"""
sns.histplot(df['Age'], kde= True)
plt.title("Age Distribution of Titanic Passengers")
plt.show()


# 2.Survival Rate by Class:
#Explore survival rates by passenger class.

sns.barplot(x= "Pclass",  y="Survived" , data=df)
plt.title('Survival Rate by Class')
plt.show()

"""


#5.2: Handle Categorical Variables

df['Survived'] = df['Survived'].astype('category')
df['Pclass'] = df['Pclass'].astype('category')

# Convert categorical variables into numerical values
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})

# One-hot encoding for 'Embarked' and 'Pclass'
df = pd.get_dummies(df, columns=['Embarked', 'Pclass'], drop_first=True)

# Check the updated DataFrame
#df.head()

#print(df.info())


#print(df.describe())

#print(df)


                                                   #Step 6: Feature Engineering


#6.1: Create a Family Size Feature


# Create a FamilySize feature
df['FamilySize'] = df['SibSp'] + df['Parch'] + 1  # +1 to include the passenger itself

# Drop SibSp and Parch as they are now redundant
df = df.drop(['SibSp', 'Parch'], axis=1)




# Display the first few rows of the cleaned data
print("After preprocessing:")
print(df.head())

#                                                       2. Model Performance Output

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import accuracy_score



# Define the feature columns (X) and target column (y)
X = df.drop('Survived', axis=1)  # X will contain all columns except 'Survived'
y = df['Survived']  # y will contain the 'Survived' column, which is the target




# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the Logistic Regression model
model = LogisticRegression(max_iter=1000)  # Ensure model is initialized
model.fit(X_train, y_train)  # Train the model

# Now you can use the model to make predictions
y_pred = model.predict(X_test)

# Evaluate the model's accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")