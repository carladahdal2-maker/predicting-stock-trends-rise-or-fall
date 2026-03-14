Stock Trend Prediction

This project implements a neural network for predicting short-term stock price movements (rise or fall).
It uses a custom deep learning framework built from scratch, including layers, activations, losses, and optimizers.
The model leverages technical indicators such as moving averages, RSI, volatility, and momentum to forecast future trends.

- Features

Fully modular neural network with support for Dense, Conv1D, Dropout, and BatchNorm layers.

Multiple activation functions: ReLU, Sigmoid, Tanh, Linear.

Loss functions: Binary Cross-Entropy, Mean Squared Error, Softmax Cross-Entropy.

Optimizers: SGD and Momentum.

Data preprocessing and feature engineering including rolling statistics and normalization.

- Dataset

The training and test datasets are not included in this repository due to their size. They can be downloaded from the competition page:

Kaggle: Predicting Stock Trends - Rise or Fall

After downloading, place the CSV files in the data/ directory.

Usage
python main.py

Make sure you have the datasets in the data/ folder. The code automatically preprocesses the data and trains the model.
