import pandas as pd
import random

# List of real Netflix show titles
netflix_titles = [
    "Stranger Things", "Breaking Bad", "Money Heist", "The Witcher", "Bridgerton", "Narcos",
    "Squid Game", "Dark", "The Queen's Gambit", "House of Cards", "BoJack Horseman",
    "13 Reasons Why", "Black Mirror", "You", "The Crown", "Ozark", "Mindhunter",
    "Better Call Saul", "Love, Death & Robots", "Elite", "Sex Education", "Lupin",
    "The Umbrella Academy", "Wednesday", "Alice in Borderland", "Sweet Tooth",
    "Shadow and Bone", "Arcane", "Locke & Key", "Outer Banks", "The Sandman", "Peaky Blinders"
]

# Genres & Ratings
genres = ["Drama", "Comedy", "Action", "Thriller", "Horror", "Sci-Fi", "Documentary", "Romance"]
ratings = ["G", "PG", "PG-13", "R", "TV-MA", "TV-14", "TV-Y7"]

# Function to generate dataset
def generate_netflix_data(num_entries, id_start=1):
    random.shuffle(netflix_titles)
    while len(netflix_titles) < num_entries:
        netflix_titles.extend(random.sample(netflix_titles, num_entries - len(netflix_titles)))
    
    data = []
    for i in range(num_entries):
        data.append({
            "Show_ID": id_start + i,
            "Title": netflix_titles[i],
            "Genre": random.choice(genres),
            "Rating": random.choice(ratings),
            "Views": random.randint(1000, 1000000),
            "Release_Year": random.randint(2000, 2024)
        })
    return pd.DataFrame(data)

# Generate original dataset
data1 = generate_netflix_data(50)

# Create modified dataset with discrepancies
data2 = data1.copy()

# Introduce random changes in Views & Rating for 30 shows
for _ in range(30):
    idx = random.randint(0, len(data2) - 1)  # Fixing index range
    data2.at[idx, "Views"] = random.randint(1000, 1000000)
    data2.at[idx, "Rating"] = random.choice(ratings)


# Remove 10 random shows & add 10 new ones
data2 = data2.drop(data2.sample(10).index)
new_entries = generate_netflix_data(10, id_start=201)
data2 = pd.concat([data2, new_entries], ignore_index=True)

# Print to verify data exists
print("Data1 Preview:\n", data1.head())
print("Data2 Preview:\n", data2.head())

# Save datasets
data1.to_csv("netflix_real_data1.csv", index=False)
data2.to_csv("netflix_real_data2.csv", index=False)

print("Datasets created: netflix_real_data1.csv & netflix_real_data2.csv")
 
# Function to compare two datasets
def compare_datasets(data1, data2):
    # Show the first 10 rows of data1 and data2
    print("First 10 rows of data1:")
    print(data1.head(10))
    
    print("\nFirst 10 rows of data2:")
    print(data2.head(10))
    
    # 1. Show Title Consistency
    consistency = pd.merge(data1[['Show_ID', 'Title', 'Genre', 'Rating', 'Views', 'Release_Year']],
                           data2[['Show_ID', 'Title', 'Genre', 'Rating', 'Views', 'Release_Year']],
                           on='Title', how='outer', suffixes=('_data1', '_data2'))
    
    # Shows that exist in both datasets but with discrepancies in Views or Rating
    discrepancies = consistency[(consistency['Views_data1'] != consistency['Views_data2']) | 
                                (consistency['Rating_data1'] != consistency['Rating_data2'])]
    
    print("\nDiscrepancies in Views or Rating between data1 and data2:")
    print(discrepancies[['Title', 'Views_data1', 'Views_data2', 'Rating_data1', 'Rating_data2']])

    # 2. New Shows in data2
    new_shows = data2[~data2['Title'].isin(data1['Title'])]
    
    print("\nNew Shows in data2 (not present in data1):")
    print(new_shows[['Title', 'Genre', 'Rating', 'Views', 'Release_Year']])

    # 3. Removed Shows from data2
    removed_shows = data1[~data1['Title'].isin(data2['Title'])]
    
    print("\nRemoved Shows from data2 (present in data1 but not in data2):")
    print(removed_shows[['Title', 'Genre', 'Rating', 'Views', 'Release_Year']])

    # 4. Overall Summary
    print("\nOverall Comparison Summary:")
    print(f"Total number of shows in data1: {len(data1)}")
    print(f"Total number of shows in data2: {len(data2)}")
    print(f"Number of shows with discrepancies: {len(discrepancies)}")
    print(f"Number of new shows in data2: {len(new_shows)}")
    print(f"Number of removed shows from data2: {len(removed_shows)}")

# Example Usage:
compare_datasets(data1, data2)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Function to compare two datasets with visualizations
def compare_datasets(data1, data2):
    # Show the first 10 rows of data1 and data2
    print("First 10 rows of data1:")
    print(data1.head(10))
    
    print("\nFirst 10 rows of data2:")
    print(data2.head(10))

    # 1. Show Title Consistency
    consistency = pd.merge(data1[['Show_ID', 'Title', 'Genre', 'Rating', 'Views', 'Release_Year']],
                           data2[['Show_ID', 'Title', 'Genre', 'Rating', 'Views', 'Release_Year']],
                           on='Title', how='outer', suffixes=('_data1', '_data2'))
    
    # Shows that exist in both datasets but with discrepancies in Views or Rating
    discrepancies = consistency[(consistency['Views_data1'] != consistency['Views_data2']) | 
                                (consistency['Rating_data1'] != consistency['Rating_data2'])]
    
    print("\nDiscrepancies in Views or Rating between data1 and data2:")
    print(discrepancies[['Title', 'Views_data1', 'Views_data2', 'Rating_data1', 'Rating_data2']])

    # 2. New Shows in data2
    new_shows = data2[~data2['Title'].isin(data1['Title'])]
    
    print("\nNew Shows in data2 (not present in data1):")
    print(new_shows[['Title', 'Genre', 'Rating', 'Views', 'Release_Year']])

    # 3. Removed Shows from data2
    removed_shows = data1[~data1['Title'].isin(data2['Title'])]
    
    print("\nRemoved Shows from data2 (present in data1 but not in data2):")
    print(removed_shows[['Title', 'Genre', 'Rating', 'Views', 'Release_Year']])

    # 4. Visualizations
    plt.figure(figsize=(10, 6))

    # Distribution of Views in data1 and data2
    plt.subplot(2, 2, 1)
    sns.histplot(data1['Views'], color='blue', kde=True, label='data1', bins=15)
    sns.histplot(data2['Views'], color='red', kde=True, label='data2', bins=15)
    plt.title('Views Distribution Comparison')
    plt.legend()

    # Distribution of Ratings in data1 and data2
    plt.subplot(2, 2, 2)
    sns.countplot(data=data1, x='Rating', palette='Blues', label='data1')
    sns.countplot(data=data2, x='Rating', palette='Reds', label='data2')
    plt.title('Rating Distribution Comparison')
    plt.legend()

    # Bar chart showing discrepancies
    plt.subplot(2, 2, 3)
    discrepancies_count = len(discrepancies)
    plt.bar(['Discrepancies'], [discrepancies_count], color='purple')
    plt.title('Number of Discrepancies')

    # Bar chart showing new and removed shows
    plt.subplot(2, 2, 4)
    new_shows_count = len(new_shows)
    removed_shows_count = len(removed_shows)
    plt.bar(['New Shows in data2', 'Removed Shows from data2'], 
            [new_shows_count, removed_shows_count], color=['green', 'orange'])
    plt.title('New and Removed Shows')

    plt.tight_layout()
    plt.show()

    # 5. Overall Summary
    print("\nOverall Comparison Summary:")
    print(f"Total number of shows in data1: {len(data1)}")
    print(f"Total number of shows in data2: {len(data2)}")
    print(f"Number of shows with discrepancies: {len(discrepancies)}")
    print(f"Number of new shows in data2: {len(new_shows)}")
    print(f"Number of removed shows from data2: {len(removed_shows)}")

# Example Usage:
compare_datasets(data1, data2)


