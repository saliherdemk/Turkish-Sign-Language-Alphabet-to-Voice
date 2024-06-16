# Turkish-Sign-Language-Alphabet-to-Voice

This project is a Turkish Sign Language Alphabet Recognizer using Python.
You can make a sentences and make it talk.

# Demo

<img src="https://github.com/saliherdemk/Turkish-Sign-Language-Alphabet-to-Voice/blob/master/media/demo.gif" width="450" height="355">

# Article (Turkish)

[Turkish Article](https://drive.google.com/file/d/1w7vMpXj_KUjqeKczWPqj6jAhSdFLQhUA/view)

# Alphabet

| <img src="https://github.com/saliherdemk/Turkish-Sign-Language-Alphabet-to-Voice/blob/master/Samples/A.png" width=100 height=80> | <img src="https://github.com/saliherdemk/Turkish-Sign-Language-Alphabet-to-Voice/blob/master/Samples/B.png" width=100 height=80> | <img src="https://github.com/saliherdemk/Turkish-Sign-Language-Alphabet-to-Voice/blob/master/Samples/C.png" width=100 height=80> | <img src="https://github.com/saliherdemk/Turkish-Sign-Language-Alphabet-to-Voice/blob/master/Samples/D.png" width=100 height=80> | <img src="https://github.com/saliherdemk/Turkish-Sign-Language-Alphabet-to-Voice/blob/master/Samples/E.png" width=100 height=80> |
| :------------------------------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------------------------------: |
|                                                                A                                                                 |                                                                B                                                                 |                                                                C                                                                 |                                                                D                                                                 |                                                                E                                                                 |

| <img src="https://github.com/saliherdemk/Turkish-Sign-Language-Alphabet-to-Voice/blob/master/Samples/F.png" width=100 height=80> | <img src="https://github.com/saliherdemk/Turkish-Sign-Language-Alphabet-to-Voice/blob/master/Samples/G.png" width=100 height=80> | <img src="https://github.com/saliherdemk/Turkish-Sign-Language-Alphabet-to-Voice/blob/master/Samples/H.png" width=100 height=80> | <img src="https://github.com/saliherdemk/Turkish-Sign-Language-Alphabet-to-Voice/blob/master/Samples/I.png" width=100 height=80> | <img src="https://github.com/saliherdemk/Turkish-Sign-Language-Alphabet-to-Voice/blob/master/Samples/K.png" width=100 height=80> |
| :------------------------------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------------------------------: |
|                                                                F                                                                 |                                                                G                                                                 |                                                                H                                                                 |                                                                I                                                                 |                                                                K                                                                 |

| <img src="https://github.com/saliherdemk/Turkish-Sign-Language-Alphabet-to-Voice/blob/master/Samples/L.png" width=100 height=80> | <img src="https://github.com/saliherdemk/Turkish-Sign-Language-Alphabet-to-Voice/blob/master/Samples/M.png" width=100 height=80> | <img src="https://github.com/saliherdemk/Turkish-Sign-Language-Alphabet-to-Voice/blob/master/Samples/N.png" width=100 height=80> | <img src="https://github.com/saliherdemk/Turkish-Sign-Language-Alphabet-to-Voice/blob/master/Samples/O.png" width=100 height=80> | <img src="https://github.com/saliherdemk/Turkish-Sign-Language-Alphabet-to-Voice/blob/master/Samples/P.png" width=100 height=80> |
| :------------------------------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------------------------------: |
|                                                                L                                                                 |                                                                M                                                                 |                                                                N                                                                 |                                                                O                                                                 |                                                                P                                                                 |

| <img src="https://github.com/saliherdemk/Turkish-Sign-Language-Alphabet-to-Voice/blob/master/Samples/R.png" width=100 height=80> | <img src="https://github.com/saliherdemk/Turkish-Sign-Language-Alphabet-to-Voice/blob/master/Samples/S.png" width=100 height=80> | <img src="https://github.com/saliherdemk/Turkish-Sign-Language-Alphabet-to-Voice/blob/master/Samples/T.png" width=100 height=80> | <img src="https://github.com/saliherdemk/Turkish-Sign-Language-Alphabet-to-Voice/blob/master/Samples/U.png" width=100 height=80> | <img src="https://github.com/saliherdemk/Turkish-Sign-Language-Alphabet-to-Voice/blob/master/Samples/V.png" width=100 height=80> |
| :------------------------------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------------------------------: |
|                                                                R                                                                 |                                                                S                                                                 |                                                                T                                                                 |                                                                U                                                                 |                                                                V                                                                 |

| <img src="https://github.com/saliherdemk/Turkish-Sign-Language-Alphabet-to-Voice/blob/master/Samples/Y.png" width=100 height=80> | <img src="https://github.com/saliherdemk/Turkish-Sign-Language-Alphabet-to-Voice/blob/master/Samples/Z.png" width=100 height=80> | <img src="https://github.com/saliherdemk/Turkish-Sign-Language-Alphabet-to-Voice/blob/master/Samples/SPACE.png" width=100 height=80> | <img src="https://github.com/saliherdemk/Turkish-Sign-Language-Alphabet-to-Voice/blob/master/Samples/BACKSPACE.png" width=100 height=80> | <img src="https://github.com/saliherdemk/Turkish-Sign-Language-Alphabet-to-Voice/blob/master/Samples/DOT.png" width=100 height=80> |
| :------------------------------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------------------------------------: |
|                                                                Y                                                                 |                                                                Z                                                                 |                                                                Space                                                                 |                                                                Backspace                                                                 |                                                                Dot                                                                 |

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

# pyttsx3

If you want to use Turkish voice, you have to follow [this](https://github.com/nateshmbhat/pyttsx3/issues/25#issuecomment-601512309) steps on Windows. ([Alternative Turkish resource]([this](https://forum.yazbel.com/t/pyttsx3-voice-hatasi-turkce-seslendirme-yapamiyorum/4299/2)))
