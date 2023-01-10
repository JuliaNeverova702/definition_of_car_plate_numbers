import easyocr
import os
import cv2


def text_recognition(file_path):
    reader = easyocr.Reader(["en"])
    label=['A', 'B', 'E', 'K', 'M', 'H', 'O', 'P', 'C', 'T', 'Y', 'X', 'Y', 'K', 
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    result = reader.readtext(file_path, batch_size=1, workers=2, allowlist=label) # увеличить batch_size и workers для ускорения
    if not result:
        return [0, 0]
    else:
        number = result[0][1]
        occuracy = result[0][2]

    return [number, occuracy]
    # return result


def modif_img(file_path):
    img = cv2.imread(file_path)
    bfilter = cv2.bilateralFilter(img, 11, 11, 11)
    edged = cv2.Canny(bfilter, 30, 200)
    save_the_modif_img(file_path, edged)


def save_the_modif_img(file_path, img):
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
        modif_img(folder_path + '/' + jpg)
        res = text_recognition(folder_path + '/' + jpg)
        res.append(jpg)
        writing_in_files(res)

        # print(f"{text_recognition(folder_path + '/' + jpg)}")


def writing_in_files(res):
    with open('result.txt', 'a+') as file:
        file.write("{} {} {}\n".format(*res))


def main():
    read_jpg('../dataset')
    # change_img('../test/number.jpg')
    # print(f"{text_recognition('../dataset/01122022_125355.jpg')}")


if __name__ == "__main__":
    main()
