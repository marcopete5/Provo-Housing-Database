

import csv
import os
import sys


sys.path.append("../../")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "housing.settings")
import django

django.setup()
print "14"
from main.models import ComplexName

apt_complexes = ComplexName.objects.all()
print apt_complexes
print "19"
for apt_complex in apt_complexes:
	print apt_complex.name
print"22"
complex_list_csv = os.path.join(os.path.dirname(os.path.abspath(__file__)), "complex_list.csv")

csv_file = open(complex_list_csv, 'r')
reader = csv.DictReader(csv_file)


for row in reader:

	new_apt_complex, created = ComplexName.objects.get_or_create(name = row['name'])

	new_apt_complex.address = row['address']
	new_apt_complex.latitude = row['latitude']
	new_apt_complex.longitude = row['longitude']
	new_apt_complex.website = row['website']
	new_apt_complex.phone_number = row['phone_number']


	new_apt_complex.save()

csv_file.close()



