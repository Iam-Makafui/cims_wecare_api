# Welfare Management System API

The Welfare Management System API is a comprehensive system designed to manage welfare activities efficiently. It provides a robust interface to handle user management, welfare payments, case management, reporting and analytics, chatbot integration, SMS notifications, and expense tracking.

## Features

    User Management: Crucial for security and access control, ensuring only authorized personnel can interact with the system and defining different roles for administrators, case managers, etc.

    Welfare Payment (Single & Bulk): Facilitating individual or bulk payments efficiently ensures timely support to beneficiaries while streamlining the payment process.

    Case Management: Capturing detailed information about each case, including member details, issued aid, and dates, allows for personalized support and accurate tracking of welfare activities.

    Reporting and Analytics: Essential for insights into the welfare program's performance, helping in decision-making, resource allocation, and identifying trends or areas needing attention.

    Chatbot: A user-friendly interface to access and retrieve welfare-related data from the database, enhancing accessibility and easing information retrieval for users.

    SMS Notifications: Timely notifications can be crucial for both beneficiaries and staff, ensuring important updates or reminders are received promptly.

    Expenses Entry and Tracking: Maintaining records of expenses incurred allows for transparent financial tracking, aiding in budgeting and compliance with auditing standards.

## Usage

### Prerequisites

    Python 3.x
    MySQL
    
### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Iam-Makafui/welfare_management_software_api.git
    cd welfare_management_software_api
    ```

2. Create and activate a virtual environment:
    ```bash
    # Create a virtual environment (if not already created)
    python -m venv myenv

    # Activate the virtual environment
    source myenv/bin/activate  # For Unix/Linux
    .\myenv\Scripts\activate   # For Windows
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Database Setup:
    - Create a MySQL database named `welfare_management_system_dev`.
    - Configure the database connection in `db.py`.

### Running the API

Run the following command within the activated virtual environment and the root folder:
```bash
python run.py
```

## License

This project is licensed under the [MIT License](LICENSE).

---
