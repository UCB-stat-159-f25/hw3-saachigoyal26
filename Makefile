# Makefile for HW3 – LIGO Tools (MyST builds)

# 1. Create or update environment
env:
	conda env update --file environment.yml --prune || conda env create --file environment.yml

# 2. Build MyST site locally (HTML)
html:
	myst build --html

# 3. Clean generated files
clean:
	rm -rf _build figures audio
