from google import genai

client = genai.Client(api_key="your_api") # AIzaSyCrfmrq2SU-9BJEAU40xwpQ6j_3qskzqds

myfile = client.files.upload(file="./static/test_img/bad_makeup.jpg")

prompt = """
  Give the segmentation masks for the eyebrows, eyes, nose, and mouth.
  Output a JSON list of segmentation masks where each entry contains the 2D
  bounding box in the key "box_2d", the segmentation mask in key "mask", and
  the text label in the key "label". Use descriptive labels for each facial feature:
  "eyebrows", "eyes", "nose", and "mouth".
"""

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=[myfile, prompt])

print(response.text)
