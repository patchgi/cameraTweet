import cv2
import tweepy

CONSUMER_KEY="****"
CONSUMER_SECRET="****"
ACCESS_TOKEN="****"
ACCESS_SECRET="****"

cameraPort=0
def shotCamera():
	cap=cv2.VideoCapture(cameraPort)
	size=None
	while(True):
		ret,frame=cap.read()
		if size is not None and len(size) == 2:
			frame = cv2.resize(frame, size)
		cv2.imshow("camera",frame)

		k=cv2.waitKey(1)
		if k>=0:
			cv2.imwrite("shot.png",frame)
			break
	cap.release()
	cv2.destroyAllWindows()

def tweetImg():
	text=raw_input("inputTweetText>>>")
	hashTag=raw_input("hashTag>>>")
	if hashTag!="":
		text+=" #"+hashTag
	try:
		auth=tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
		auth.set_access_token(ACCESS_TOKEN,ACCESS_SECRET)
		api=tweepy.API(auth)

		api.update_with_media(status=text,filename='shot.png')

	except tweepy.TweepError as e:
		print e.reason

if __name__=="__main__":
	shotCamera()
	tweetImg()
