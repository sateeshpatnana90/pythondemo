import datetime

import requests
import csv
import json
class Common_Methods:

    def send_api_request(self,api):
        try:
            if api["auth"] == "Y":
                headers={"auth":"auth"}
            else:
                headers= api["headers"]
            response = requests.request(method=api["method"],url=api["endpoint"],params=api["params"],data=api["payload"],headers=headers)
            return response
        except:
            print("api call failed")

    def verify_response_code(self,expected,actual):
        try:
            assert expected == actual

        except AssertionError:
            print("Response code not matched and actual = ",actual)

    def verify_response_time(self,expected,actual):
        try:
            assert actual <= expected
        except AssertionError:
            print("response time should be less than 2sec and actual=",actual)

    def verify_response_msg(self,expected,actual):
        try:
            print(expected,type(expected))
            print(actual,type(actual))
            if expected == actual:
                print("ok")
            assert expected == actual
        except AssertionError:
            print("response body not matching actual= ",actual," " ,expected)

    def get_api_list(self,path):
        try:
            with open(path, mode='r') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                li = []
                for row in csv_reader:
                    if str(row["execution_flag"]).upper() == "Y":
                        li.append(row)

            #jobj = json.dumps(li)
            return li
        except Exception as ex:
            print("csv file not loading and exception is ",str(ex))
            return []

    def create_report_log(self,title,desc,status):
        timestamp= datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")

        with open('../reports/logs/log.csv', mode='a') as employee_file:
            employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            employee_writer.writerow(['t1',title,status,timestamp,desc])

