# Rust Commands
format-rust:
	cargo fmt --quiet

lint-rust:
	cargo clippy --quiet

test-rust:
	cargo test --quiet

build-rust:
	cargo build --release

run-rust: 
	cargo run

perf-test-rust:
	cargo test --release --test test_performance -- --nocapture > rust_performance.txt
	echo "# Rust Performance Report" > rust_performance.md
	cat rust_performance.txt >> rust_performance.md

# Python Commands
install-python:
	pip install --upgrade pip && \
		pip install -r requirements.txt

format-python:	
	black src/*.py tests/*.py

lint-python:
	# Uncomment the following for detailed linting with pylint, but note slower speed
	# pylint --disable=R,C --ignore-patterns=test_.*?py src/*.py tests/*.py
	ruff check src/*.py tests/*.py --ignore E501

test-python:
	python -m pytest -vv --cov=src --cov=tests tests/test_stats.py

perf-test-python:
	PYTHONPATH=src python tests/test_performance.py > python_performance.txt
	echo "# Python Performance Report" > python_performance.md
	cat python_performance.txt >> python_performance.md

