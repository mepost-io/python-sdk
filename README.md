Mepost Python SDK
=================

This Python library provides a convenient way to interact with the Mepost API, facilitating operations such as sending emails, managing scheduled messages, and querying specific message information using the Mepost platform.

Features
--------

-   Send emails directly and using predefined templates.
-   Retrieve, cancel, and manage scheduled messages.
-   Query information about specific messages.

Installation
------------

To install the Mepost Python SDK, simply use pip:

```bash
pip install mepost-sdk
```

Ensure you have Python 3.6 or later installed on your system.

Usage
-----

Here's how to get started with the Mepost Python SDK:

### Initializing a Client

First, create a client instance with your API key:

```python
from mepost.client import MepostClient

client = MepostClient(api_key="your_api_key_here")
```

### Sending an Email

To send an email using the SDK:

```python
email_data = {
    "from_email": "info@example.com",
    "subject": "Test Email",
    "text": "This is a test email sent from the Mepost Python SDK.",
    "to": [{"email": "recipient@example.com"}]
}

response = client.send_email(email_data)
print("Email sent response:", response)
```

### Managing Scheduled Messages

To retrieve information about a scheduled message:

```python
schedule_id = "your_schedule_id"
email_info = client.get_info(schedule_id, "recipient@example.com")
print("Scheduled Message Info:", email_info)
```

Available Methods
-----------------

The Mepost Python SDK offers the following methods:

### `send_email(email_data)`

-   Description: Sends an email with the provided details.
-   Parameters:
    -   `email_data`: A dictionary containing email fields such as `from_email`, `subject`, `text`, and `to`.

### `send_email_by_template(email_data, template_id)`

-   Description: Sends an email using a specified template.
-   Parameters:
    -   `email_data`: A dictionary containing the email details.
    -   `template_id`: The ID of the template used for sending the email.

### `get_info(schedule_id, email)`

-   Description: Retrieves information about a specific scheduled message.
-   Parameters:
    -   `schedule_id`: The ID of the scheduled message.
    -   `email`: The email address associated with the message.

### `cancel_scheduled_message(scheduled_message_id)`

-   Description: Cancels a scheduled message.
-   Parameters:
    -   `scheduled_message_id`: The ID of the message to cancel.

### `get_scheduled_message(schedule_id)`

-   Description: Retrieves a scheduled message.
-   Parameters:
    -   `schedule_id`: The ID of the scheduled message.

Contributing
------------

Contributions to the Mepost Python SDK are welcome! Please feel free to fork the repository, make changes, and submit pull requests.

License
-------

This SDK is distributed under the MIT License, see LICENSE for more information.
