# import the opencv library
import cv2


# define a video capture object
vid = cv2.VideoCapture(0)


while(True):
	print("Press q to quit")
	# Capture the video frame
	# by frame
	ret, frame = vid.read()
	print("Press q to quit")

	# # Display the resulting frame
	cv2.imshow('Webcam', frame)
	
	# the 'q' button is set as the
	# quitting button you may use any
	# desired button of your choice
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# # After the loop release the cap object
# vid.release()
# Destroy all the windows
# cv2.destroyAllWindows()
