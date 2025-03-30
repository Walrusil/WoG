from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

debug = True

def test_scores_service(score_url):
    """Test the score service"""
    options = webdriver.ChromeOptions() # Set up the Chrome WebDriver
    options.add_argument('--headless')  # Run headless for testing
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options) # Create a chrom web driver

    try:
        driver.get(score_url) # Open the application URL
        # time.sleep(1) # Allow some time for the page to load (e.g., if the server is remote)

        score = driver.find_element("id", "score").text # Extract the score form the score element

        # Perform the test - check if the score is a number between 1 and 1000
        if score.isdigit():
            score = int(score)
            return 1 <= score <= 1000
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    finally:
        driver.quit() # Close the chrom web driver


def main_function():
    """Run the test and return 0 if passed or -1 if failed"""
    if test_scores_service("http://localhost:5000/score"): # Our score URL is in port 5000...
        if debug:
            print("Test passed!")
        return 0  # Success


    if debug:
        print("Test failed!")
    return -1  # Failure


if __name__ == "__main__":
    exit_code = main_function()
    if debug:
        print(f"Exit code = {exit_code}") # For debugging...
    exit(exit_code)