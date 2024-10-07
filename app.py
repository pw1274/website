import re

def replace_domain_and_vid_id(m3u8_content, new_domain):
    # Video ID ko find karna
    matches = re.findall(r'/([a-zA-Z0-9-]+)/hls', m3u8_content)

    if matches:
        video_id = matches[0]  # Pehla video ID extract karenge
        print(f"Extracted video ID: {video_id}")
    else:
        print("No video ID found in the m3u8 content.")
        return None

    # URL template jo tumne di hai usko modify karna
    url_template = f"https://{new_domain}/pw-vid/{video_id}/hls/240/main.m3u8"

    # Replace domain aur video ID purani URL mein nayi URL lagana
    new_m3u8_content = re.sub(r'https://tgxapi\.vercel\.app/pw-vid/[a-zA-Z0-9-]+/hls/240/main.m3u8', 
                              url_template, 
                              m3u8_content)

    return new_m3u8_content

# Original m3u8 content (jisme URLs hain)
m3u8_content = """
#EXTM3U
#EXT-X-VERSION:3
#EXT-X-STREAM-INF:BANDWIDTH=279896,RESOLUTION=426x240
https://tgxapi.vercel.app/pw-vid/{vid-id}/hls/240/main.m3u8?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9kMWQzNHA4dno2M29pcS5jbG91ZGZyb250Lm5ldC8zMzk0NDk1Zi01NDljLTQyODUtOWQxYS0wMTdmNmY1MzQ3YmEvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTcyODI2NDAxNX19fV19&Key-Pair-Id=APKAJBP3D6S2IU5JK4LQ&Signature=hbusvBjWtHprLhVQT9I-CmGYPRy7STsrJulevMcVjrUDGxKObKm4ssoEHkVhtbM2eNNmv~A~UlXyNW2tAGlusoTrowXqV-U1q4iuviAr5gOvrx1xvTvBRJi8EeAInpIDqSZcoD1~z8asybVC--UWErhfG9KJ-dfO0yYypYI7FkvZODJkGGoFExB7wAj0yP3grr2UXy3~hNCw~CSKEzIAbfxKOSIPquBVa660J3UhMl3MPzb6LYikexijW7RUQOzth5VQlw-Sk7N9Zn3jzHXxUsdUId9-Pcm2KWOULP0~M17~rBWmJOMco1H7x4etjOcWeqOqRpn2nN-5yLbsS5301g__
"""

# Replace domain with tumhara desired domain
new_domain = "studybuddyofficial.vercel.app"

# Nayi m3u8 content generate karo
new_m3u8_content = replace_domain_and_vid_id(m3u8_content, new_domain)
print(new_m3u8_content)
