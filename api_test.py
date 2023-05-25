import pytest

from apiautomation.common import config
from apiautomation.common.common_methods import Common_Methods

# from apiautomation.apiautomation.common import config
# from fratello.apiautomation.common.common_methods import Common_Methods

common_methods = Common_Methods()
api_list = common_methods.get_api_list(config.csv_path)
@pytest.mark.parametrize("api",api_list)
def test_verify_api(api):
    print("\napi -- ",api)
    response = common_methods.send_api_request(api)
    common_methods.verify_response_code(int(api["response_code"]),response.status_code)
    common_methods.verify_response_time(int(api["res_time"]),response.elapsed.total_seconds())
    common_methods.verify_response_msg(str(api["response"]),str(response.json()["result"]))
    common_methods.create_report_log(api["title"],"testcese","passed")


