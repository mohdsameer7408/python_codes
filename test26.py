from pathlib import Path


path = Path("ecommerce")
print(path.exists())
pl = Path()
for file in pl.glob('*.py'):
    print(file)
