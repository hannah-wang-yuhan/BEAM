import tempfile
from google import genai
from google.genai import types
from PIL import Image
import io

def pil_to_bytes(image: Image.Image, format='JPEG') -> bytes:
    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format=format)
    return img_byte_arr.getvalue()

async def analyze_facial_makeup(before_img: Image.Image, after_img: Image.Image):

    try:
        client = genai.Client(api_key="your-own-api")

        prompt = """
You are a professional makeup analyst. Given a before-makeup and an after-makeup face photo, 
please identify and analyze the changes in makeup in the following areas:

1. Eyes (left and right)
2. Nose
3. Lips (upper and lower)
4. Cheeks (left and right)

For each facial part:
- Describe the makeup applied (e.g., eyeshadow color, lipstick tone, blush type)
- Comment on the completeness (any uncovered parts?), uniformity (blending & texture), 
  boundary overflow (color outside the natural facial zone), and color match (aesthetic compatibility).
- Give one short improvement suggestion if necessary.

Please output the result in the following textual format. Use clear bold titles for each facial part:

1.  **[Facial Part Name]**  
    -   **Makeup Description:** ...  
    -   **State:** ...  
    -   **Color Description:** ...  
    -   **Adjustment Suggestion:** ...  


Use clear and concise language suitable for a blind user using TTS. When possible, include both a human-friendly color description and a rough RGB estimate. Suggestions should be specific and actionable.

"""

        before_bytes = pil_to_bytes(before_img, format='JPEG')
        with tempfile.NamedTemporaryFile(suffix='.jpg', delete=False) as tmp_before:
            tmp_before.write(before_bytes)
            tmp_before_path = tmp_before.name
        uploaded_file = client.files.upload(file=tmp_before_path)

        after_bytes = pil_to_bytes(after_img, format='JPEG')

        response = client.models.generate_content(
            model='gemini-2.0-flash',
            contents=[
                prompt,
                uploaded_file,
                types.Part.from_bytes(data=after_bytes, mime_type='image/jpeg')
            ]
        )

        return response.text

    except Exception as e:
        return f"Error during image analysis: {str(e)}"
