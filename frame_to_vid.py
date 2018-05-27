import cv2
import os
import argparse
import collections

ap = argparse.ArgumentParser()
ap.add_argument("-o", "--output", required=False, default='out.mp4', help="output file")
ap.add_argument("-d", "--dir", required=True, help="directory of frames")
ap.add_argument("-f", "--fps", required=True, help="frame per second of the video")
args = vars(ap.parse_args())

dir = args['dir']
images = {}
first = True
h = 0
w = 0
c = 0
for f in os.listdir(dir):
    if first:
        frame = cv2.imread(os.path.join(dir, f))
        h,w,c = frame.shape
        first = False
    frame_num = float(f.split('_')[1].split('frame')[1])
    images.update({frame_num:f})

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(args['output'], fourcc, float(args['fps']), (w, h))

for k in sorted(images):
    frame = cv2.imread(os.path.join(dir,images[k]))
    out.write(frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

out.release()
cv2.destroyAllWindows()
