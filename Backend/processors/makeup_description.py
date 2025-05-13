from google.genai import types
from google import genai
import io

async def makeup_description(image):
    caption= """"
You are a professional makeup analyst. Given an after-makeup face photo,
please identify and check the makeup in the following steps:

1. Base Makeup Check
2. Blush Check
3. Overall Color Matching Check

For each step:
- Makeup Description: Describe the makeup applied (e.g., foundation type, blush used, application method).
- State: Comment on the completeness (any uncovered areas?), uniformity (blending and texture), boundary overflow (color outside the natural facial zone?), and color match (aesthetic compatibility).
- Color Description: Provide a user-friendly color description (e.g., warm beige, soft pink) and a rough RGB estimate where possible (e.g., "RGB: 255, 220, 200").
- Adjustment Suggestion: If necessary, provide a brief improvement suggestion (e.g., "Blend the foundation more evenly," "Try a lighter blush tone," "Consider matching the lip color with the blush").

Please output the result in the following textual format. Use clear bold titles for each step:

1.  **[Step Name]**  
    -   **Makeup Description:** ...  
    -   **State:** ...  
    -   **Color Description:** ...  
    -   **Adjustment Suggestion:** ...  


Use clear and concise language suitable for a blind user using TTS. When possible, include both a human-friendly color description and a rough RGB estimate. Suggestions should be specific and actionable.

"""

    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format='JPEG')
    img_byte_arr = img_byte_arr.getvalue()

    client = genai.Client(api_key="AIzaSyCrfmrq2SU-9BJEAU40xwpQ6j_3qskzqds")

    try:
        response = client.models.generate_content(
            model='gemini-2.0-flash',  
            contents=[
                types.Part.from_bytes(
                    data=img_byte_arr,  
                    mime_type='image/jpeg',
                ),
                caption
            ]
        )

        return response.text
    except Exception as e:
        print(f"Error while calling GenAI API: {str(e)}")
        return {"error": "无法生成描述，请稍后再试"}