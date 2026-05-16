# Task 0: Basics of HTTP/HTTPS

## 1. Differentiating HTTP and HTTPS
- **Security (Encryption):** HTTP transmits data in plain text, making it vulnerable to interception and eavesdropping (e.g., using packet sniffers like Wireshark). HTTPS encrypts the session with an SSL/TLS layer, transforming sensitive data into unreadable ciphertext.
- **Ports:** HTTP uses port 80 by default, whereas HTTPS uses port 443 for secure connections.
- **Data Integrity:** HTTPS prevents data from being modified or tampered with during transit by unauthorized third parties.

## 2. Structure of an HTTP Request and Response

### HTTP Request Structure:
1. **Request Line:** Contains the method (e.g., GET, POST), the resource path (e.g., /index.html), and the protocol version (e.g., HTTP/1.1).
2. **Headers:** Key-value pairs providing metadata about the request (e.g., `Host: example.com`, `User-Agent: Mozilla/5.0`, `Accept: application/json`).
3. **Empty Line:** A blank line separating headers from the body.
4. **Body:** Optional data payload sent to the server (mainly used in POST, PUT, or PATCH requests to submit form inputs or JSON payloads).

### HTTP Response Structure:
1. **Status Line:** Contains the protocol version, a numeric status code, and its textual reason phrase (e.g., HTTP/1.1 200 OK).
2. **Headers:** Metadata regarding the server and response content (e.g., `Content-Type: text/html`, `Server: Apache`, `Date`).
3. **Empty Line:** A blank line indicating the headers section is complete.
4. **Body:** The actual content returned by the server, such as HTML, images, or JSON data.

## 3. Common HTTP Methods
- **Method:** GET
  - **Description:** Retrieves data from the server. It is an idempotent method that does not modify server state.
  - **Use Case:** Fetching a web page or retrieving a user profile from an API.
- **Method:** POST
  - **Description:** Submits data to the server to create a new resource.
  - **Use Case:** Submitting a registration form to create a new account.
- **Method:** PUT
  - **Description:** Replaces all current representations of the target resource with the request payload.
  - **Use Case:** Updating an entire user profile with new details.
- **Method:** DELETE
  - **Description:** Deletes the specified resource from the server.
  - **Use Case:** Removing a blog post or deleting an account.

## 4. Common HTTP Status Codes
- **Status Code:** 200 OK
  - **Description:** The request succeeded, and the server delivered the expected payload.
  - **Scenario:** A user visits `google.com` and the search page loads successfully.
- **Status Code:** 301 Moved Permanently
  - **Description:** The requested resource has been assigned a new permanent URI.
  - **Scenario:** A website migrates from HTTP to HTTPS, redirecting all legacy traffic automatically.
- **Status Code:** 400 Bad Request
  - **Description:** The server cannot process the request due to a client-side error (e.g., malformed syntax).
  - **Scenario:** Sending a broken or invalid JSON payload to an API endpoint.
- **Status Code:** 401 Unauthorized
  - **Description:** The request requires user authentication or authentication credentials failed.
  - **Scenario:** An unauthenticated user attempts to access a protected private dashboard.
- **Status Code:** 404 Not Found
  - **Description:** The server cannot find the requested resource or path.
  - **Scenario:** Typing a non-existent URL extension like `example.com/broken-link` in the browser.
- **Status Code:** 500 Internal Server Error
  - **Description:** The server encountered an unexpected condition that prevented it from fulfilling the request.
  - **Scenario:** A backend crash or database connection failure in a Python/Flask application.
