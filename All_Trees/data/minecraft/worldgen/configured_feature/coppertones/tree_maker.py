import json
from copy import deepcopy

with open('types.json') as f:
	globals().update(json.load(f))
with open('generic.json') as f:
	generic = json.load(f)

for t in trunks:
	for f in foliage:
		new = deepcopy(generic)
		new['config']['trunk_placer']['type'] = t['type']
		new['config']['foliage_placer']['type'] = f['type']
		new['config']['trunk_provider']['state']['Name'] = t['block']
		new['config']['leaves_provider']['state']['Name'] = f['block']
		if 'extra' in f:
			new['config']['foliage_placer'].update(f['extra'])
		if t['abbr'] == 'f':
			new['config']['trunk_provider']['state']['Properties'] = {'axis': 'y'}
		with open('_'.join(['tree', t['abbr'], f['abbr']])+'.json', 'w') as f:
			json.dump(new, f, indent=4)

input('Done!')