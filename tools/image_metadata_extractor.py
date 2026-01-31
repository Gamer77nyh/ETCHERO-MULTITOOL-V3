import sys
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
import os

def get_exif_data(image_path):
    try:
        image = Image.open(image_path)
        exif_data = image._getexif()
        
        if not exif_data:
            print("[-] No EXIF metadata found in this image.")
            return

        print(f"\n=== Metadata for {os.path.basename(image_path)} ===\n")

        for tag_id, value in exif_data.items():
            tag_name = TAGS.get(tag_id, tag_id)
            
            # Skip long binary data
            if isinstance(value, bytes) and len(value) > 50:
                value = f"[Binary data: {len(value)} bytes]"
            
            print(f"{tag_name:<25}: {value}")
            
    except IOError:
        print("[-] Error: Could not open image file. Make sure it's a valid image.")
    except Exception as e:
        print(f"[-] An error occurred: {e}")

def main():
    print("\n=== Image Metadata (Exif) Extractor ===")
    print("Supports: .jpg, .jpeg, .tiff (PNG metadata is often stored differently)")
    
    path = input("\nEnter path to image file: ").strip().strip('"')
    
    if os.path.exists(path):
        get_exif_data(path)
    else:
        print("[-] File does not exist.")

if __name__ == "__main__":
    main()
    input("\nPress Enter to return to menu...")
