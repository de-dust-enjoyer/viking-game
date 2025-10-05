from PIL import Image
import os


def slice_spritesheet(input_path, frame_width, frame_height, animations, output_dir="sliced_animations"):
    """
    Slice a spritesheet into separate images for each animation.

    Args:
        input_path: Path to the spritesheet image
        frame_width: Width of each frame in pixels
        frame_height: Height of each frame in pixels
        animations: Dict mapping animation names to (row, num_frames)
                   Example: {"idle": (0, 4), "run": (1, 8), "jump": (2, 6)}
        output_dir: Directory to save sliced animations
    """
    # Load spritesheet
    sheet = Image.open(input_path)

    # Create output directory
    os.makedirs(output_dir, exist_ok=True)

    # Process each animation
    for anim_name, (row, num_frames) in animations.items():
        frames = []

        # Extract each frame
        for col in range(num_frames):
            x = col * frame_width
            y = row * frame_height

            # Crop frame from spritesheet
            frame = sheet.crop((x, y, x + frame_width, y + frame_height))
            frames.append(frame)

        # Create output image with all frames in a row
        output_width = frame_width * num_frames
        output_img = Image.new("RGBA", (output_width, frame_height))

        # Paste frames
        for i, frame in enumerate(frames):
            output_img.paste(frame, (i * frame_width, 0))

        # Save
        output_path = os.path.join(output_dir, f"{anim_name}.png")
        output_img.save(output_path)
        print(f"Saved {anim_name} animation: {num_frames} frames -> {output_path}")


# Example usage:
# Configure your spritesheet here


def slice_spritesheets_in_folder(folder):
    animations = {
        "idle_down": (0, 6),  # Row 0, 4 frames
        "idle_side": (1, 6),  # Row 1, 8 frames
        "idle_up": (2, 6),  # Row 2, 8 frames
        "walk_down": (3, 6),  # Row 3, 6 frames
        "walk_side": (4, 6),  # Row 4, 5 frames
        "walk_up": (5, 6),
        "attack_0_down": (6, 4),
        "attack_1_down": (7, 4),
        "attack_2_down": (8, 4),
        "attack_0_side": (9, 4),
        "attack_1_side": (10, 4),
        "attack_2_side": (11, 4),
        "attack_0_up": (12, 4),
        "attack_1_up": (13, 4),
        "attack_2_up": (14, 4),
        "die": (15, 4),
        "hit_down": (20, 1),
        "hit_side": (21, 1),
        "hit_up": (22, 1),
    }
    for dir in os.walk(folder):
        for image in dir[2]:
            input_path = dir[0] + "/" + image
            output_dir = dir[0]

            slice_spritesheet(
                input_path=input_path,
                frame_width=64,  # Adjust to your frame size
                frame_height=64,  # Adjust to your frame size
                animations=animations,
                output_dir=output_dir,
            )


def delete_generated_imgs(folder):
    """DO NOT USE!!! DELETES EVERYTHING!!!"""
    for dir in os.walk(folder):
        for image in dir[2]:
            input_path = dir[0] + "/" + image

            os.remove(input_path)
