import os
import sys

sys.path.insert(1,  os.getcwd() + "\\code\\")
import api





top = api.get_top_stories()
story = api.get_item(top[0])



print(story)
