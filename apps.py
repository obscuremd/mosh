from pathlib import Path

path = Path()
for files in path.glob('*.py'):
    print(files)

print(path.glob('*.py'))