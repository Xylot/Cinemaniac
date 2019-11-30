import random
import argparse

movie_list_path = 'Lists/MovieList'
tv_list_path = 'Lists/TVList'
food_list_path = 'Lists/FoodList'

def get_file_list(file_path):
	with open(file_path, 'r') as file:
		titles = file.readlines()
	return [title.strip() for title in titles]

def parse_args():
	parser = argparse.ArgumentParser()
	parser.add_argument("--list", default='movie', help="List to generate from")
	args = parser.parse_args()
	return args

def resolve_args(args):
	if args.list == 'movie':
		return movie_list_path
	elif args.list == 'tv':
		return tv_list_path
	elif args.list ==  'food':
		return food_list_path

args = parse_args()
list_path = resolve_args(args)
content = get_file_list(list_path)

print(random.choice(content))