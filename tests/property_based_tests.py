import schemathesis

from api.main import app

schema = schemathesis.from_asgi("/openapi.json", app)

@schema.parametrize()
def test_api(case):
    response = case.call_asgi()
    case.validate_response(response)