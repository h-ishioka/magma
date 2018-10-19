import argparse
import requests
import xml.etree.ElementTree as ET

class Magma:
	def __init__(self, url = "http://magma.maths.usyd.edu.au/xml/calculator.xml"):
		self.url = url

	def calculate(self, expression, vfrag=False):
		payload = {
			'input' : expression
		}
		req = requests.post(self.url, data=payload)
		root = ET.fromstring(req.text)
		results = root.find('results')
		for line in results.iter('line'):
			print(line.text or "")

		if(vfrag):
			headers = root.find('headers')
			max_time = headers.find('max_time').text
			max_input = headers.find('max_input').text
			seed = headers.find('seed').text
			version = headers.find('version').text
			time = headers.find('time').text
			memory = headers.find('memory').text
			print(f"------------------------------")
			print(f"Calculations are restricted to {max_time} seconds.")
			print(f"Input is limited to {max_input} bytes.")
			print(f"Running Magma V{version}.")
			print(f"Seed: {seed}; Total time: {time} seconds; Total memory usage: {memory}.")

def main():
	parser = argparse.ArgumentParser(description='Magma Calculator')
	parser.add_argument('file', metavar='FILE', type=argparse.FileType('r'))
	parser.add_argument('-v', '--verbose', action='store_true')
	args = parser.parse_args()

	magma = Magma()
	magma.calculate(args.file.read(), args.verbose)

if __name__ == '__main__':
	main()
