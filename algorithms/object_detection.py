import cv2
import numpy as np

def apply_hog_detection(img):
    """
    Apply HOG (Histogram of Oriented Gradients) for pedestrian detection
    
    Args:
        img: Input image (BGR format)
    
    Returns:
        Image with detected pedestrians
    """
    # Create HOG descriptor
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    
    # Detect people
    boxes, weights = hog.detectMultiScale(img, winStride=(8, 8), padding=(4, 4), scale=1.05)
    
    # Draw detection boxes
    result = img.copy()
    for (x, y, w, h) in boxes:
        cv2.rectangle(result, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    return result

def apply_haar_cascade(img, cascade_type='face'):
    """
    Apply Haar cascade for object detection
    
    Args:
        img: Input image (BGR format)
        cascade_type: Type of cascade ('face', 'eye', 'fullbody')
    
    Returns:
        Image with detected objects
    """
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Load appropriate cascade
    if cascade_type == 'face':
        cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    elif cascade_type == 'eye':
        cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
    elif cascade_type == 'fullbody':
        cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_fullbody.xml')
    else:
        return img
    
    # Detect objects
    objects = cascade.detectMultiScale(gray, 1.1, 4)
    
    # Draw detection boxes
    result = img.copy()
    for (x, y, w, h) in objects:
        cv2.rectangle(result, (x, y), (x + w, y + h), (255, 0, 0), 2)
    
    return result

def apply_template_matching(img, template_size=(50, 50)):
    """
    Apply template matching
    
    Args:
        img: Input image (BGR format)
        template_size: Size of template to search for
    
    Returns:
        Image with template matching results
    """
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Create a simple template (you can replace this with a real template)
    template = np.ones(template_size, dtype=np.uint8) * 128
    
    # Apply template matching
    result = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
    
    # Find matches
    threshold = 0.8
    locations = np.where(result >= threshold)
    
    # Draw matches
    output = img.copy()
    h, w = template.shape
    
    for pt in zip(*locations[::-1]):
        cv2.rectangle(output, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)
    
    return output 