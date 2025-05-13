from utils.image_utils import load_image_data
from utils.output_text_utils import parse_makeup_text
from processors.makeup_description import makeup_description
from processors.quality_evaluation import analyze_facial_makeup

async def dispatch(no_makeup_file, makeup_file, style_description: str):

    before_img = await load_image_data(no_makeup_file)
    after_img = await load_image_data(makeup_file)


    results = {}

    makeup_desc1 = await makeup_description(after_img) 
    # print(makeup_desc1)
    results["makeup_description"] = await parse_makeup_text(makeup_desc1)


    makeup_desc2 = await analyze_facial_makeup(before_img, after_img)
    # print(makeup_desc2)
    results["analyze_facial_makeup"] =  await parse_makeup_text(makeup_desc2)


    # results["quality_score"] = score_makeup_quality(before_img, after_img)

    return results

