from PIL import Image
import io

async def load_image_data(upload_file):

    content = await upload_file.read()

    image = Image.open(io.BytesIO(content))
    
    image = image.convert("RGB")

    return image