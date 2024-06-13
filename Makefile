dist/token-counter.exe: token-counter.py
	pyinstaller --onefile --windowed --additional-hooks-dir=. $<
