import pytesseract as pyt
import cv2
import numpy as np

from PIL import Image


def main() -> None:
    # img: Image = Image.open("/home/rowan/Documents/programming/vimusic_to_apple/Screenshots/Screenshot_20230829-134828.png")
    # img: Image = Image.open("/home/rowan/Documents/programming/vimusic_to_apple/Screenshots/Screenshot_20230829-133442.png")
    # img: Image = Image.open("/home/rowan/Documents/programming/vimusic_to_apple/Screenshots/Screenshot_20230829-134736.png")
    img: Image = Image.open("temp_cap.png")
    boxen_str: str = pyt.image_to_boxes(img)
    # print(boxen_str)

    boxen_list: list[str] = boxen_str.split("\n") # has indicies formatted as 'F 123 234 235 753 0' 

    letters_list: list[str] = []

    for index in boxen_list:
        if not index == '':
            letters_list.append(index[0])

    letters_str: str = "".join(letters_list)

    add_button_index: int = letters_str.find("AddtoaPlaylist")

    _, x1, y1, x2, y2, _ = tuple(boxen_list[add_button_index].split())

    x: int = round((int(x1) + int(x2)) / 2)
    y: int = round((int(y1) + int(y2)) / 2)

    if y == 1122:
        y += 150
    elif y == 860:
        y += 675

    print(f"{x} {y}")

    img_circ = cv2.circle(np.array(img), (x, y), 15, (0,0,255), 4)
    cv2.imwrite("res.jpg",img_circ)

    return


if __name__ == "__main__":
    main()