import cv2
import os
import sys


#example video https://www.youtube.com/watch?v=UdAwX8JB66E
def extract(_id, file_path, target_path):
    vidcap = cv2.VideoCapture(file_path)
    count = 0
    fps = vidcap.get(cv2.CAP_PROP_FPS)
    success, image = vidcap.read()
    print(success)
    while success:
        count += 1
        cv2.imwrite("./{}/{}_frame{}_{}.jpg".format(target_path, str(_id), str(count), target_path), image)
        success,image = vidcap.read()
#    print(count)

def extract_folder(folder_dir):
    ct = 0
    for file in os.listdir(folder_dir):
        filename = os.fsdecode(file)
        if filename.endswith(".mp4"):
            resolution = filename[-8:].split(".")[0]
            print(resolution)
            print(str(ct),filename,resolution)
            ct += 1
            extract(ct,'./' + folder_dir + '/' + filename,resolution)

if __name__ == '__main__':
    extract_folder(sys.argv[1])
#    main("daydream.mkv")
