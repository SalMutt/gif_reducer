from PIL import Image
import os
import sys

def make_gif_smaller(input_file, output_file, wanted_size=128):
    # Open the GIF file
    img = Image.open(input_file)
    
    # Starting values
    quality = 95
    num_colors = 256
    size_percent = 1.0
    
    # Get starting file size in KB
    start_size = os.path.getsize(input_file) / 1024
    print(f"Starting size: {start_size:.2f}KB")
    
    # Calculate starting scale based on how big the file is
    size_percent = min(1.0, (wanted_size / start_size) ** 0.5)
    
    while True:
        # Make a temporary file
        temp_file = output_file + '.temp.gif'
        
        # Get all the frames
        all_frames = []
        try:
            frame_number = 0
            while True:
                img.seek(frame_number)
                current_frame = img.copy()
                
                # Make the image smaller if needed
                if size_percent < 1.0:
                    new_width = max(int(current_frame.width * size_percent), 1)
                    new_height = max(int(current_frame.height * size_percent), 1)
                    current_frame = current_frame.resize((new_width, new_height))
                
                all_frames.append(current_frame)
                frame_number += 1
        except EOFError:
            pass  # We've gotten all the frames
        
        # Make each frame smaller
        smaller_frames = []
        for frame in all_frames:
            if frame.mode != 'P':
                frame = frame.convert('P', palette=Image.ADAPTIVE, colors=num_colors)
            smaller_frames.append(frame)
        
        # Save the new GIF
        smaller_frames[0].save(
            temp_file,
            save_all=True,
            append_images=smaller_frames[1:],
            optimize=True,
            quality=quality,
            duration=img.info.get('duration', 100),
            loop=img.info.get('loop', 0)
        )
        
        # Check how big it is now
        current_size = os.path.getsize(temp_file) / 1024
        print(f"Current size: {current_size:.2f}KB (Quality: {quality}, Colors: {num_colors}, Scale: {size_percent:.3f})")
        
        if current_size <= wanted_size:
            # We made it small enough!
            img.close()
            if os.path.exists(output_file):
                os.remove(output_file)
            os.rename(temp_file, output_file)
            return True
        
        # If it's still too big, try making it smaller
        if size_percent > 0.2:  # Don't make it too tiny
            if current_size > wanted_size * 2:
                # Way too big, make it smaller faster
                size_percent *= 0.85
            else:
                # Getting closer, make it smaller slowly
                size_percent *= 0.95
        elif num_colors > 32:
            num_colors = int(num_colors * 0.9)  # Use fewer colors
        elif quality > 60:
            quality -= 5  # Lower the quality a bit
        else:
            # Can't make it any smaller
            break
            
        # Clean up the temporary file
        if os.path.exists(temp_file):
            os.remove(temp_file)
    
    # If we got here, we couldn't make it small enough
    if os.path.exists(output_file):
        os.remove(output_file)
    os.rename(temp_file, output_file)
    return False

def main():
    # Check if we got enough information to run
    if len(sys.argv) < 3:
        print("How to use: python gif_reducer.py input.gif output.gif [size_in_kb]")
        return
    
    # Get the file names and size from command line
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    wanted_size = int(sys.argv[3]) if len(sys.argv) > 3 else 128
    
    # Make sure the input file exists
    if not os.path.exists(input_file):
        print(f"Can't find the file: {input_file}")
        return
    
    print(f"Making GIF smaller to {wanted_size}KB...")
    success = make_gif_smaller(input_file, output_file, wanted_size)
    
    if success:
        final_size = os.path.getsize(output_file) / 1024
        print(f"Done! Final size: {final_size:.2f}KB")
    else:
        print("Finished but couldn't make it as small as wanted.")

# Run the program
if __name__ == "__main__":
    main()