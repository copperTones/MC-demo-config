import json
from copy import deepcopy

with open('generic.json') as f:
	generic = json.load(f)

trunks = (
	('straight_trunk_placer', 'minecraft:red_concrete', 's'),
	('forking_trunk_placer', 'minecraft:orange_concrete', 'fr'),
	('giant_trunk_placer', 'minecraft:yellow_concrete', 'g'),
	('mega_jungle_trunk_placer', 'minecraft:green_concrete', 'mj'),
	('dark_oak_trunk_placer', 'minecraft:blue_concrete', 'dk'),
	('fancy_trunk_placer', 'minecraft:stripped_crimson_stem', 'f')
)
foliage = (
	('blob_foliage_placer', 'minecraft:red_stained_glass', 'bl', {'height': 4}),
	('spruce_foliage_placer', 'minecraft:orange_stained_glass', 's', {
		'trunk_height': {
			'base': 4,
			'spread': 4
		}}),
	('pine_foliage_placer', 'minecraft:yellow_stained_glass', 'p', {
		'height': {
			'base': 4,
			'spread': 4
		}}),
	('acacia_foliage_placer', 'minecraft:lime_stained_glass', 'ac', {}),
	('bush_foliage_placer', 'minecraft:cyan_stained_glass', 'b', {'height': 4}),
	('fancy_foliage_placer', 'minecraft:light_blue_stained_glass', 'f', {'height': 4}),
	('jungle_foliage_placer', 'minecraft:blue_stained_glass', 'j', {'height': 4}),
	('mega_pine_foliage_placer', 'minecraft:purple_stained_glass', 'mp', {
		'crown_height': {
			'base': 4,
			'spread': 4
		}}),
	('dark_oak_foliage_placer', 'minecraft:magenta_stained_glass', 'dk', {})
)

for t_type, t_block, t_abbr in trunks:
	for f_type, f_block, f_abbr, extra in foliage:
		new = deepcopy(generic)
		new['config']['trunk_placer']['type'] = t_type
		new['config']['foliage_placer']['type'] = f_type
		new['config']['trunk_provider']['state']['Name'] = t_block
		new['config']['leaves_provider']['state']['Name'] = f_block
		new['config']['foliage_placer'].update(extra)
		if t_abbr == 'f':
			new['config']['trunk_provider']['state']['Properties'] = {'axis': 'y'}
		with open('_'.join(['tree', t_abbr, f_abbr])+'.json', 'w') as f:
			json.dump(new, f, indent=4)

input('Done!')