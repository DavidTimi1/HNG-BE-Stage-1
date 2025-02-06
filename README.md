# HNG-BE-Stage-1
HNG Internship Backend Track Stage 1 Task


```markdown
# Number Classification API

The **Number Classification API** is a simple Flask-based service that takes a number as input and returns its mathematical properties, such as whether it's prime, perfect, or an Armstrong number. It also calculates the sum of its digits and provides a fun fact about the number using the Numbers API.

---

## Features
- Determine if a number is **prime** or **perfect**.
- Identify other properties like **odd**, **even**, or **Armstrong**.
- Calculate the **sum of digits** for the given number.
- Fetch a **fun fact** about the number from the Numbers API.
- Fully deployed as a publicly accessible web service.

---

## API Specification

### Endpoint
```plaintext
    GET https://number-classification-93z7.onrender.com/api/classify-number
```

### Query Parameters
| Parameter  | Type   | Required | Description                          |
|------------|--------|----------|--------------------------------------|
| `number`   | `int`  | Yes      | The number to classify.              |

---

### Example Response (200 OK)
```json
{
  "number": 371,
  "is_prime": false,
  "is_perfect": false,
  "properties": ["armstrong", "odd"],
  "digit_sum": 11,
  "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

### Error Responses
#### 400 Bad Request
```json
{
  "number": "alphabet",
  "error": true
}
```

---

## Setup and Installation

### Requirements
- Python 3.7 or higher
- pip (Python package manager)

### Clone the Repository
```bash
git clone <repository-url>
cd HNG-BE-Stage-1
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Run the Application Locally
```bash
python app.py
```

## Project Structure
```
HNG-BE-Stage-1/
│
├── app.py               # Main Flask application
├── requirements.txt     # Dependencies
└── README.md            # Documentation
```

---

## How It Works
1. The API receives a `number` via a query parameter.
2. Validates the input and computes:
   - Whether the number is **prime** or **perfect**.
   - Other properties like **odd**, **even**, or **Armstrong**.
   - **Sum of its digits**.
3. Fetches a fun fact using the [Numbers API](http://numbersapi.com/).
4. Returns the results in a JSON response.

---

## Technologies Used
- **Python**: Backend programming language.
- **Flask**: Web framework for building the API.
- **Numbers API**: For fetching fun facts about numbers.
- **Gunicorn**: WSGI HTTP server for deployment.

## License
This project is licensed under the [MIT License](LICENSE).

