run_tests:
	@echo "before tests"
	conda run -n python-autotests-basic python -m pytest
	@echo "after tests"

show_cases:
	pytest --collect-only

