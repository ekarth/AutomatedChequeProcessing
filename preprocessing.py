import numpy as np
import cv2
import os


def find_rotation_of_cheque(img):
    #   img_edges = cv2.Canny(img, 100, 100, apertureSize= 3)
    #   lines = cv2.HoughLinesP(img_edges, 1, math.pi / 180.0, 100, minLineLength=100, maxLineGap=5)
    #   angles = []

    #   for [[x1, y1, x2, y2]] in lines:
    #     cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 3)
    #     angle = math.degrees(math.atan2(y2 - y1, x2 - x1))
    #     angles.append(angle)

    #   median_angle = np.median(angles)
    #   print(median_angle)
    #   img_rotated = ndimage.rotate(img, median_angle)

    #   return img_rotated
    pass


def extract_maximum_contour(img):
    contours, _ = cv2.findContours(
        img.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    max_countour = sorted(contours, key=cv2.contourArea)[-1]
    x, y, w, h = cv2.boundingRect(max_countour)
    return img[y: y+h, x: x+w]



def extract_cheque_features(file_path):
    upload_folder_path = os.path.join(os.getcwd(), 'upload')

    file_name = (file_path.split('\\')[-1]).split('.')[0]

    #Reading image
    cheque_image = cv2.imread(file_path)

    # Resizing image 
    cheque_image = cv2.resize(cheque_image, (1376, 768))

    # Changing image to grayscale
    cheque_image_grey = cv2.cvtColor(cheque_image, cv2.COLOR_BGR2GRAY)
    
    # Applying Gaussian Blur to remove noise from the image
    cheque_image_blur = cv2.GaussianBlur(cheque_image_grey, (3, 3), cv2.BORDER_DEFAULT)
    
    # Convert the blurred image to binary image
    cheque_image_threshold = cv2.adaptiveThreshold(cheque_image_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 7, 20)
    
    # Dividing cheque into two parts: part with micr and part without micr code
    cheque_image_upper = cheque_image_threshold[: 644, ]
    cheque_image_lower = cheque_image_threshold[644:, ]
    
    # Extracting potential images to be used as features using image segmentation
    cheque_date_roi = cheque_image_upper[50: 136, 980: 1350]
    cheque_number_roi = cheque_image_lower[20: 100, 250: 535]
    account_number_roi = cheque_image_upper[360: 450, 200: 700]
    cheque_amount_digits_roi = cheque_image_upper[278: 380, 977: 1332]
    cheque_amount_words_roi = cheque_image_upper[220: 295, : 1330]
    cheque_amount_words_roi_2 = cheque_image_upper[295: 360, : 950]
    account_holder_signature_roi = cheque_image_upper[413: 605, 950: 1330]
    
    # Cheque Date
    cheque_date = cv2.resize(extract_maximum_contour(cheque_date_roi), (264, 40))
    width = cheque_date.shape[1]
    
    for col in range(0, width, width//8):
        cv2.line(cheque_date, (col-1, 0), (col-1, 40), (0, 0, 0), 3)

    cv2.imwrite(os.path.join(upload_folder_path, (file_name + "_date.jpg")), cheque_date)
    
    # Cheque Number
    cheque_number = cheque_number_roi
    cv2.imwrite(os.path.join(upload_folder_path, (file_name + "_cheque_num.jpg")), cheque_number)
    
    # Account Number
    account_number = extract_maximum_contour(account_number_roi)
    cv2.imwrite(os.path.join(upload_folder_path, (file_name + "_account_num.jpg")), account_number)
    
    # Cheque Figure
    cheque_amount_digits = cheque_amount_digits_roi
    cv2.imwrite(os.path.join(upload_folder_path, (file_name + "_figure.jpg")), cheque_amount_digits)

    # Cheque Amount
    v = np.zeros(cheque_amount_words_roi.shape)
    v[: cheque_amount_words_roi_2.shape[0], : cheque_amount_words_roi_2.shape[1]] = cheque_amount_words_roi_2
    cheque_amount = np.vstack((cheque_amount_words_roi, v))

    cv2.imwrite(os.path.join(upload_folder_path, (file_name + "_amount_in_words.jpg")), cheque_amount)
    
    # Account Holder Signature 
    cv2.imwrite(os.path.join(upload_folder_path, (file_name + "_sign.jpg")), account_holder_signature_roi)

# extract_cheque_features('D:\Projects\AutomatedChequeProcessing\Cheque100828.jpg')