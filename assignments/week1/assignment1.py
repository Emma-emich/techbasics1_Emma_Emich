#%%
# ASCII Art: A cute sitting cat
# Reference: Designed manually, character by character
# Tip: use raw strings (r"") to avoid fighting with backslashes!

def draw_cat():
    # The ears and head
    print(r"  /\_/\  ")    # pointy ears using / \ _

    # The face - eyes and nose
    print(r" ( o.o ) ")    # round face with 'o' eyes

    # The mouth/chin area
    print(r"  > ^ <  ")    # whiskers > < and a tiny nose ^

    # The paws
    print(r" (__|__) ")    # little paws at the bottom

draw_cat()
#%%
# flower
def draw_flower():
    print(r"""
                       __/)
                    .-(__(=:
                    |    \)
              (\__  |
             :=)__)-|  __/)
              (/    |-(__(=:
            ______  |  _ \)
           /      \ | / \
                   \|/   \
                ____|____ \
               [         ] \
                \       /   \
                 \     /
                  \___/
                  """)

draw_flower()