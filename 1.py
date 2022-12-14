import numpy as np
import cv2

query_img = cv2.imread('input/image_3.jpg')
train_img = cv2.imread('input/image_3_template.jpg')

# Convert it to grayscale
query_img_bw = cv2.cvtColor(query_img ,cv2.COLOR_BGR2GRAY )
train_img_bw = cv2.cvtColor(train_img, cv2.COLOR_BGR2GRAY)

# Initialize the ORB detector algorithm
orb = cv2.ORB_create(100000)
# Now detect the keypoints and compute
# the descriptors for the query image
# and train image
queryKeypoints, queryDescriptors = orb.detectAndCompute(query_img_bw ,None)
trainKeypoints, trainDescriptors = orb.detectAndCompute(train_img_bw ,None)

# Initialize the Matcher for matching
# the keypoints and then match the
# keypoints

matcher = cv2.BFMatcher()

matches = matcher.match(queryDescriptors ,trainDescriptors)
# draw the matches to the final image
# containing both the images the drawMatches()
# function takes both images and keypoints
# and outputs the matched query image with
# its train image

final_img = cv2.drawMatches(query_img, queryKeypoints,
                            train_img, trainKeypoints, matches[:30] ,None)



final_img = cv2.resize(final_img, (1000 ,650))

# Show the final image
print(queryKeypoints[0] > queryKeypoints[1])
print((queryKeypoints))

#print(trainKeypoints)

cv2.imshow("Matches", final_img)
cv2.waitKey(10000)

