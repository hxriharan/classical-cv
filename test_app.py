#!/usr/bin/env python3
"""
Test script for the Classical Computer Vision Gradio App
"""

import sys
import os

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def test_imports():
    """Test if all required modules can be imported"""
    try:
        import gradio as gr
        print("✅ Gradio imported successfully")
        
        import cv2
        print("✅ OpenCV imported successfully")
        
        import numpy as np
        print("✅ NumPy imported successfully")
        
        from PIL import Image
        print("✅ PIL imported successfully")
        
        # Test our algorithm imports
        from algorithms.image_processing import apply_gaussian_blur
        print("✅ Image processing algorithms imported successfully")
        
        from algorithms.edge_detection import apply_canny
        print("✅ Edge detection algorithms imported successfully")
        
        from algorithms.feature_detection import apply_sift
        print("✅ Feature detection algorithms imported successfully")
        
        from algorithms.segmentation import apply_thresholding
        print("✅ Segmentation algorithms imported successfully")
        
        from algorithms.object_detection import apply_haar_cascade
        print("✅ Object detection algorithms imported successfully")
        
        print("\n🎉 All imports successful! The app should work correctly.")
        return True
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("Please install missing dependencies with: pip install -r requirements.txt")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

def test_basic_functionality():
    """Test basic algorithm functionality"""
    try:
        import cv2
        import numpy as np
        from algorithms.image_processing import apply_gaussian_blur
        
        # Create a test image
        test_img = np.random.randint(0, 255, (100, 100, 3), dtype=np.uint8)
        
        # Test Gaussian blur
        result = apply_gaussian_blur(test_img)
        
        if result is not None and result.shape == test_img.shape:
            print("✅ Basic algorithm functionality test passed")
            return True
        else:
            print("❌ Basic algorithm functionality test failed")
            return False
            
    except Exception as e:
        print(f"❌ Basic functionality test failed: {e}")
        return False

if __name__ == "__main__":
    print("🧪 Testing Classical Computer Vision Gradio App...\n")
    
    # Test imports
    imports_ok = test_imports()
    
    if imports_ok:
        # Test basic functionality
        functionality_ok = test_basic_functionality()
        
        if functionality_ok:
            print("\n🚀 All tests passed! You can now run the app with:")
            print("python gradio_app.py")
        else:
            print("\n⚠️  Some functionality tests failed. Check the algorithms.")
    else:
        print("\n❌ Import tests failed. Please check your dependencies.") 