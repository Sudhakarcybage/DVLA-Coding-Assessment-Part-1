import pytest
from dvla_demo_part1 import DVLAReg

@pytest.fixture
def dvla():
    return DVLAReg()

def test_vehicles_reg_quantity(dvla):
    with open("testdata_dvla.txt") as f:
        expectedtotal_registrationNumbers = int(f.readline().split("=")[1])
        actualtotal_registration_numbers = dvla.totalquantity_registration()
        assert actualtotal_registration_numbers == expectedtotal_registrationNumbers



def test_returnvehicledetailsforgivenregnumbers(dvla):
    expected_vehicle_details = {
        "AB01 CDE": (2001, 12345),
        "FG02 HJK": (2002, 67890),
        "L33T H4X0R": (2022, None)

    }

    for reg_number, (expected_year, expected_vehicle_ID) in expected_vehicle_details.items():
        actual_reg_number, actual_year, actual_vehicle_ID = (dvla.returnvehicledetailsforgivenregnumbers(reg_number))
        assert actual_reg_number == reg_number
        assert actual_year == expected_year
        assert actual_vehicle_ID == expected_vehicle_ID

def test_rigistration_not_found(dvla):
    invalid_registration_numbers = "XX3 XX45"
    actual_reg_number, actual_year, actual_vehicle_ID = (dvla.returnvehicledetailsforgivenregnumbers(invalid_registration_numbers))
    assert (actual_reg_number, actual_year, actual_vehicle_ID) == (None, None, None)
