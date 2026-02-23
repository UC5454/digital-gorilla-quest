#!/usr/bin/env python3
"""Digital Gorilla Quest - キャラクター画像一括生成"""

import os
import sys
import time
from pathlib import Path

try:
    from google import genai
    from google.genai import types
except ImportError:
    print("Error: google-genai not installed. Run: pip install google-genai")
    sys.exit(1)

API_KEY = os.environ.get("GEMINI_API_KEY", "AIzaSyCMWDvpJRjpaW3e7dV1QUNaVYEfIexTbgo")
MODEL_NAME = "gemini-3-pro-image-preview"
BASE_DIR = Path(__file__).parent

STYLE_PREFIX = "Anime style digital illustration with big expressive eyes, colorful and friendly game art style, 16:9 aspect ratio, high quality, detailed, vibrant colors. "

EVOLUTION_IMAGES = [
    ("evolution/child_gorilla.png", "A small cute baby gorilla with very large curious eyes, playful expression, sitting on digital green grassland with pixel-like grass particles floating, soft sunlight, adorable and innocent"),
    ("evolution/young_gorilla.png", "A young teenage gorilla with slightly muscular build, growing confident expression, standing in a lush forest with tall trees, dappled sunlight through leaves, energetic pose"),
    ("evolution/mature_gorilla.png", "A mature powerful gorilla with strong muscular body, fierce determined eyes, standing on a mountain peak with rocky terrain, wind blowing, dramatic sky"),
    ("evolution/blackback.png", "A blackback gorilla with shining black fur, arms crossed confidently, standing in a dark cave with lightning bolts crackling around, electric blue and purple energy effects"),
    ("evolution/silverback.png", "A majestic silverback gorilla with gleaming silver back fur, regal dignified pose, standing in an ancient golden temple with light aura radiating, divine atmosphere"),
    ("evolution/jungle_king.png", "A gorilla king wearing a golden crown, surrounded by golden aura and royal energy, sitting on a throne in a fortress, red cape flowing, commanding presence"),
    ("evolution/legendary_kingkong.png", "A legendary colossal King Kong gorilla engulfed in flame aura, standing on the highest peak looking down over a vast jungle, epic scale, mythical golden fire effects, ultimate power"),
]

BOSS_IMAGES = [
    ("bosses/boss_gatekeeper.png", "A gatekeeper gorilla guard in green armor, holding a shield and spear, standing at a grassland gate entrance, stern protective expression, guardian warrior"),
    ("bosses/boss_sage.png", "A wise old gorilla sage with long white beard, holding a glowing staff, sitting under a massive ancient tree in a forest, wisdom light emanating, scholarly robes"),
    ("bosses/boss_warrior.png", "A martial artist gorilla in a torn training gi/karate uniform, fighting stance, in a mountain dojo with wooden training posts, intense focused expression"),
    ("bosses/boss_mage.png", "A sorcerer gorilla wearing magical dark robes with mystical runes, floating magic circles around hands, deep cave background with purple magical light"),
    ("bosses/boss_priest.png", "A priest gorilla in white and gold temple vestments, holding a staff of light, standing in a temple with beautiful stained glass windows, holy radiance"),
    ("bosses/boss_medium.png", "A spirit medium gorilla with semi-transparent glowing aura, floating runic letters orbiting around, at a mystical altar with blue ethereal flames"),
    ("bosses/boss_general.png", "A samurai general gorilla in full Japanese-style armor and helmet, wielding a katana sword, standing on fortress castle walls, commanding warrior pose"),
    ("bosses/boss_dragon.png", "A dragon gorilla with massive dragon wings and fire breath, standing on a volcano peak with lava flowing below, scales and horns, fearsome hybrid creature"),
    ("bosses/boss_kingkong.png", "The ultimate King Kong boss, the largest of all bosses, enormous muscular body, thunder clouds and lightning surrounding, sitting on a throne at the absolute summit, final boss energy"),
]

def generate_image(client, prompt, output_path):
    """Generate a single image and save it."""
    full_prompt = STYLE_PREFIX + prompt
    print(f"  Generating: {output_path.name}...")

    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=full_prompt,
            config=types.GenerateContentConfig(
                response_modalities=['IMAGE']
            )
        )

        for part in response.parts:
            if part.inline_data is not None:
                image = part.as_image()
                output_path.parent.mkdir(parents=True, exist_ok=True)
                image.save(str(output_path))
                print(f"  OK: {output_path}")
                return True

        print(f"  WARN: No image data in response for {output_path.name}")
        return False

    except Exception as e:
        print(f"  ERROR: {output_path.name} - {e}")
        return False


def main():
    client = genai.Client(api_key=API_KEY)

    all_images = EVOLUTION_IMAGES + BOSS_IMAGES
    success = 0
    failed = 0

    print(f"=== Digital Gorilla Quest Image Generation ===")
    print(f"Total images to generate: {len(all_images)}")
    print()

    for rel_path, prompt in all_images:
        output_path = BASE_DIR / rel_path

        if output_path.exists():
            print(f"  SKIP (exists): {rel_path}")
            success += 1
            continue

        ok = generate_image(client, prompt, output_path)
        if ok:
            success += 1
        else:
            failed += 1

        # Rate limiting
        time.sleep(2)

    print()
    print(f"=== Done: {success} success, {failed} failed out of {len(all_images)} ===")


if __name__ == "__main__":
    main()
