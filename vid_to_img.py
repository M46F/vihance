import cv2


#example video https://www.youtube.com/watch?v=UdAwX8JB66E
def main(file_path):
    vidcap = cv2.VideoCapture(file_path)
    vidcap2 = cv2.VideoCapture(file_path)
    success,image = vidcap.read()
    count = 0

    while success:
        cv2.imwrite("frame%d_original.jpg" % count, image)
        resized = cv2.resize(image, (640, 360), interpolation = cv2.INTER_LINEAR)
        cv2.imwrite("frame%d_360p.jpg" % count, resized)
        success,image = vidcap.read()
        count += 1
        if count%100 == 0:
            lanjut = input("continue?(y/n)>")
            if lanjut == 'n':
                break

if __name__ == '__main__':
    print("example (please download the video first or change file_path params)")
    main("The Never-Ending Game of Dungeons & Dragons.mp4")
