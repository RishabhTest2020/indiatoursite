import os

# Let's inspect jaipur_gal1, jaipur_gal2, jaipur_gal3 to see what they are
print("Checking Jaipur images:")
for f in os.listdir('img'):
    if 'jaipur' in f:
        print(f, os.path.getsize(os.path.join('img', f)))
