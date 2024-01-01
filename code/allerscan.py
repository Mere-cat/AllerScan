from PIL import Image
import pytesseract
import pandas as pd
import os

if __name__ == "__main__":
    # User Input
    label_path = input("Please input the path of the image of the cosmetic ingredient list：")

    # Read file
    df = pd.read_csv('database.csv', quotechar='"')
    img = Image.open(label_path)
    text = pytesseract.image_to_string(img, lang='chi_tra')

    # Calculate
    df['result'] = df['Allergen'].apply(lambda x: x in text)
    count = 0

    # Print the result
    for index, row in df.iterrows():
        if row['result'] == True:
            print("Allergen Found:", row['Allergen'])
            print("Function of the allergen:", row['Function'])
            count = count + 1
            print("===================================")

    df.to_csv('output.csv', index=False)
    output_path = os.path.join(os.getcwd(), 'output.csv')

    print("Total Allergen Count:", count)
    print("Full result saved in:", output_path)