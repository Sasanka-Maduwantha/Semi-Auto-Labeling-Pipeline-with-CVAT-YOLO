import os
from ultralytics import YOLO

# --- Configuration ---
# Set the path to the folder that contains your images (e.g., the folder with your 'ishara3' directory)
IMAGES_BASE_FOLDER = 'drive/MyDrive/A2/DATA2/test'

# Set the name of your custom subfolder (e.g., 'ishara3').
# If you don't have a subfolder, just leave this as an empty string.
CUSTOM_SUBFOLDER = ''

# Set the path to your trained YOLO model file (e.g., yolov8n.pt or best.pt)
MODEL_PATH = 'drive/MyDrive/A2/best_v2.pt'

# Set the path where the annotation files will be saved
OUTPUT_LABELS_FOLDER = 'drive/MyDrive/A2/DATA2/output'

# --- Script ---
def get_image_paths(base_path, subfolder):
    """
    Finds all image files in a specified directory, optionally in a subfolder.
    """
    if subfolder:
        image_dir = os.path.join(base_path, subfolder)
    else:
        image_dir = base_path

    if not os.path.exists(image_dir):
        print(f"Error: The directory '{image_dir}' does not exist.")
        return []

    # Get a list of all image paths
    image_paths = [os.path.join(image_dir, f) for f in os.listdir(image_dir) if f.lower().endswith('.png')]
    return image_paths

def main():
    """Main function to run the complete annotation process."""

    # Step 1: Get the list of image files to process
    print("Step 1: Finding image files...")
    images_to_process = get_image_paths(IMAGES_BASE_FOLDER, CUSTOM_SUBFOLDER)

    if not images_to_process:
        print("No image files found. Exiting.")
        return

    print(f"Found {len(images_to_process)} images to process.")

    # Step 2: Load the YOLO model
    print("Step 2: Loading the YOLO model...")
    try:
        model = YOLO(MODEL_PATH)
    except Exception as e:
        print(f"Error loading model: {e}")
        return

    # Step 3: Run prediction and save annotations
    print("Step 3: Running predictions and saving annotations locally...")

    # The 'predict' method takes the folder directly and saves the .txt files automatically
    model.predict(
        source=os.path.join(IMAGES_BASE_FOLDER, CUSTOM_SUBFOLDER) if CUSTOM_SUBFOLDER else IMAGES_BASE_FOLDER,
        save_txt=True,
        project=OUTPUT_LABELS_FOLDER,
        name='',  # This ensures the output folder is exactly the one you specified
    )

    print("\nProcess complete.")
    print(f"The YOLO-formatted annotation files are located at: {OUTPUT_LABELS_FOLDER}")

if __name__ == '__main__':
    main()
