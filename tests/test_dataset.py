
from helper import dataset_not_found_return_codes, successful_return_codes

# Import SEAR
from sear import sear


def test_add_dataset(delete_dataset):
    add_result = sear(
            {
            "operation": "add", 
            "admin_type": "data-set", 
            "data_set": delete_dataset,
            "traits": {
                "base:installation_data": "DATASET PROFILE GENERATED DURING SEAR TESTING, NOT IMPORTANT",  # noqa: E501
            },
            },
        )
    assert "errors" not in str(add_result.result)
    assert add_result.result["return_codes"] == successful_return_codes

def test_extract_dataset(create_dataset):
    extract_result = sear(
            {
            "operation": "extract",
            "admin_type": "data-set", 
            "data_set": create_dataset,
            },
        )
    assert "errors" not in str(extract_result.result)
    assert extract_result.result["return_codes"] == successful_return_codes

def test_dataset_not_found():
    not_found_result = sear(
            {
            "operation": "extract",
            "admin_type": "data-set", 
            "data_set": "DOES.NOT.EXIST",
            },
        )
    assert "errors" in str(not_found_result.result)
    assert not_found_result.result["return_codes"] == dataset_not_found_return_codes

def test_delete_dataset(create_dataset):
    delete_result = sear(
            {
            "operation": "delete",
            "admin_type": "data-set", 
            "data_set": create_dataset,
            },
        )
    assert "errors" not in str(delete_result.result)
    assert delete_result.result["return_codes"] == successful_return_codes