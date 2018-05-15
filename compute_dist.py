
import sys
from skimage.measure import compare_ssim as ssim
from scipy.misc.pilutil import imread
from scipy.misc import imresize
from scipy.linalg import norm
from scipy import sum, average
import cv2

def to_grayscale(arr):
    "If arr is a color image (3D array), convert it to grayscale (2D array)."
    if len(arr.shape) == 3:
        return average(arr, -1)  # average over the last axis (color channels)
    else:
        return arr

def normalize(arr):
    rng = arr.max()-arr.min()
    amin = arr.min()
    return (arr-amin)*255/rng


def compare_images(img1, img2):
    # normalize to compensate for exposure difference, this may be unnecessary
    # consider disabling it
    img1 = normalize(img1)
    img2 = normalize(img2)
    # calculate the difference and its norms
    diff = img1 - img2  # elementwise for scipy arrays
    m_norm = sum(abs(diff))  # Manhattan norm
    z_norm = norm(diff.ravel(), 0)  # Zero norm
    return (m_norm, z_norm)

def main():
    file1, file2 = sys.argv[1:1+2]
    # read images as 2D arrays (convert to grayscale for simplicity)
    img2 = cv2.cvtColor(cv2.resize(cv2.imread(file2),(150,150)), cv2.COLOR_BGR2GRAY)
    img1 = cv2.cvtColor(cv2.resize(cv2.imread(file1), (150,150)), cv2.COLOR_BGR2GRAY)
    # compare
    (score, diff) = ssim(img1, img2, full=True)
    diff = (diff * 255).astype("uint8")
    print("SSIM: {}".format(score))

#    n_m, n_0 = compare_images(img1, img2)
#    print("Manhattan norm:", n_m, "/ per pixel:", n_m/img1.size)
#    print("Zero norm:", n_0, "/ per pixel:", n_0*1.0/img1.size)


if __name__ == "__main__":
    main()
