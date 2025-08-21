import cv2
import numpy as np

def apply_sift(img, max_features=100):
    """
    Apply SIFT (Scale-Invariant Feature Transform) feature detection
    
    Args:
        img: Input image (BGR format)
        max_features: Maximum number of features to detect
    
    Returns:
        Image with detected SIFT features
    """
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Create SIFT detector
    sift = cv2.SIFT_create(nfeatures=max_features)
    
    # Detect keypoints
    keypoints = sift.detect(gray, None)
    
    # Draw keypoints
    result = cv2.drawKeypoints(img, keypoints, None, 
                              flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    
    return result

def apply_surf(img, hessian_threshold=400, max_features=100):
    """
    Apply SURF (Speeded-Up Robust Features) feature detection
    
    Args:
        img: Input image (BGR format)
        hessian_threshold: Threshold for hessian keypoint detector
        max_features: Maximum number of features to detect
    
    Returns:
        Image with detected SURF features
    """
    try:
        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # Create SURF detector (only available in opencv-contrib-python)
        surf = cv2.xfeatures2d.SURF_create(hessian_threshold)
        surf.setMaxFeatures(max_features)
        
        # Detect keypoints
        keypoints = surf.detect(gray, None)
        
        # Draw keypoints
        result = cv2.drawKeypoints(img, keypoints, None, 
                                  flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        
        return result
    except:
        # Fallback to SIFT if SURF is not available
        return apply_sift(img, max_features)

def apply_orb(img, max_features=100):
    """
    Apply ORB (Oriented FAST and Rotated BRIEF) feature detection
    
    Args:
        img: Input image (BGR format)
        max_features: Maximum number of features to detect
    
    Returns:
        Image with detected ORB features
    """
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Create ORB detector
    orb = cv2.ORB_create(nfeatures=max_features)
    
    # Detect keypoints
    keypoints = orb.detect(gray, None)
    
    # Draw keypoints
    result = cv2.drawKeypoints(img, keypoints, None, 
                              flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    
    return result

def apply_brief(img, max_features=100):
    """
    Apply BRIEF (Binary Robust Independent Elementary Features) feature detection
    
    Args:
        img: Input image (BGR format)
        max_features: Maximum number of features to detect
    
    Returns:
        Image with detected BRIEF features
    """
    try:
        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # Create STAR detector (used with BRIEF)
        star = cv2.xfeatures2d.StarDetector_create(maxSize=45)
        
        # Create BRIEF descriptor
        brief = cv2.xfeatures2d.BriefDescriptorExtractor_create()
        
        # Detect keypoints
        keypoints = star.detect(gray, None)
        
        # Limit number of keypoints
        if len(keypoints) > max_features:
            keypoints = keypoints[:max_features]
        
        # Draw keypoints
        result = cv2.drawKeypoints(img, keypoints, None, 
                                  flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        
        return result
    except:
        # Fallback to ORB if BRIEF is not available
        return apply_orb(img, max_features) 