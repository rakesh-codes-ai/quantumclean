"""Smoke tests that each case study runs end-to-end without error."""
import runpy
import os
import pytest

HERE = os.path.dirname(__file__)
CASES = os.path.join(HERE, "..", "examples", "case_studies")


@pytest.mark.parametrize("script", [
    "case1_customer_validation.py",
    "case2_transaction_anomalies.py",
    "case3_pipeline_governance.py",
])
def test_case_study_runs(script):
    path = os.path.join(CASES, script)
    # runs the whole script; any exception fails the test
    runpy.run_path(path, run_name="__main__")
