
# pattern to find Python source files
SOURCES=$(wildcard dnz/*.py)

# Making test phony
.PHONY: test

## help:			: print the help message
help: Makefile
	@sed -n 's/^##//p' $<

## install-deps		: install the dependencies to run and develop the project (may need sudo)
install-deps: install-dependencies

install-dependencies: 
	pip2 install --upgrade -r requirements.txt || pip install --upgrade -r requirements.txt

## clean			: clean temporary build files
clean:
	rm dnz/*.pyc || true
	./setup.py clean --all || true
	rm coverage-debug || true
	rm -Rf .coverage || true

## test			: run the test suite
test:
	./setup.py nosetests

## pep8			: check Python code style
pep8: $(SOURCES)
	pep8 --exclude=_version.py --max-line-length=120 --show-source --show-pep8 setup.py dnz/ || true

pep8_report.txt: $(SOURCES)
	pep8 --exclude=_version.py --max-line-length=120 setup.py dnz/ > pep8_report.txt || true

diff_pep8_report: pep8_report.txt
	diff-quality --violations=pep8 pep8_report.txt

## pep257      		: check Python code style
pep257: $(SOURCES)
	#pep257 --ignore=D100,D101,D102,D103 \
	pep257 \
		setup.py dnz/ || true

pep257_report.txt: $(SOURCES) $(wildcard tests/*.py)
	pep257 setup.py dnz/ > pep257_report.txt 2>&1 || true

diff_pep257_report: pep257_report.txt
	diff-quality --violations=pep8 pep257_report.txt