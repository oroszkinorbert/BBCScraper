import json
from urllib.request import urlopen

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from highlight_text import fig_text

from mplsoccer import Bumpy, FontManager, add_image

Goals=[]
xG=[]

font_normal = FontManager("https://raw.githubusercontent.com/google/fonts/main/apache/"
                          "roboto/Roboto%5Bwdth,wght%5D.ttf")
font_bold = FontManager("https://raw.githubusercontent.com/google/fonts/main/apache/"
                        "robotoslab/RobotoSlab%5Bwght%5D.ttf")

epl = Image.open(
    urlopen("https://raw.githubusercontent.com/andrewRowlinson/mplsoccer-assets/main/epl.png")
)

season_dict = json.load(
    urlopen("https://raw.githubusercontent.com/andrewRowlinson/mplsoccer-assets/main/epl.json")
)

player_dict = json.load(
    urlopen("https://raw.githubusercontent.com/andrewRowlinson/mplsoccer-assets/main/"
            "percentile.json")
)


# match-week
match_day = ["Week " + str(num) for num in range(1, 39)]

# highlight dict --> team to highlight and their corresponding colors
highlight_dict = {
    "xG": "crimson",
    "Goals": "gold"
}

# instantiate object
bumpy = Bumpy(
    scatter_color="#282A2C", line_color="#252525",  # scatter and line colors
    rotate_xticks=45,  # rotate x-ticks by 90 degrees
    ticklabel_size=20, label_size=30,  # ticklable and label font-size
    scatter_primary='D',  # marker to be used
    show_right=True,  # show position on the rightside
    plot_labels=True,  # plot the labels
    alignment_yvalue=0.4,  # y label alignment
    alignment_xvalue=0.5  # x label alignment
)

# plot bumpy chart
fig, ax = bumpy.plot(
    x_list=match_day,  # match-day or match-week
    y_list=np.linspace(1, 40, 40).astype(float),  # position value from 1 to 20
    values=season_dict,  # values having positions for each team
    secondary_alpha=0.5,   # alpha value for non-shaded lines/markers
    highlight_dict=highlight_dict,  # team to be highlighted with their colors
    figsize=(40, 26),  # size of the figure
    x_label='Week',
    y_label='Goals and Expected Goals',  # label name
    ylim=(-0.1, 40),  # y-axis limit
    lw=2.5,   # linewidth of the connecting lines
    fontproperties=font_normal.prop,   # fontproperties for ticklables/labels
    upside_down=True
)

# title and subtitle
TITLE = "Erling Haaland week-wise Goals and xG in Premier League:"
SUB_TITLE = "A comparison between <xG> and <Goals> of Erling Haaland in Premier League 22/23"

# add title
fig.text(0.11, 0.95, TITLE, size=29, color="#F2F2F2", fontproperties=font_bold.prop)

# add subtitle
fig_text(
    0.11, 0.94, SUB_TITLE, color="#F2F2F2",
    highlight_textprops=[{"color": 'crimson'}, {"color": 'gold'}],
    size=25, fig=fig, fontproperties=font_bold.prop
)

# add image
fig = add_image(
     epl,
     fig,  # figure
     0.01, 0.89,  # left and bottom dimensions
     0.1, 0.1  # height and width values
)

# if space is left in the plot use this
plt.tight_layout(pad=1)