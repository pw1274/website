import re

def replace_domain_and_vid_id(m3u8_content, new_domain):
    # Find and replace all URLs that match the pattern
    def url_replacer(match):
        # Extract the video ID from the matched URL
        video_id = match.group(1)
        quality = match.group(2)
        # Reconstruct the URL with the new domain and same query params
        return f"https://{new_domain}/pw-vid/{video_id}/hls/{quality}/main.m3u8{match.group(3)}"
    
    # Pattern to find URLs in the m3u8 content
    pattern = r'https://tgxapi\.vercel\.app/pw-vid/([a-zA-Z0-9-]+)/hls/([0-9]+)/main\.m3u8(\?.*)'

    # Replace the URLs using the url_replacer function
    new_m3u8_content = re.sub(pattern, url_replacer, m3u8_content)

    return new_m3u8_content

# Original m3u8 content
m3u8_content = """
#EXTM3U
#EXT-X-VERSION:3
#EXT-X-STREAM-INF:BANDWIDTH=279896,RESOLUTION=426x240
https://tgxapi.vercel.app/pw-vid/{video_id}/hls/240/main.m3u8?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9kMWQzNHA4dno2M29pcS5jbG91ZGZyb250Lm5ldC8zMzk0NDk1Zi01NDljLTQyODUtOWQxYS0wMTdmNmY1MzQ3YmEvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTcyODI2NDAxNX19fV19&Key-Pair-Id=APKAJBP3D6S2IU5JK4LQ&Signature=hbusvBjWtHprLhVQT9I-CmGYPRy7STsrJulevMcVjrUDGxKObKm4ssoEHkVhtbM2eNNmv~A~UlXyNW2tAGlusoTrowXqV-U1q4iuviAr5gOvrx1xvTvBRJi8EeAInpIDqSZcoD1~z8asybVC--UWErhfG9KJ-dfO0yYypYI7FkvZODJkGGoFExB7wAj0yP3grr2UXy3~hNCw~CSKEzIAbfxKOSIPquBVa660J3UhMl3MPzb6LYikexijW7RUQOzth5VQlw-Sk7N9Zn3jzHXxUsdUId9-Pcm2KWOULP0~M17~rBWmJOMco1H7x4etjOcWeqOqRpn2nN-5yLbsS5301g__
#EXT-X-STREAM-INF:BANDWIDTH=426723,RESOLUTION=640x360
https://tgxapi.vercel.app/pw-vid/{video_id}/hls/360/main.m3u8?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9kMWQzNHA4dno2M29pcS5jbG91ZGZyb250Lm5ldC8zMzk0NDk1Zi01NDljLTQyODUtOWQxYS0wMTdmNmY1MzQ3YmEvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTcyODI2NDAxNX19fV19&Key-Pair-Id=APKAJBP3D6S2IU5JK4LQ&Signature=hbusvBjWtHprLhVQT9I-CmGYPRy7STsrJulevMcVjrUDGxKObKm4ssoEHkVhtbM2eNNmv~A~UlXyNW2tAGlusoTrowXqV-U1q4iuviAr5gOvrx1xvTvBRJi8EeAInpIDqSZcoD1~z8asybVC--UWErhfG9KJ-dfO0yYypYI7FkvZODJkGGoFExB7wAj0yP3grr2UXy3~hNCw~CSKEzIAbfxKOSIPquBVa660J3UhMl3MPzb6LYikexijW7RUQOzth5VQlw-Sk7N9Zn3jzHXxUsdUId9-Pcm2KWOULP0~M17~rBWmJOMco1H7x4etjOcWeqOqRpn2nN-5yLbsS5301g__
#EXT-X-STREAM-INF:BANDWIDTH=545886,RESOLUTION=854x480
https://tgxapi.vercel.app/pw-vid/{video_id}/hls/480/main.m3u8?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9kMWQzNHA4dno2M29pcS5jbG91ZGZyb250Lm5ldC8zMzk0NDk1Zi01NDljLTQyODUtOWQxYS0wMTdmNmY1MzQ3YmEvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTcyODI2NDAxNX19fV19&Key-Pair-Id=APKAJBP3D6S2IU5JK4LQ&Signature=hbusvBjWtHprLhVQT9I-CmGYPRy7STsrJulevMcVjrUDGxKObKm4ssoEHkVhtbM2eNNmv~A~UlXyNW2tAGlusoTrowXqV-U1q4iuviAr5gOvrx1xvTvBRJi8EeAInpIDqSZcoD1~z8asybVC--UWErhfG9KJ-dfO0yYypYI7FkvZODJkGGoFExB7wAj0yP3grr2UXy3~hNCw~CSKEzIAbfxKOSIPquBVa660J3UhMl3MPzb6LYikexijW7RUQOzth5VQlw-Sk7N9Zn3jzHXxUsdUId9-Pcm2KWOULP0~M17~rBWmJOMco1H7x4etjOcWeqOqRpn2nN-5yLbsS5301g__
#EXT-X-STREAM-INF:BANDWIDTH=1251806,RESOLUTION=1280x720
https://tgxapi.vercel.app/pw-vid/{video_id}/hls/720/main.m3u8?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9kMWQzNHA4dno2M29pcS5jbG91ZGZyb250Lm5ldC8zMzk0NDk1Zi01NDljLTQyODUtOWQxYS0wMTdmNmY1MzQ3YmEvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTcyODI2NDAxNX19fV19&Key-Pair-Id=APKAJBP3D6S2IU5JK4LQ&Signature=hbusvBjWtHprLhVQT9I-CmGYPRy7STsrJulevMcVjrUDGxKObKm4ssoEHkVhtbM2eNNmv~A~UlXyNW2tAGlusoTrowXqV-U1q4iuviAr5gOvrx1xvTvBRJi8EeAInpIDqSZcoD1~z8asybVC--UWErhfG9KJ-dfO0yYypYI7FkvZODJkGGoFExB7wAj0yP3grr2UXy3~hNCw~CSKEzIAbfxKOSIPquBVa660J3UhMl3MPzb6LYikexijW7RUQOzth5VQlw-Sk7N9Zn3jzHXxUsdUId9-Pcm2KWOULP0~M17~rBWmJOMco1H7x4etjOcWeqOqRpn2nN-5yLbsS5301g__
"""

# Replace domain with your desired domain
new_domain = "studybuddyofficial.vercel.app"

# Generate new m3u8 content
new_m3u8_content = replace_domain_and_vid_id(m3u8_content, new_domain)
print(new_m3u8_content)
