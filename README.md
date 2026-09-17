# Pav Bhaji Text Classification

This is a machine learning project I built to classify food-related Instagram posts into two categories:

- Pav Bhaji
- Not Pav Bhaji

The idea behind the project was simple: use the caption and hashtags from an Instagram food post and let a machine learning model decide whether the post is related to Pav Bhaji.

## About the Project

I used a dataset containing Instagram food posts with captions, hashtags, and other post information.

The text from the captions and tags was combined and cleaned before training the machine learning models. I then converted the text into numerical features using TF-IDF and used those features to train different classification algorithms.

The complete workflow includes data preprocessing, text cleaning, feature extraction, model training, evaluation, and testing with new text.

## Dataset

The dataset contains 452 records.

After checking the labels:

- 269 posts are Non-Pav Bhaji
- 183 posts are Pav Bhaji

The labels are:

```text
0 = Non-Pav Bhaji
1 = Pav Bhaji