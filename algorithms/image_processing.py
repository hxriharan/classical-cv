import cv2
import numpy as np
from PIL import Image

def apply_gaussian_blur(img, kernel_size=(5, 5), sigma=1.0):
    """
    Apply Gaussian blur to the image
    
    Args:
        img: Input image (BGR format)
        kernel_size: Size of Gaussian kernel (width, height)
        sigma: Standard deviation of Gaussian kernel
    
    Returns:
        Blurred image
    """
    return cv2.GaussianBlur(img, kernel_size, sigma)

def apply_median_filter(img, kernel_size=5):
    """
    Apply median filter to remove salt-and-pepper noise
    
    Args:
        img: Input image (BGR format)
        kernel_size: Size of median filter kernel
    
    Returns:
        Filtered image
    """
    return cv2.medianBlur(img, kernel_size)

def apply_bilateral_filter(img, d=15, sigma_color=75, sigma_space=75):
    """
    Apply bilateral filter for edge-preserving smoothing
    
    Args:
        img: Input image (BGR format)
        d: Diameter of each pixel neighborhood
        sigma_color: Filter sigma in the color space
        sigma_space: Filter sigma in the coordinate space
    
    Returns:
        Filtered image
    """
    return cv2.bilateralFilter(img, d, sigma_color, sigma_space)

def apply_sharpening_filter(img, kernel_type='laplacian'):
    """
    Apply sharpening filter to enhance image details
    
    Args:
        img: Input image (BGR format)
        kernel_type: Type of sharpening kernel ('laplacian' or 'unsharp')
    
    Returns:
        Sharpened image
    """
    if kernel_type == 'laplacian':
        # Laplacian sharpening
        kernel = np.array([[-1, -1, -1],
                          [-1,  9, -1],
                          [-1, -1, -1]])
        return cv2.filter2D(img, -1, kernel)
    
    elif kernel_type == 'unsharp':
        # Unsharp masking
        blurred = cv2.GaussianBlur(img, (0, 0), 2.0)
        sharpened = cv2.addWeighted(img, 1.5, blurred, -0.5, 0)
        return np.clip(sharpened, 0, 255).astype(np.uint8)
    
    else:
        return img

def apply_histogram_equalization(img):
    """
    Apply histogram equalization to improve contrast
    
    Args:
        img: Input image (BGR format)
    
    Returns:
        Image with improved contrast
    """
    # Convert to YUV for better histogram equalization
    img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
    
    # Apply histogram equalization to Y channel
    img_yuv[:,:,0] = cv2.equalizeHist(img_yuv[:,:,0])
    
    # Convert back to BGR
    return cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)

def apply_gamma_correction(img, gamma=1.0):
    """
    Apply gamma correction to adjust brightness
    
    Args:
        img: Input image (BGR format)
        gamma: Gamma value (gamma < 1 brightens, gamma > 1 darkens)
    
    Returns:
        Gamma-corrected image
    """
    # Build lookup table
    invGamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** invGamma) * 255
                      for i in np.arange(0, 256)]).astype("uint8")
    
    # Apply gamma correction using lookup table
    return cv2.LUT(img, table) 