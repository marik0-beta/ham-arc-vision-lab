# HAM ARC Vision Lab

A beginner-friendly computer-vision demo built with Python, OpenCV, NumPy, and Streamlit. Upload an image and explore grayscale conversion, Canny edge detection, threshold segmentation, and HSV color masking. Processed images can be downloaded.

> **Scope:** This is an image-processing prototype, not a trained object detector and not a hardware-integrated system.

## Features

- Upload PNG, JPG, JPEG, or WebP images
- Convert an image to grayscale
- Detect edges with adjustable Canny thresholds
- Segment pixels using a brightness threshold
- Experiment with HSV color masking
- Download processed output as a PNG
- Run locally on Windows without Arduino or a webcam

## Tech stack

- Python
- OpenCV
- NumPy
- Pillow
- Streamlit

## Run locally on Windows

1. Install Python 3.10 or newer from [python.org](https://www.python.org/downloads/). During installation, enable **Add Python to PATH**.
2. Download or clone this repository.
3. Open Command Prompt or PowerShell in the project folder.
4. Create and activate a virtual environment:

   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

   If PowerShell blocks activation, use Command Prompt and run:

   ```bat
   .venv\Scripts\activate.bat
   ```

5. Install dependencies:

   ```powershell
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

6. Launch the app:

   ```powershell
   python -m streamlit run app.py
   ```

7. Open the local URL shown in the terminal (usually `http://localhost:8501`) and upload an image.

## Quick test checklist

- [ ] App launches without errors
- [ ] Upload a JPG or PNG
- [ ] Grayscale output is black and white
- [ ] Canny output highlights object boundaries
- [ ] Changing threshold sliders changes the output
- [ ] HSV mask isolates at least some pixels in the selected hue range
- [ ] Download button saves a PNG that opens correctly

## Publish to GitHub

Create a new **public** repository named `ham-arc-vision-lab` on GitHub. Do not initialize it with a README if you already have this one locally. Then, from the project folder:

```powershell
git init
git add .
git commit -m "Build interactive OpenCV vision lab"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/ham-arc-vision-lab.git
git push -u origin main
```

Replace `YOUR-USERNAME` with your GitHub username. Git may ask you to authenticate in a browser.

## Optional live demo

You can deploy the app using Streamlit Community Cloud:

1. Push the repository to GitHub.
2. Visit [share.streamlit.io](https://share.streamlit.io/).
3. Sign in with GitHub and select this repository.
4. Set the main file to `app.py` and deploy.

Deployment availability and platform requirements can change. Test the public link in a private/incognito window before sharing it.

## Possible next improvements

- Add contour detection and object-area measurements
- Add a webcam mode with clear permission handling
- Add a pretrained object-detection model and compare its results with classical vision
- Add a simple test suite for image-processing functions
- Later, connect vision output to an Arduino project when hardware is available

## What I learned

After running and testing the app, update this section with what you personally observed about image arrays, color spaces, thresholds, and edge detection. Do not claim experiments you have not completed.
