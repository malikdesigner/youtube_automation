# Youtube and Gmail Account Creation Automation Script


## Overview

This script allows you to automate the creation of Gmail and Youtube accounts using the Selenium automation framework with the Chrome WebDriver. It navigates through the Gmail sign-up process by filling in the required details, such as name, username, password, and more.

## Prerequisites

- Python 3.x
- ChromeDriver - [Download ChromeDriver](https://sites.google.com/chromium.org/driver/)
- Selenium library - Install using `pip install selenium`

## Usage

1. Clone this repository:

   ```
   git clone https://github.com/malikdesigner/youtube_automation.git
   ```

2. Download the ChromeDriver executable and place it in the repository directory.

3. Install the required libraries:

   ```
   pip freeze > requirements.txt
   ```

4. Open the script (`gmail_automation.py`) and update the `your_first_name`, `your_last_name`, `your_username`, `your_birthday`, `your_gender`, and `your_password` variables with your desired account details.

5. Run the script:

   ```
   python gmail_automation.py
   ```

6. The script will automate the Gmail account creation process and provide you with the created account's username and password at the end.

7. **Important:** Please be aware that automating website interactions might go against the website's terms of use. Use this script responsibly and be cautious not to violate any rules or regulations.

## Disclaimer

This script is provided for educational and informational purposes only. The author is not responsible for any misuse or violation of terms of service resulting from the use of this script.

## Credits

Original script by Abdelhakim Khaouiti ([khaouitiabdelhakim on GitHub](https://github.com/khaouitiabdelhakim))

## License
This project is licensed under the MIT License 

```
Copyright 2024 KHAOUITI ABDELHAKIM

Licensed under the MIT License
You may obtain a copy of the License at

http://opensource.org/licenses/MIT

Unless required by applicable law or agreed to in writing, software
distributed under the MIT License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the MIT License.
```
