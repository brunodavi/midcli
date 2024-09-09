import shutil
from pathlib import Path
from gradio_client import Client


def image_generator(prompt: str, style = 'Anime', filename = 'image', image_dir = '.'):
    client = Client("mukaist/Midjourney")

    [images, _] = client.predict(
		prompt=prompt,
		negative_prompt="(deformed iris, deformed pupils, semi-realistic, cgi, 3d, render, sketch, cartoon, drawing, anime:1.4), text, close up, cropped, out of frame, worst quality, low quality, jpeg artifacts, ugly, duplicate, morbid, mutilated, extra fingers, mutated hands, poorly drawn hands, poorly drawn face, mutation, deformed, blurry, dehydrated, bad anatomy, bad proportions, extra limbs, cloned face, disfigured, gross proportions, malformed limbs, missing arms, missing legs, extra arms, extra legs, fused fingers, too many fingers, long neck",
		use_negative_prompt=True,
		style=style,
		seed=0,
		width=1024,
		height=1024,
		guidance_scale=6,
		randomize_seed=True,
		api_name="/run"
	)

    for number, img in enumerate(images, start=1):
	    source = Path(img['image'])
	    dest = Path(f'{image_dir}/{filename}{number}.png')

	    shutil.copy(source, dest)
