import base64
import pickle

# Define a minimal dummy class
class UserProfile:
    def __repr__(self):
        return f"UserProfile({self.__dict__})"

# Decode and Deserialize function
def decode_and_deserialize(encoded_data):
    try:
        # Decode base64
        decoded_data = base64.b64decode(encoded_data)

        # Deserialize pickle
        deserialized_obj = pickle.loads(decoded_data)

        print("Deserialized Object:")
        print(deserialized_obj)
        print("\nObject Attributes:")
        print(vars(deserialized_obj))  # Print actual attributes
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    encoded_data = "gASVfgAAAAAAAACMCF9fbWFpbl9flIwLVXNlclByb2ZpbGWUk5QpgZR9lCiMCHVzZXJuYW1llIwEdXNlcpSMA2Jpb5SMDFJlZ3VsYXIgdXNlcpSMC3ByZWZlcmVuY2VzlH2UKIwFdGhlbWWUjAVsaWdodJSMDW5vdGlmaWNhdGlvbnOUiHV1Yi4="
    decode_and_deserialize(encoded_data)
