import requests
import json


class SurveyMokeyAPI:

    def __init__(self, api_key):

        with open('client_data.json', 'r') as f:
            client_data = json.load(f)

        self.client_id = client_data['client_id']
        self.secret = client_data['secret']
        self.api_key = api_key

    # SURVEY -------------------------------------------------------------------

    def get_surveys(self):
        response = self.request('get', endpoint='surveys')
        # survey_list = response.json().get("data", {}).get("surveys")
        return response.json()

    def get_survey_details(self, survey_id):
        endpoint = 'surveys/{}/details'.format(survey_id)
        response = self.request('get', endpoint=endpoint)
        return response.json()

    def create_survey(self, survey):
        response = self.request('post', endpoint='surveys', body=survey)
        return response.json()

    def update_survey(self, survey_id, survey):
        endpoint = 'surveys/{}'.format(survey_id)
        response = self.request('put', endpoint=endpoint, body=survey)
        return response.json()

    # PAGE ---------------------------------------------------------------------

    def create_page(self, survey_id, page_data):
        endpoint = "surveys/{}/pages".format(survey_id)
        response = self.request('post', endpoint=endpoint, body=page_data)
        return response.json()

    def update_page(self, survey_id, page_id, page_data):
        endpoint = "surveys/{}/pages/{}".format(survey_id, page_id)
        response = self.request('put', endpoint=endpoint, body=page_data)
        return response.json()

    def get_pages(self, survey_id):
        endpoint = "surveys/{}/pages".format(survey_id)
        response = self.request('get', endpoint=endpoint)
        return response.json()

    # QUESTION -----------------------------------------------------------------

    def create_question(self, survey_id, page_id, page_data):
        endpoint = "surveys/{}/pages/{}/questions".format(survey_id, page_id)
        response = self.request('post', endpoint=endpoint, body=page_data)
        return response.json()

    def update_question(self, survey_id, page_id, question_id, question_data):
        endpoint = "surveys/{}/pages/{}/questions/{}".format(survey_id, page_id, question_id)
        response = self.request('put', endpoint=endpoint, body=question_data)
        return response.json()

    def get_questions(self, survey_id, page_id):
        endpoint = "surveys/{}/pages/{}/questions".format(survey_id, page_id)
        response = self.request('get', endpoint=endpoint)
        return response.json()

    # CONTACTS -----------------------------------------------------------------

    def create_contact_list(self, contact_list):
        endpoint = "contact_lists/"
        response = self.request('post', endpoint=endpoint, body=contact_list)
        return response.json()

    def bulk_create_contacts(self, contact_list_id, contacts):
        endpoint = "contact_lists/{}/contacts/bulk".format(contact_list_id)
        response = self.request('post', endpoint=endpoint, body=contacts)
        return response.json()

    # COLLECTOR ----------------------------------------------------------------

    def create_collector(self, survey_id, collector):
        endpoint = "surveys/{}/collectors".format(survey_id)
        response = self.request('post', endpoint=endpoint, body=collector)
        return response.json()

    def update_collector(self, collector_id, collector):
        endpoint = "collectors/{}".format(collector_id)
        response = self.request('put', endpoint=endpoint, body=collector)
        return response.json()

    def get_collector(self, collector_id):
        endpoint = "collectors/{}".format(collector_id)
        response = self.request('get', endpoint=endpoint)
        return response.json()

    def get_survey_collectors(self, survey_id):
        endpoint = "surveys/{}/collectors".format(survey_id)
        response = self.request('get', endpoint=endpoint)
        return response.json()

    # COLLECTOR MESSAGE --------------------------------------------------------

    def get_collector_messages(self, collector_id):
        endpoint = "collectors/{}/messages".format(collector_id)
        response = self.request('get', endpoint=endpoint)
        return response.json()

    def get_collector_message(self, collector_id, message_id):
        endpoint = "collectors/{}/messages/{}".format(collector_id, message_id)
        response = self.request('get', endpoint=endpoint)
        return response.json()

    def create_collector_message(self, collector_id, message):
        endpoint = "collectors/{}/messages".format(collector_id)
        response = self.request('post', endpoint=endpoint, body=message)
        return response.json()

    # SEND
    def send_collector_message(self, collector_id, message_id, schedule_date):
        endpoint = "collectors/{}/messages/{}/send".format(collector_id,
                                                           message_id)
        send_body = dict()
        if schedule_date:
            send_body = {'scheduled_date': schedule_date}
        response = self.request('post', endpoint=endpoint, body=send_body)
        return response.json()

    # RECIPIENTS ---------------------------------------------------------------

    def set_collector_recipient(self, collector_id, message_id, recipient):
        endpoint = "collectors/{}/messages/{}/recipients".format(collector_id,
                                                                 message_id)
        response = self.request('post', endpoint=endpoint, body=recipient)
        return response.json()

    def get_collector_recipients(self, collector_id, message_id):
        endpoint = "collectors/{}/messages/{}/recipients".format(collector_id,
                                                                 message_id)
        response = self.request('get', endpoint=endpoint)
        return response.json()

    # REQUEST ------------------------------------------------------------------

    def request(self, method, endpoint, body=None):
        headers = {
            "Authorization": "bearer {}".format(self.api_key),
            "Content-Type": "application/json"
        }
        host = "https://api.surveymonkey.net/v3/"
        uri = "{}{}".format(host, endpoint)

        client = requests.session()
        response = client.request(method, uri, json=body, headers=headers)
        return response
