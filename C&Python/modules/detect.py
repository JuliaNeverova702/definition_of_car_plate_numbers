import easyocr
import os
import cv2

def text_recognition(file_path):
    reader = easyocr.Reader(["en"])
    label=['A', 'B', 'E', 'K', 'M', 'H', 'O', 'P', 'C', 'T', 'Y', 'X', 'Y', 'K', 
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    result = reader.readtext(file_path, batch_size=1, workers=2, allowlist=label) # увеличить batch_size и workers для ускорения
    number = result[0][1]
    occuracy = result[0][2]

    return [number, occuracy]

def change_img(file_path):
    img = cv2.imread(file_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    bfilter = cv2.bilateralFilter(gray, 11, 11, 11)
    edged = cv2.Canny(bfilter, 30, 200)
    saving_the_modif_img(file_path, edged)


def saving_the_modif_img(file_path, img):
    try:
        cv2.imwrite(file_path, img)
        print(f"{file_path} saved")
    except:
        print(f"{file_path} not saved")


def read_jpg(folder_path):
    dataset_list = os.listdir(folder_path)
    with open('result.txt', 'w') as file:
        pass
    for jpg in dataset_list:
        change_img(folder_path + '/' + jpg)
        res = text_recognition(folder_path + '/' + jpg)
        res.append(jpg)
        writing_in_files(res)


def writing_in_files(res):
    with open('result.txt', 'a+') as file:
        file.write("{} {} {}\n".format(*res))


def main():
    read_jpg('../dataset')
    # change_img('../test/number.jpg')


if __name__ == "__main__":
    main()