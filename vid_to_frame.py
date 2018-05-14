import cv2
import os
import sys


#example video https://www.youtube.com/watch?v=UdAwX8JB66E
def extract(_id, file_path, target_path):
    print(_id, file_path, target_path)
    vidcap = cv2.VideoCapture(file_path)
    count = 0
    fps = vidcap.get(cv2.CAP_PROP_FPS)
    success, image = vidcap.read()
#    print(success)
    while success:
        count += 1
        target_write = "./{}{}_frame{}_{}.jpg".format(target_path, str(_id), str(count), target_path[:-1])
        print(target_write)
        cv2.imwrite(target_write, image)
#        print(count)
        success,image = vidcap.read()
#    print(count)

def extract_folder(folder_dir, dir_360p, dir_720p):
    ct = 0
    for file in os.listdir(folder_dir):
        filename = os.fsdecode(file)
        if filename.endswith(".mp4"):
            resolution = filename[-8:].split(".")[0]
            if resolution == '360p':
                extract(ct, './' + folder_dir + '/' + filename, dir_360p)
            elif resolution == '720p':
                extract(ct, './' + folder_dir + '/' + filename, dir_720p)

if __name__ == '__main__':
    extract_folder(sys.argv[1], sys.argv[2], sys.argv[3])
#    main("daydream.mkv")
