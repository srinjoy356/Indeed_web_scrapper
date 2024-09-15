from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import json
import time

def extract_job_data(url):
    options = Options()
    options.headless = True  # Run in headless mode
    service = Service(r'chromedriver.exe')  # Update with the correct path
    driver = webdriver.Chrome(service=service, options=options)

    driver.get(url)
    job_listings = driver.find_elements(By.CLASS_NAME, 'tapItem')
    job_data = []
    # job_title_element = listing.find_element(By.CLASS_NAME, 'jobTitle')
    # job_title = job_title_element.text.strip()
    print(driver)


    # for listing in job_listings:
    #     job_title_element = listing.find_element(By.CLASS_NAME, 'jobTitle')
    #     job_title = job_title_element.text.strip()
    #
    #     # Extract the URL from the anchor tag inside the jobTitle element
    #     job_link_element = job_title_element.find_element(By.TAG_NAME, 'a')
    #     job_link = job_link_element.get_attribute('href')
    #
    #     # Navigate to the job detail page to extract the job description
    #     driver.execute_script("window.open(arguments[0]);", job_link)
    #     driver.switch_to.window(driver.window_handles[-1])
    #     time.sleep(2)  # Allow time for the page to load
    #
    #     # Extract job description
    #     try:
    #         job_description_element = driver.find_element(By.ID, 'jobDescriptionText')
    #         job_description = job_description_element.text.strip()
    #     except Exception as e:
    #         job_description = "Job description not found."
    #
    #     # Close the job detail tab and switch back to the job listings tab
    #     driver.close()
    #     driver.switch_to.window(driver.window_handles[0])
    #
    #     job_data.append({
    #         'title': job_title,
    #         'url': job_link,
    #         'description': job_description
    #     })



    driver.quit()
    return job_data

if __name__ == '__main__':
    base_url = "https://in.indeed.com/jobs"
    location = "Kolkata"
    keywords = "python developer"

    url = f"{base_url}?l={location}&q={keywords}"

    job_data = extract_job_data(url)

    with open('jobs.json', 'w') as f:
        json.dump(job_data, f, indent=4)






