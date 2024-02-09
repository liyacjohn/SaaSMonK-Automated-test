from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_movie_website_login():
    # Start the WebDriver (Chrome in this example)
    driver = webdriver.Chrome()

    try:
        # Open the movie review website
        driver.get("https://movie-reviews-psi.vercel.app/")

        # Use explicit wait for the presence of movie cards
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "/html/body/main/section[2]/div[1]/a/article"))
        )

        # Validate the presence of movie cards and search bar
        assert len(driver.find_elements(By.XPATH, "/html/body/main/section[2]/div[1]/a/article")) > 0
        assert driver.find_element(By.XPATH, "/html/body/main/section[1]/input").is_displayed()
        print("\n Test Case 1: Home Page - Movie cards and search bar validated. \n")

        # Test Case 2: Clicking on a movie card opens the movie review page
        movie_card = driver.find_element(By.XPATH, "/html/body/main/section[2]/div[1]/a/article")
        movie_card.click()
        time.sleep(2)

        # Wait for the title to change to "Movie Review"
        WebDriverWait(driver, 10).until(EC.title_contains("Movie Review"))
        driver.get("https://movie-reviews-psi.vercel.app/")
        time.sleep(2)

        # Validate that the movie review page is opened
        assert "Movie Review" in driver.title
        print("Test Case 2: Movie card click - Movie review page opened.\n")

        # Fill in movie details in the add movie form
        add_movie = driver.find_element(By.XPATH, "/html/body/nav/div/button[1]")
        add_movie.click()

        # Add a small delay before interacting with input fields
        time.sleep(2)

        title_input = driver.find_element(By.ID, "name")
        title_input.send_keys("Test Movie")
        time.sleep(2)

        date_input = driver.find_element(By.ID, "release")
        date_input.send_keys("21/02/2024")
        time.sleep(2)

        submit_button = driver.find_element(By.CSS_SELECTOR, "#movie-add-modal > div > form > div.flex.justify-end > button")
        submit_button.click()


        # Validate the presence of the newly added movie in the list
        assert "Test Movie" in driver.page_source
        print("Test Case 3: Add Movie - Movie list updated with 'Test Movie'.\n")

        # Test Case 4: Editing a movie updates the movie list
        edit_movie_button = driver.find_element(By.XPATH, "/html/body/main/section[2]/div[1]/div/button[1]")
        edit_movie_button.click()

        # Modify movie details in the edit movie form
        title_input.clear()
        title_input.send_keys("Edited Movie")
        submit_button.click()

        # Validate the presence of the edited movie in the list
        assert "Edited Movie" in driver.page_source
        print("Test Case 4: Edit Movie - Movie list updated with 'Edited Movie'.")


        # Wait for the login to complete
        WebDriverWait(driver, 10).until(EC.title_contains("Movie Review"))

        # Assert that the user is redirected to the home page after login
        assert "Movie Review" in driver.title

    finally:
        # Close the browser window
        driver.quit()

# Run the test
if __name__ == "__main__":
    test_movie_website_login()
