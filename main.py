"""
This is the main Python script for signing a PDF file using the Dropbox Sign API
"""

# Imports
import sys

# pretty print makes JSON responses look good on the console output
from pprint import pprint

# Import config.py config.py is in .gitignore so that it doesn't get pushed to Git repo
import config

# import different Dropbox Sign modules
from dropbox_sign import \
    ApiClient, ApiException, Configuration, apis, models
    
# Global variables
configuration = Configuration(
    # Configure HTTP basic authorization: api_key
    username=config.API_KEY,

    # or, configure Bearer (JWT) authorization: oauth2
    # access_token="YOUR_ACCESS_TOKEN",
)

# Class declarations

# Function declarations

def main():
    with ApiClient(configuration) as api_client:
        signature_request_api = apis.SignatureRequestApi(api_client)

        signer_1 = models.SubSignatureRequestTemplateSigner(
            role="Developer",
            email_address=config.SIGNER_EMAIL_ADDRESS,
            name="Prospective Developer",
        )

        signing_options = models.SubSigningOptions(
            draw=True,
            type=True,
            upload=True,
            phone=True,
            default_type="draw",
        )

        data = models.SignatureRequestSendWithTemplateRequest(
            template_ids=config.TEMPLATE_IDS,
            subject="Standard Developer NDA",
            message="Please sign the NDA first",
            signers=[signer_1],
            signing_options=signing_options,
            test_mode=True,
        )

        try:
            response = signature_request_api.signature_request_send_with_template(data)
            pprint(response)
        except ApiException as e:
            print("Exception when calling Dropbox Sign API: %s\n" % e)

# Main body
if __name__ == '__main__':
    main()