# Gesture Recognition for HCI


Gestures are one of the most intuitive ways of communicating, conveying and conversing. The advantages of this are - 

  - Intuitive
  - Easily understandable
  - Doesn't require much effort

# Features

Gestures can also be used as a way of interacting with a system. They can be of great use when used as an interaction method. Gestures can be used to control the mouse, enter text, execute keyboard shotcuts, and much more without a single touch. They don't require physical touch and are way more useful than traditional interaction devices.


In this project, the following features are implemented:
  - Execute keyboard shortcuts with gestures
  - Typing with the help of gestures

These usecases can be easily extended to controlling the mouse and interacting with a virtual keyboard using this mouse.

> Gesture recognition can be seen as a way for computers to begin to understand human body language, thus building a richer bridge between machines and humans than primitive text user interfaces or even GUIs (graphical user interfaces), which still limit the majority of input to keyboard and mouse and interact naturally without any mechanical devices.

Using the concept of gesture recognition, it is possible to point a finger at this point will move accordingly. This could make conventional input on devices such and even redundant.

### Tech

Gesture Recognition for HCI uses a number of open source modules and an open source dataset to work properly:

#### Dataset used
For this project we used the EMNIST (Extended MNIST) dataset. It is freely available on the Internet. You should read about it here <a href="https://arxiv.org/pdf/1702.05373.pdf">https://arxiv.org/pdf/1702.05373.pdf</a>. If you want to download the original dataset click <a href="https://cloudstor.aarnet.edu.au/plus/index.php/s/54h3OuGJhFLwAlQ/download">here</a>.<br>
For this project we are using only the 'letters' dataset.

#### Requirements
1. Python 3.x
2. Keras with Tensorflow as backend
3. OpenCV 3.4
4. h5py
5. Jupyter-Notebook (to view and train_model.ipynb and store_images.ipynb)
6. pyautogui
7. A good CPU
8. A good GPU (not compulsory but recommended)
9. Patience. A lot of it......

### Installation

Install the dependencies required for the project as follows - 

```
$ pip install -r requirements.txt
```

## How to use this project
1. First set the HSV masking range for the paper that you are wearing in your finger. To do that run this file

```
$ python range-detector.py -f HSV -w
```
The easiest way to use it is to put any colour paper in front of the camera and then slowly increasing the lower parameters(H_MIN, V_MIN, S_MIN) one by one and then slowly decreasing the upper parameters (H_MAX, V_MAX, S_MAX). When the adjusting has been done you will find that only the colour paper will have a corresponding white patch and rest of the image will be dark. 

2. Now run the gesture_action_cnn file.
```
$ python gesture_action_cnn.py
```

Press `t` or `s` to toggle between typing and keyboard shortcuts mode.
## Keyboard Shortcuts
1. A = Ctrl + A (Select all)
2. C = Ctrl + C (Copy)
3. E = Open Explorer
4. F = Open Facebook
5. L = Win + L (Lock the computer)
6. M = Win (Start Menu)
7. N = Ctrl + N (New File)
8. O = Take a screenshot
9. P = Take a photo with a 5 sec delay
10. R = Win + R (Open Run dialog)
11. S = Ctrl + S (Save file)
12. T = Ctrl + Shift + T (Open Task Manager)
13. V = Ctrl + V (Paste)
14. X = Ctrl + X (Cut)
15. Z = Ctrl + Z (Undo)

The actions performed for gestures can be changed as needed by changing the `action.py` file
