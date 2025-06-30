import requests
import json

print("""created by : SAINI01SANDEEP (GITHUB)""")

def test_firebase_security(firebase_url, auth_key=None):
    if not firebase_url.endswith('.json'):
        if firebase_url.endswith('/'):
            firebase_url += '.json'
        else:
            firebase_url += '/.json'

    test_data = {
        "security_test": {
            "message": "test is done",
            "timestamp": "2023-11-15T12:00:00Z",
            "test_id": "delete_me_after_testing"
        }
    }

    print(f"\nTarget Firebase URL: {firebase_url}")
    if auth_key:
        print("Auth Key: Provided")
    else:
        print("Auth Key: Not provided")

    # Test 1: Unauthenticated Read
    print("\n=== Test 1: Unauthenticated Read ===")
    try:
        response = requests.get(firebase_url)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text[:200]}...\n")
    except Exception as e:
        print(f"Error: {str(e)}\n")

    # Test 2: Unauthenticated Write
    print("=== Test 2: Unauthenticated Write ===")
    try:
        response = requests.put(firebase_url, json=test_data)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}\n")
    except Exception as e:
        print(f"Error: {str(e)}\n")

    # Test 3: Authenticated Write
    if auth_key:
        print("=== Test 3: Authenticated Write ===")
        try:
            params = {"auth": auth_key}
            response = requests.put(firebase_url, json=test_data, params=params)
            print(f"Status Code: {response.status_code}")
            print(f"Response: {response.text}\n")
        except Exception as e:
            print(f"Error: {str(e)}\n")

    # Test 4: Invalid Auth Key Write
    print("=== Test 4: Invalid Authentication Write ===")
    try:
        params = {"auth": "invalid-key-123"}
        response = requests.put(firebase_url, json=test_data, params=params)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}\n")
    except Exception as e:
        print(f"Error: {str(e)}\n")

    # Test 5: Path Traversal Attempt
    print("=== Test 5: Path Traversal Attempt ===")
    try:
        malicious_path = firebase_url.replace(".firebaseio.com", ".firebaseio.com/../sensitive_data")
        response = requests.get(malicious_path)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text[:200]}...\n")
    except Exception as e:
        print(f"Error: {str(e)}\n")

    print("✅ Security testing complete.\nCheck the database for test entries and clean up if needed.")

if __name__ == "__main__":
    print("\n=== Firebase Realtime Database Security Tester ===")
    firebase_url = input("Enter the Firebase Realtime Database URL (without `.json`): ").strip()
    auth_key = input("Enter Auth Key (optional - press Enter to skip): ").strip()

    if not firebase_url.startswith("http"):
        print("❌ Invalid URL. Please include 'https://' and try again.")
    else:
        test_firebase_security(firebase_url, auth_key if auth_key else None)
