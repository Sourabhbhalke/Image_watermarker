## Image Watermarking Flask App
### Steps to Run the Application
### Create a Copy of the Project:
### Clone the repository to your local machine.
### Open Command Prompt and Change Directory:
### Navigate to the folder where the app.py file is located.

#### cd path/to/your/repo

### Create Environment:
### Create a new Conda environment. Replace <environment_name> with your preferred environment name.

#### conda create -n <environment_name> python=3.8

### Activate Environment:
### Activate the Conda environment.

#### conda activate <environment_name>

### Install Required Dependencies:
### Install all required Python packages from the requirements.txt file.

#### python -m pip install -r requirements.txt

### Run the Application:
### Start the Flask application.

#### python app.py

### You will receive a URL in the command prompt. Copy and paste this URL into your browser to access the application.


### Test with Sample Data:


### Use the sample_data folder to find images for testing the application.




## Latest Changes

### Refactor Image Processing to Prevent Multiple Logo Stacking

- **Unique Filename Generation:** Implemented unique filename generation using `uuid` to prevent overwriting images and stacking multiple logos on top of each other.
- **Separate Image Saving:** Ensured that each processed image is saved with a unique filename, preserving the original files.
- **Updated Logic for Watermarks:** Updated `views.py` to handle both logo and text watermarks separately without accumulating multiple iterations.

### Changes in `views.py`

- Added logic to create unique filenames for each processed image using `uuid`.
- Modified image saving to use unique filenames, avoiding overwriting of existing files.
- Improved handling of text and logo watermarks to ensure clarity and prevent multiple logos on the same image.

### Additional Changes

- Updated `requirements.txt` to include all necessary dependencies for running the application.

