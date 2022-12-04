# Turkish-Sign-Language-Alphabet-to-Voice

This project is a Turkish Sign Language Alphabet Recognizer using Python.
You can make a sentences and make it talk.

# Demo
<img src="https://github.com/saliherdemk/Turkish-Sign-Language-Alphabet-to-Voice/blob/master/media/demo.gif" width="450" height="355">

# Article (Turkish)
[Turkish Article](https://drive.google.com/file/d/1w7vMpXj_KUjqeKczWPqj6jAhSdFLQhUA/view)

# Requirements
```
pip install -r requirements.txt
```

# Trained Data
You can download trained data from [Here](https://drive.google.com/file/d/1ApQOGHlMVP52LSJoSoBsvw46gDHgda2-/view?usp=sharing)

# Model
I tried diffirent models and i implemented the most optimum model in the model.py file.
You can compare models with tensorboard.
```
tensorboard --logdir=logs
```

# Usage
First of all you need to train the model and save it.
```
python model.py
```
Then you can use this model to recognize sign language in real-time through webcam.
```
python prediction.py
```
Also you can create your own dataset with collectImg.py file. Once you done that don't forget convert images to numpy array with createData.py. Be careful with the file paths.
