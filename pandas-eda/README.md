# Book Popularity Analysis

This project analyzes the popularity of books based on attributes such as genre, publication year, and ratings. The goal is to uncover trends in book popularity, with a particular focus on the fantasy genre. By exploring average ratings and the distribution of genres over time, the analysis provides insights into which genres and books are most appreciated by readers.

## Dataset

The dataset used in this analysis includes 500 books with attributes like:

- **Title**: The title of the book.
- **Author**: The author of the book.
- **Publication Year**: The year the book was published.
- **Genre**: The genre(s) the book belongs to.
- **Average Rating**: The average rating of the book on Goodreads.
- **Number of Ratings**: The number of ratings the book has received.

Some columns contain missing values, which are noted and addressed during the analysis.

**Dataset Source**: [Link to dataset](https://raw.githubusercontent.com/melaniewalsh/responsible-datasets-in-context/main/datasets/top-500-novels/library_top_500.csv)

## Analysis Overview

The project focuses on the following areas:

- **Genre Popularity**: Exploring which genres are the most popular based on ratings and counts.
- **Consistency in Ratings**: Examining trends in average ratings across different publication years and genres.
- **Enduring Appeal of Fantasy and Classics**: Investigating the top-rated books, especially focusing on classic fantasy literature.

Visualizations like line charts and bar plots are used to illustrate these trends.

## Requirements

To run the project, make sure you have the following Python packages installed:
- `pandas`
- `altair`
