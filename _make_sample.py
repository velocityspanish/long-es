import os, sys, asyncio, importlib.util, tempfile
os.environ.setdefault("AI_MODEL", "gemini-fast")
os.environ.setdefault("POLLINATIONS_API_KEY", "dummy")

spec = importlib.util.spec_from_file_location('m', os.path.join(os.getcwd(), 'youtube_longform_automation.py'))
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

OUT = tempfile.mkdtemp(prefix="es_sample_")
print("Work dir:", OUT)

# Use the hardcoded, guaranteed-correct Spanish fallback phrases
phrases = m.get_fresh_fallback_phrases("Motivation", 6)
print(f"Using {len(phrases)} fallback Spanish phrases:")
for p in phrases:
    print("  EN:", p['english'], "| ES:", p['spanish'])

# 1) Images (local PIL)
imgs = []
for i, ph in enumerate(phrases):
    ip = os.path.join(OUT, f"phrase_{i:04d}.jpg")
    m.generate_complete_image(ph, "Motivation", ip)
    imgs.append(ip)
print(f"Generated {len(imgs)} images")

# 2) Audio (edge-tts - the part that was broken)
audio_files = m.generate_all_audio(phrases, OUT)
print(f"Generated {len(audio_files)} audio segments")

# 3) Final narration
final = os.path.join(OUT, "narration.mp3")
m.create_final_narration(audio_files, final)

# 4) Video
video = os.path.join(OUT, "spanish_sample.mp4")
m.create_video_from_images_audio(imgs, audio_files, final, video)

import subprocess
def dur(p):
    r = subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","default=noprint_wrappers=1:nokey=1", p], capture_output=True, text=True)
    return r.stdout.strip()

if os.path.exists(video):
    print("VIDEO OK:", video, "duration:", dur(video), "size:", os.path.getsize(video), "bytes")
    # verify it has an audio stream (spanish!)
    r = subprocess.run(["ffprobe","-v","error","-select_streams","a:0","-show_entries","stream=codec_name","-of","default=noprint_wrappers=1", video], capture_output=True, text=True)
    print("Audio stream:", r.stdout.strip() or "NONE")
else:
    print("VIDEO FAILED")
