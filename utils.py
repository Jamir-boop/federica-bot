import os
import datetime

def take_screenshot(driver, filename=None):
    """
    Takes a screenshot of the current page and saves it with the specified filename.
    If no filename is provided, it generates one based on the class name, date, and time.

    :param driver: The WebDriver instance.
    :param filename: The name of the file where the screenshot will be saved (optional).
    """
    # Create the logs directory if it doesn't exist
    if not os.path.exists('logs'):
        os.makedirs('logs')

    if filename is None:
        now = datetime.datetime.now().strftime('%d-%m-%Y_%M_%H_%S')
        classname = driver.__class__.__name__
        filename = f'{classname}_{now}.png'
    elif not os.path.splitext(filename)[1] == '.png':
        filename += '.png'
    
    # Modify the path to save the screenshot in the logs folder
    filepath = os.path.join('logs', filename)
    driver.save_screenshot(filepath)
    print(f'Screenshot saved as {filepath}')
