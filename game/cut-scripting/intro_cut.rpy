# Show a background. This uses a placeholder by default, but you can
# add a file (named either "bg room.png" or "bg room.jpg") to the
# images directory to show it.

scene bg room

"Temporary text" "The text that's in here now is just a placeholder. But if we make the text really long then we can see the effect of it on this textbox design, which may or not be as we desire."

#This is just to test that the sprites for Marshall are displaying properly.
show marshall annoyed at center:
    zoom 0.2

play sound beaming
m "I should be annoyed."

play sound penclick
#show m smile
m smile "But now I smile."