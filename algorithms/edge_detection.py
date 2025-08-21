import cv2
import numpy as np

def apply_sobel(img, ksize=3, dx=1, dy=1):
    """
    Apply Sobel edge detection
    
    Args:
        img: Input image (BGR format)
        ksize: Size of Sobel kernel
        dx: Order of derivative x
        dy: Order of derivative y
    
    Returns:
        Edge detected image
    """
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Apply Sobel
    sobelx = cv2.Sobel(gray, cv2.CV_64F, dx, 0, ksize=ksize)
    sobely = cv2.Sobel(gray, cv2.CV_64F, 0, dy, ksize=ksize)
    
    # Compute magnitude
    magnitude = np.sqrt(sobelx**2 + sobely**2)
    magnitude = np.uint8(magnitude * 255 / magnitude.max())
    
    return cv2.cvtColor(magnitude, cv2.COLOR_GRAY2BGR)

def apply_canny(img, threshold1=50, threshold2=150):
    """
    Apply Canny edge detection
    
    Args:
        img: Input image (BGR format)
        threshold1: First threshold for the hysteresis procedure
        threshold2: Second threshold for the hysteresis procedure
    
    Returns:
        Edge detected image
    """
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Apply Canny
    edges = cv2.Canny(gray, threshold1, threshold2)
    
    return cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

def apply_harris_corner_detection(img, block_size=2, ksize=3, k=0.04, threshold=0.01):
    """
    Apply Harris corner detection
    
    Args:
        img: Input image (BGR format)
        block_size: Size of neighborhood considered
        ksize: Aperture parameter for Sobel operator
        k: Harris detector free parameter
        threshold: Threshold for corner detection
    
    Returns:
        Image with detected corners
    """
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Apply Harris corner detection
    corners = cv2.cornerHarris(gray, block_size, ksize, k)
    
    # Dilate to mark the corners
    corners = cv2.dilate(corners, None)
    
    # Create output image
    result = img.copy()
    result[corners > threshold * corners.max()] = [0, 0, 255]  # Mark corners in red
    
    return result

def apply_hough_lines(img, rho=1, theta=np.pi/180, threshold=100, min_line_length=50, max_line_gap=10):
    """
    Apply Hough line detection
    
    Args:
        img: Input image (BGR format)
        rho: Distance resolution of the accumulator in pixels
        theta: Angle resolution of the accumulator in radians
        threshold: Accumulator threshold parameter
        min_line_length: Minimum line length
        max_line_gap: Maximum gap between line segments
    
    Returns:
        Image with detected lines
    """
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Apply Canny edge detection
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)
    
    # Apply Hough line detection
    lines = cv2.HoughLinesP(edges, rho, theta, threshold, 
                           minLineLength=min_line_length, maxLineGap=max_line_gap)
    
    # Create output image
    result = img.copy()
    
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(result, (x1, y1), (x2, y2), (0, 255, 0), 2)
    
    return result

def apply_hough_circles(img, dp=1, min_dist=50, param1=50, param2=30, min_radius=0, max_radius=0):
    """
    Apply Hough circle detection
    
    Args:
        img: Input image (BGR format)
        dp: Inverse ratio of the accumulator resolution to the image resolution
        min_dist: Minimum distance between the centers of the detected circles
        param1: Upper threshold for the internal Canny edge detector
        param2: Threshold for center detection
        min_radius: Minimum circle radius
        max_radius: Maximum circle radius
    
    Returns:
        Image with detected circles
    """
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Apply Gaussian blur
    gray = cv2.medianBlur(gray, 5)
    
    # Apply Hough circle detection
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, dp, min_dist,
                              param1=param1, param2=param2,
                              minRadius=min_radius, maxRadius=max_radius)
    
    # Create output image
    result = img.copy()
    
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            # Draw the outer circle
            cv2.circle(result, (i[0], i[1]), i[2], (0, 255, 0), 2)
            # Draw the center of the circle
            cv2.circle(result, (i[0], i[1]), 2, (0, 0, 255), 3)
    
    return result 