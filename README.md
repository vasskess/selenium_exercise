# Selenium Booking Automation Project

This project is created for educational purposes, serving as a practical exercise to reinforce my understanding of Selenium as I explore its capabilities.

## Introduction

This Selenium automation project focuses on creating a Python script to interact with the Booking.com website. The project covers various actions such as accepting cookies, changing language, selecting a location, choosing dates, adjusting the number of adults, and performing a search.

## Features

- **Accept Cookies:** Automatically accepts cookies on the Booking.com website.
- **Change Language:** Changes the language to Bulgarian on the Booking.com website.
- **Select Location:** Enters the location "Vratza" in the search input field.
- **Select Dates:** Chooses check-in and check-out dates on the calendar.
- **Select Adults:** Adjusts the number of adults ( where first ensures its reduced to 1 if the default value is changed in the future ) and rooms based on predefined constants.
- **Perform Search:** Initiates a search for accommodations.

Additionally, the project includes the following helper functions:

- **`click_with_delay`**: Delays the click actions for a more human-like interaction.
- **`remove_popup_if_presented`**: Removes an annoying popup that may appear during interactions.
- It also includes some helpful comments.

## Installation

1. Clone the repository to your local machine:<br>
```git clone https://github.com/your-username/selenium-booking-automation.git```

2. Install the required dependencies:<br>
```pip install -r requirements.txt```

3. Run the script:<br>
    ```python run.py```
