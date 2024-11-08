install:
	poetry install

brain-games:
	poetry run brain-games

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

package-reinstall:
	python3 -m pip install --user --force-reinstall dist/*.whl

# local install
package-install-local:
	python3 -m pip install dist/*.whl

# local reinstall
package-reinstall-local:
	python3 -m pip install --force-reinstall dist/*.whl

# local build and reinstall
fil:
	poetry build
	python3 -m pip install --force-reinstall dist/*.whl

# global build and reinstall
fi:
	poetry build
	python3 -m pip install --user --force-reinstall dist/*.whl

lint:
	poetry run flake8 brain_games
