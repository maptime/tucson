#%%
ls
# %%
import os
images = [i for i in os.listdir() if "screenshot" in i ]
#%%


import shutil as sh
[sh.copy(i,i.replace(" ","_").lower()) for i in images]



# %%
with open("README.md","r") as phile:
    contents = phile.read()


# %%
images.sort()

# %%
images

# %%
res =[]
im_count = 0
for line in contents.split("\n"):
    if "-i" in line and im_count < len(images):
        line = f"\n![](./{images[im_count]})\n"
        im_count+=1
    res.append(line)

"\n".join(res)

with open("test.md","w") as phile:
    phile.write("\n".join(res))
# %%
[os.remove(i) for i in os.listdir() if "Screenshot" in i]

# %%
