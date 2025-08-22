import gradio as gr
import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import io
import base64

# Import our algorithms
from algorithms.image_processing import (
    apply_gaussian_blur, apply_median_filter, apply_bilateral_filter,
    apply_sharpening_filter, apply_histogram_equalization, apply_gamma_correction
)
from algorithms.edge_detection import (
    apply_sobel, apply_canny, apply_harris_corner_detection,
    apply_hough_lines, apply_hough_circles
)
from algorithms.feature_detection import (
    apply_sift, apply_surf, apply_orb, apply_brief
)
from algorithms.segmentation import (
    apply_thresholding, apply_watershed, apply_slic_segmentation
)
from algorithms.object_detection import (
    apply_hog_detection, apply_haar_cascade, apply_template_matching
)

def process_image(image, algorithm_type, algorithm_params):
    """
    Main function to process uploaded image with selected algorithm
    """
    if image is None:
        return None, "Please upload an image first."
    
    # Convert PIL image to OpenCV format
    if isinstance(image, np.ndarray):
        img = image
    else:
        img = np.array(image)
    
    # Convert RGB to BGR if needed
    if len(img.shape) == 3 and img.shape[2] == 3:
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    
    try:
        if algorithm_type == "Image Processing":
            result = process_image_processing(img, algorithm_params)
        elif algorithm_type == "Edge Detection":
            result = process_edge_detection(img, algorithm_params)
        elif algorithm_type == "Feature Detection":
            result = process_feature_detection(img, algorithm_params)
        elif algorithm_type == "Segmentation":
            result = process_segmentation(img, algorithm_params)
        elif algorithm_type == "Object Detection":
            result = process_object_detection(img, algorithm_params)
        else:
            return None, "Invalid algorithm type selected."
        
        return result, f"Successfully applied {algorithm_params} algorithm."
    
    except Exception as e:
        return None, f"Error processing image: {str(e)}"

def process_image_processing(img, algorithm):
    """Handle image processing algorithms"""
    if algorithm == "Gaussian Blur":
        return apply_gaussian_blur(img)
    elif algorithm == "Median Filter":
        return apply_median_filter(img)
    elif algorithm == "Bilateral Filter":
        return apply_bilateral_filter(img)
    elif algorithm == "Sharpening":
        return apply_sharpening_filter(img)
    elif algorithm == "Histogram Equalization":
        return apply_histogram_equalization(img)
    elif algorithm == "Gamma Correction":
        return apply_gamma_correction(img)
    else:
        return img

def process_edge_detection(img, algorithm):
    """Handle edge detection algorithms"""
    if algorithm == "Sobel":
        return apply_sobel(img)
    elif algorithm == "Canny":
        return apply_canny(img)
    elif algorithm == "Harris Corner":
        return apply_harris_corner_detection(img)
    elif algorithm == "Hough Lines":
        return apply_hough_lines(img)
    elif algorithm == "Hough Circles":
        return apply_hough_circles(img)
    else:
        return img

def process_feature_detection(img, algorithm):
    """Handle feature detection algorithms"""
    if algorithm == "SIFT":
        return apply_sift(img)
    elif algorithm == "SURF":
        return apply_surf(img)
    elif algorithm == "ORB":
        return apply_orb(img)
    elif algorithm == "BRIEF":
        return apply_brief(img)
    else:
        return img

def process_segmentation(img, algorithm):
    """Handle segmentation algorithms"""
    if algorithm == "Thresholding":
        return apply_thresholding(img)
    elif algorithm == "Watershed":
        return apply_watershed(img)
    elif algorithm == "SLIC":
        return apply_slic_segmentation(img)
    else:
        return img

def process_object_detection(img, algorithm):
    """Handle object detection algorithms"""
    if algorithm == "HOG":
        return apply_hog_detection(img)
    elif algorithm == "Haar Cascade":
        return apply_haar_cascade(img)
    elif algorithm == "Template Matching":
        return apply_template_matching(img)
    else:
        return img

def create_interface():
    """Create the Gradio interface"""
    
    with gr.Blocks(title="Classical Computer Vision Algorithms", theme=gr.themes.Soft()) as demo:
        gr.Markdown("""
        # Classical Computer Vision Algorithms
        
        Upload an image and test various classical computer vision algorithms using the controls below.
        """)
        
        with gr.Row():
            with gr.Column(scale=1):
                # Image upload
                input_image = gr.Image(label="Upload Image", type="pil")
                
                # Algorithm type selection
                algorithm_type = gr.Dropdown(
                    choices=["Image Processing", "Edge Detection", "Feature Detection", "Segmentation", "Object Detection"],
                    label="Algorithm Category",
                    value="Image Processing"
                )
                
                # Algorithm selection based on type
                algorithm_params = gr.Dropdown(
                    choices=["Gaussian Blur", "Median Filter", "Bilateral Filter", "Sharpening", "Histogram Equalization", "Gamma Correction"],
                    label="Algorithm",
                    value="Gaussian Blur"
                )
                
                # Process button
                process_btn = gr.Button("Process Image", variant="primary")
                
                # Status message
                status_msg = gr.Textbox(label="Status", interactive=False)
            
            with gr.Column(scale=1):
                # Output image
                output_image = gr.Image(label="Processed Image")
        
        # Update algorithm choices based on type
        def update_algorithm_choices(algorithm_type):
            if algorithm_type == "Image Processing":
                return gr.Dropdown(choices=["Gaussian Blur", "Median Filter", "Bilateral Filter", "Sharpening", "Histogram Equalization", "Gamma Correction"])
            elif algorithm_type == "Edge Detection":
                return gr.Dropdown(choices=["Sobel", "Canny", "Harris Corner", "Hough Lines", "Hough Circles"])
            elif algorithm_type == "Feature Detection":
                return gr.Dropdown(choices=["SIFT", "SURF", "ORB", "BRIEF"])
            elif algorithm_type == "Segmentation":
                return gr.Dropdown(choices=["Thresholding", "Watershed", "SLIC"])
            elif algorithm_type == "Object Detection":
                return gr.Dropdown(choices=["HOG", "Haar Cascade", "Template Matching"])
            else:
                return gr.Dropdown(choices=[])
        
        algorithm_type.change(
            fn=update_algorithm_choices,
            inputs=[algorithm_type],
            outputs=[algorithm_params]
        )
        
        # Process button click
        process_btn.click(
            fn=process_image,
            inputs=[input_image, algorithm_type, algorithm_params],
            outputs=[output_image, status_msg]
        )
        
        # Footer
        gr.Markdown("""
        ---
        ### Available Algorithms
        
        **Image Processing:**
        - Gaussian Blur: Smooths image using Gaussian kernel
        - Median Filter: Removes salt-and-pepper noise
        - Bilateral Filter: Edge-preserving smoothing
        - Sharpening: Enhances image details
        - Histogram Equalization: Improves contrast
        - Gamma Correction: Adjusts brightness
        
        **Edge Detection:**
        - Sobel: Gradient-based edge detection
        - Canny: Multi-stage edge detection
        - Harris Corner: Corner detection
        - Hough Lines: Line detection
        - Hough Circles: Circle detection
        
        **Feature Detection:**
        - SIFT: Scale-invariant feature transform
        - SURF: Speeded-up robust features
        - ORB: Oriented FAST and rotated BRIEF
        - BRIEF: Binary robust independent elementary features
        
        **Segmentation:**
        - Thresholding: Binary segmentation
        - Watershed: Region-based segmentation
        - SLIC: Superpixel segmentation
        
        **Object Detection:**
        - HOG: Histogram of oriented gradients
        - Haar Cascade: Viola-Jones detection
        - Template Matching: Pattern matching
        """)
    
    return demo

# Create the interface
demo = create_interface()

# Launch for Hugging Face Spaces
if __name__ == "__main__":
    demo.launch() 