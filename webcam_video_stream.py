from threading import Thread
import cv2

class WebcamVideoStream:
	def __init__(self, src=0):
		self.cam = cv2.VideoCapture(0)
		if self.cam.read()[0] == False:
			self.cam = cv2.VideoCapture(1)
		self.img = cv2.flip(self.cam.read()[1],1)
		#self.img = cv2.flip(img,1)
		self.stopped = False

	def start(self):
		Thread(target=self.update, args=()).start()
		return self

	def update(self):
		while not self.stopped:
			self.img = self.cam.read()[1]

	def read(self):
		return self.img

	def save(self, location):
		cv2.imwrite(location, self.read())

	def stop(self):
		self.cam.release()
		self.stopped = True

