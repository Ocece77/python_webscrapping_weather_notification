
# 🌦️ Weather Notification App 🌦️

**Created by [Oceane (ocece77)](https://github.com/ocece77)**  
📧 Contact: oceanekasindupro@gmail.com

---

## 🌟 Project Overview

Welcome to the **Weather Notification App**! This project is designed to keep you updated on the weather throughout the day, sending notifications directly to your macOS desktop. Whether it's morning, afternoon, or evening, you’ll get the current temperature in real-time! This project was developed as part of my journey to deepen my Python skills and share my passion for this language. 🐍

This project only run on MacOs

---

## 🎯 Features

- **Real-time Weather Notifications**: Get temperature updates based on the current time of day—morning, afternoon, or evening.
- **macOS Compatibility**: Uses the `pync` library for native macOS notifications.
- **BeautifulSoup Web Scraping**: Gathers weather data directly from [Weather.com](https://weather.com) by scraping temperature information.
- **Time-based Logic**: Automatically determines whether to display morning, afternoon, or evening temperatures.

---

## ⚙️ How It Works

1. **Get Current Time**: 🕒 The app checks the system time to determine which weather update to show.
2. **Scrape Weather Data**: 🌐 The app pulls weather data from [Weather.com](https://weather.com) using `requests` and `BeautifulSoup`.
3. **Display Notifications**: 💬 The app sends a weather update notification for the morning, afternoon, or evening based on the current time.

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.x**
- **macOS** (for `pync` notifications)
- Install required Python libraries with:
  ```bash
  pip install requests beautifulsoup4 pync
  ```

### Installation & Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/ocece77/weather-notification-app.git
   cd weather-notification-app
   ```

2. Run the program:
   ```bash
   python weather_notification.py
   ```

3. 🎉 **Get Notified**: Based on the time, you'll receive a notification with the current temperature for the relevant part of the day!

---

## 📄 Code Explanation

### Main Components

- **Time Retrieval**: 
  ```python
  c_time = datetime.now()
  curr_time_parse = c_time.strftime('%H:%M:%S')
  ```
  Uses the `datetime` library to get the current time and formats it to identify the appropriate part of the day.

- **Weather Data Fetching**:
  ```python
  def getWeather(url):
      req = requests.get(url)
      if req.status_code == 200:
          print("Find it!")
      return req.text
  ```
  Retrieves and returns the raw HTML from Weather.com if the connection is successful.

- **Data Parsing**:
  ```python
  morning_indication = soup.find("span", dir="ltr").contents
  ```
  Extracts specific weather details from the HTML using `BeautifulSoup`.

- **Notification Functions**:
  ```python
  def displayMorningTemp():
      pync.notify(morning_temp_str, title="Today's weather 🌥️")
  ```
  Displays notifications for morning, afternoon, or evening temperatures on macOS.

---

## 💡 Why I Built This

I'm **Oceane** (aka **ocece77**), and I created this project because I'm passionate about Python 🐍 and aim to work with it professionally in the future. This project gave me hands-on experience with web scraping, real-time data handling, and time-based logic, all while using my favorite language!

---

## 📝 Feedback

Feel free to leave comments or suggestions to help me improve the code or explore new features! 📨

---

Happy coding, and stay informed with your local weather! 🌤️
