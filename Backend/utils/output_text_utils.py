import re

async def parse_makeup_text(description):
    result = {}

    section_pattern = r"(\d+)\.\s*\*\*(.*?)\*\*\s*\n"
    sections = list(re.finditer(section_pattern, description))

    for i, match in enumerate(sections):
        section_index = match.group(1)
        section_title = match.group(2).strip() 
        section_key = f"{section_index}. {section_title}"
        result[section_key] = {}

        start_pos = match.end()
        if i + 1 < len(sections):
            end_pos = sections[i + 1].start()
        else:
            end_pos = len(description)
        section_text = description[start_pos:end_pos]


        sub_section_pattern = r"-\s+\*\*(.*?):\*\*\s*(.*?)(?=\n\s*-\s+\*\*|$)"
        sub_sections = re.findall(sub_section_pattern, section_text, re.DOTALL)


        for key, value in sub_sections:
            result[section_key][key.strip()] = value.strip()

    return result


#description = """
#Okay, I'm ready to analyze the makeup changes between the before and after photos.
#
#1.  **Eyes (Left and Right)**
#    -   **Makeup Description:** There appears to be eyeshadow applied, likely a soft, warm brown, and some eyeliner along the upper lash line on both eyes. There might also be a light coat of mascara to define the lashes.
#    -   **State:** The eyeshadow seems mostly complete on the lids, but is very light and could be extended further. The eyeliner is thin.   
#    -   **Color Description:** The eyeshadow appears to be a light, warm brown (RGB ~180, 140, 110). The eyeliner is likely black or a dark brown.
#    -   **Adjustment Suggestion:** Consider adding a bit more definition to the outer corner of the eye with a slightly darker shade of eyeshadow to add depth.
#
#2.  **Nose**
#    -   **Makeup Description:** Contour makeup is likely applied to the sides of the nose. Additionally, highlighter is likely applied to the bridge.
#    -   **State:** The nose contouring and highlight are applied along the bridge.
#    -   **Color Description:** The contour seems to be a light brown or taupe (RGB ~150, 130, 110), while the highlight looks like a pale ivory (RGB ~240, 230, 210).
#    -   **Adjustment Suggestion:** Blend the contouring slightly more to avoid harsh lines for a more natural look.
#
#3.  **Lips (Upper and Lower)**
#    -   **Makeup Description:** Lipstick or lip tint has been applied to both the upper and lower lips.
#    -   **State:** Lip color appears completely applied.
#    -   **Color Description:** The lip color is a muted, rosy-nude shade (RGB ~190, 150, 130).
#    -   **Adjustment Suggestion:** The application is neat and well-matched to the overall look. No adjustment needed.
#
#4.  **Cheeks (Left and Right)**
#    -   **Makeup Description:** Blush has been applied to the cheeks.
#    -   **State:** Blush is placed high on the cheeks, extending towards the temples.
#    -   **Color Description:** The blush appears to be a soft peach or light coral shade (RGB ~250, 200, 180).
#    -   **Adjustment Suggestion:** Blend the blush slightly more for a softer, more diffused look, especially around the edges, so it looks more natural.
#"""
#

#result_dict = parse_makeup_text(description)
#print(result_dict)
## 
## 