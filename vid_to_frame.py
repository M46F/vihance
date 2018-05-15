import cv2
import os
import sys
import json


def extract(_id, file_path, target_path):
    print(_id, file_path, target_path)
    vidcap = cv2.VideoCapture(file_path)
    count = 0
    fps = int(vidcap.get(cv2.CAP_PROP_FPS))
    print(fps)
    success, image = vidcap.read()
    while success:
        count += 1
        if count % fps == 0:
            target_write = "./{}{}_frame{}_{}.jpg".format(
                target_path, str(_id), str(count/fps), target_path[:-1])
            # print(target_write)
            cv2.imwrite(target_write, image)
        success, image = vidcap.read()


def extract_folder(folder_dir, dir_360p, dir_720p):
    dict_of_vid = {}
    dir_dict = {'360p': dir_360p, '720p': dir_720p}
    for file in os.listdir(folder_dir):
        filename = os.fsdecode(file)
        resolution = filename[-8:].split(".")[0]
        name = filename[:-9]
        if name in dict_of_vid:
            dict_of_vid[name]['resolution'].update({resolution: filename})
        else:
            dict_of_vid.update({name: {'resolution': {resolution: filename}}})
        # if filename.endswith(".mp4"):
        #     if resolution == '360p':
        #         extract(ct, './' + folder_dir + '/' + filename, dir_360p)
        #     elif resolution == '720p':
        #         extract(ct, './' + folder_dir + '/' + filename, dir_720p)
    _id = 0
    for k in dict_of_vid:
        if len(dict_of_vid[k]['resolution']) < 2:
            print("skip", k)
            continue
        for res in dict_of_vid[k]['resolution']:
            extract(_id, './' + folder_dir + '/' + dict_of_vid[k]['resolution'][res], dir_dict[res])
        dict_of_vid[k].update({'id': _id})
        _id += 1
    with open('data.json', 'w') as fp:
        json.dump(dict_of_vid, fp)


if __name__ == '__main__':
    extract_folder(sys.argv[1], sys.argv[2], sys.argv[3])
#    main("daydream.mkv")
