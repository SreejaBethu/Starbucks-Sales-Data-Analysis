import pandas as pd
import matplotlib.pyplot as plt
from fuzzywuzzy import process

def load_dataset(file_path=r"https://raw.githubusercontent.com/prasertcbs/basic-dataset/master/Starbucks%20satisfactory%20survey.csv"):
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None

def find_best_match(column_names, target_column):
    best_match = process.extractOne(target_column, column_names)
    return best_match[0]

def set_index(df, column_name):
    try:
        df.set_index(column_name, inplace=True)
        print("Index set successfully.")
    except Exception as e:
        print(f"Error setting index: {e}")

import matplotlib.pyplot as plt

def visualize_data(df):
    plt.rcParams.update({'font.size': 10})
    fig, axs = plt.subplots(4, 1, figsize=(10, 25))
    plt.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.9, wspace=0.2, hspace=1.2)
    
# Create a plot
plt.plot([0,1, 2, 3])

# Render the plot in a GitHub README file
plt.ion()
plt.show(block=False)

    # Histogram
    axs[0].hist(df['12. How would you rate the quality of Starbucks compared to other brands (Coffee Bean, Old Town White Coffee..) to be:'], bins=10, color='skyblue')
    axs[0].set_title('Distribution of Ratings')

    # Box Plot
    bp = axs[1].boxplot(df['12. How would you rate the quality of Starbucks compared to other brands (Coffee Bean, Old Town White Coffee..) to be:'],patch_artist=True)

    for element in ['boxes', 'whiskers', 'fliers', 'means', 'medians', 'caps']:
        plt.setp(bp[element], color='black')

    for patch in bp['boxes']:
        patch.set(facecolor='lightblue')

    axs[1].set_title('Box Plot of Ratings')

    # Bar Chart
    ratings_by_gender = df.groupby('2. Your Age')['12. How would you rate the quality of Starbucks compared to other brands (Coffee Bean, Old Town White Coffee..) to be:'].mean()
    axs[2].bar(ratings_by_gender.index, ratings_by_gender.values, color='orange')
    axs[2].set_title('Average Rating by Age')

    # Scatter Plot
    axs[3].scatter(df['12. How would you rate the quality of Starbucks compared to other brands (Coffee Bean, Old Town White Coffee..) to be:'], df['13. How would you rate the price range at Starbucks?'], color='green')
    axs[3].set_title('Relationship between Quality Rating and Price Range Rating')

    plt.suptitle('Starbucks Survey Results')
    plt.show()


def main():
    df = load_dataset()
    if df is not None:
        print("Column Names:")
        print(df.columns.tolist())
        target_column = 'Respondent ID'
        similar_column_names = [col for col in df.columns if target_column.lower() in col.lower()]
        print("Similar column names:", similar_column_names)
        best_match = find_best_match(df.columns.tolist(), target_column)
        print("Found column:", best_match)
        print("Best match:", best_match)
        set_index(df, best_match)
        visualize_data(df)

if __name__ == "__main__":
    main()
