def rake_garden(garden):
    return ' '.join([x if x in 'rockgravel' else 'gravel' for x in garden.split()])

'''
Help Suzuki rake his garden!

The monastery has a magnificent Zen garden made of white gravel and rocks and it
 is raked diligently everyday by the monks. Suzuki having a keen eye is always on
 the lookout for anything creeping into the garden that must be removed during the
 daily raking such as insects or moss.

You will be given a string representing the garden such as:

garden = 'gravel gravel gravel gravel gravel gravel gravel gravel gravel rock
  gravel gravel gravel slug gravel rock gravel gravel rock gravel gravel gravel
  gravel snail gravel gravel rock gravel gravel gravel gravel gravel spider
  gravel rock gravel gravel'

Rake out any items that are not a rock or gravel and replace them with gravel such that:

garden = 'slug spider rock gravel gravel gravel gravel gravel gravel gravel'

Returns a string with all items except a rock or gravel replaced with gravel:

garden = 'gravel gravel rock gravel gravel gravel gravel gravel gravel gravel'

'''
