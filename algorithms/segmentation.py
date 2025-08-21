import cv2
import numpy as np
from skimage import segmentation, color

def apply_thresholding(img, threshold_type='otsu'):
    """
    Apply thresholding for image segmentation
    
    Args:
        img: Input image (BGR format)
        threshold_type: Type of thresholding ('otsu', 'adaptive', 'binary')
    
    Returns:
        Thresholded image
    """
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    if threshold_type == 'otsu':
        # Otsu's thresholding
        _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    elif threshold_type == 'adaptive':
        # Adaptive thresholding
        thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                     cv2.THRESH_BINARY, 11, 2)
    
    elif threshold_type == 'binary':
        # Simple binary thresholding
        _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    
    else:
        thresh = gray
    
    return cv2.cvtColor(thresh, cv2.COLOR_GRAY2BGR)

def apply_watershed(img, markers_count=10):
    """
    Apply watershed segmentation
    
    Args:
        img: Input image (BGR format)
        markers_count: Number of markers for watershed
    
    Returns:
        Watershed segmented image
    """
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Apply threshold to get binary image
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    
    # Noise removal
    kernel = np.ones((3, 3), np.uint8)
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
    
    # Sure background area
    sure_bg = cv2.dilate(opening, kernel, iterations=3)
    
    # Finding sure foreground area
    dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
    _, sure_fg = cv2.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)
    sure_fg = np.uint8(sure_fg)
    
    # Finding unknown region
    unknown = cv2.subtract(sure_bg, sure_fg)
    
    # Marker labelling
    _, markers = cv2.connectedComponents(sure_fg)
    markers = markers + 1
    markers[unknown == 255] = 0
    
    # Apply watershed
    markers = cv2.watershed(img, markers)
    
    # Create result image
    result = img.copy()
    result[markers == -1] = [255, 0, 0]  # Mark watershed boundaries in blue
    
    return result

def apply_slic_segmentation(img, n_segments=100, compactness=10):
    """
    Apply SLIC (Simple Linear Iterative Clustering) superpixel segmentation
    
    Args:
        img: Input image (BGR format)
        n_segments: Number of segments
        compactness: Compactness parameter
    
    Returns:
        SLIC segmented image
    """
    # Convert BGR to RGB
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # Apply SLIC
    segments = segmentation.slic(img_rgb, n_segments=n_segments, compactness=compactness)
    
    # Create segmented image
    segmented = color.label2rgb(segments, img_rgb, kind='avg')
    
    # Convert back to BGR
    result = cv2.cvtColor(segmented, cv2.COLOR_RGB2BGR)
    
    return result 