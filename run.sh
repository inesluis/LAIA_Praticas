#!/bin/bash 
# First, train the model 
python train.py 
# Then, start Flask API 
python app.py
# Finally, run the test client
python test_client.py