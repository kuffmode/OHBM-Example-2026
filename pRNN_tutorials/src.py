import numpy as np
import matplotlib.pyplot as plt
plt.style.use("./style_sheet.mplstyle")

def create_pRNN_adj_matrix(wm_flag): 
    """ 
    Creates an adjacency matrix for a given pRNN architecture. 
    Arguments: 
        wm_flag: a 7 element binary vector, which includes or excludes each additional connection.
            Order: ii, hh, oo, io, oi, hi, oh. 
            [0,0,0,0,0,0,0] = a feedforward architecture.
            [0,1,0,0,0,0,0] = a standard RNN.
            [1,1,1,1,1,1,1] = a fully recurrent architecture.
    Returns: 
        W: a binary matrix (3,3) with connections (1) between (source, target). 
            So W[src, tgt] = 1 means: an connection from neuron src → neuron tgt.
    """

    W = np.zeros((3, 3))

    i, h, o = slice(0,1), slice(1,2), slice(2,3)

    W[i, h] = 1
    W[h, o] = 1

    if wm_flag[0]: 
        W[i, i] = 1
    if wm_flag[1]:  
        W[h, h] = 1
    if wm_flag[2]: 
        W[o, o] = 1
    if wm_flag[3]:  
        W[i, o] = 1
    if wm_flag[4]:  
        W[o, i] = 1
    if wm_flag[5]:  
        W[h, i] = 1
    if wm_flag[6]:  
        W[o, h] = 1

    return W 

def plot_pRNN_architecture(wm_flag, ax=None, color=None):
    """
    Plots a pRNN architecture.
    Arguments:
        wm_flag: a 7 element binary vector, which includes or excludes each additional weight matrix.
        ax: a matplotlib axis (only needed if a color is provided)
        color: when provided, the whole architecture will be drawn with one color.
    """
    # ih and ho
    plt.scatter(x=[0, 1, 2], y=[1, 1, 1], color="xkcd:slate grey", zorder=1)
    plt.plot([0, 2], [1, 1], color="xkcd:slate grey", zorder=1)
    plt.arrow(
        0.35, 1, dx=0.1, dy=0.0, width=0.0, head_width=0.1, color="xkcd:slate grey"
    )
    plt.arrow(
        1.35, 1, dx=0.1, dy=0.0, width=0.0, head_width=0.1, color="xkcd:slate grey"
    )

    # ii, hh, oo
    for l in range(3):
        if wm_flag[l]:
            plt.plot([l, l], [0.75, 1.25], color="xkcd:teal blue", zorder=0)
            plt.arrow(
                l,
                0.9,
                dx=0.0,
                dy=-0.1,
                width=0.0,
                head_width=0.1,
                color="xkcd:teal blue",
            )
            plt.arrow(
                l,
                1.1,
                dx=0.0,
                dy=0.1,
                width=0.0,
                head_width=0.1,
                color="xkcd:teal blue",
            )

    if wm_flag[3]:  # io
        plt.plot([0.1, 1.9], [1.5, 1.5], color="xkcd:topaz", zorder=0)
        plt.arrow(
            0.85, 1.5, dx=0.1, dy=0.0, width=0.0, head_width=0.1, color="xkcd:topaz"
        )

    if wm_flag[4]:  # oi
        plt.plot([0.1, 1.9], [0.5, 0.5], color="xkcd:topaz", zorder=0)
        plt.arrow(
            1.15, 0.5, dx=-0.1, dy=0.0, width=0.0, head_width=0.1, color="xkcd:topaz"
        )

    if wm_flag[5]:  # hi
        plt.plot([0.1, 0.9], [1.25, 1.25], color="xkcd:orange", zorder=0)
        plt.arrow(
            0.67, 1.25, dx=-0.1, dy=0.0, width=0.0, head_width=0.1, color="xkcd:orange"
        )

    if wm_flag[6]:  # oh
        plt.plot([1.1, 1.9], [0.75, 0.75], color="xkcd:orange", zorder=0)
        plt.arrow(
            1.67, 0.75, dx=-0.1, dy=0.0, width=0.0, head_width=0.1, color="xkcd:orange"
        )

    plt.ylim([0.25, 1.75])
    plt.axis("off")

    if color:
        for line in ax.get_lines():
            line.set_color(color)

        for patch in ax.patches:
            patch.set_facecolor(color)
            patch.set_edgecolor(color)

        for path_collection in ax.collections:
            path_collection.set_facecolor(color)
            path_collection.set_edgecolor(color)

def plot_pRNN_dynamics(x_hist):
    """
    Plots pRNN dynamics over time. 
    Arguments:
        x_hist: an array of dynamics, (architectures, time, nodes). 
    """

    cols = ["xkcd:light grey", "xkcd:purple", "xkcd:spearmint"]
    labels = ["Input", "Hidden", "Output"]

    fig, ax = plt.subplots(
        nrows=8, ncols=16, figsize=(30, 15),
        sharex=True, sharey=True
    )

    t = np.arange(x_hist.shape[1])
    for a, _ in enumerate(ax.ravel()):
        plt.sca(ax.ravel()[a])

        plt.plot(t, x_hist[a, :, 0], color=cols[0], lw=2)
        plt.plot(t, x_hist[a, :, 1], color=cols[1], lw=2)
        plt.plot(t, x_hist[a, :, 2], color=cols[2], lw=2)
        ax.ravel()[a].axis("off")

# # Video 

# cmap = colors.LinearSegmentedColormap.from_list(
#     "",[(0.0, "white"),(1.0, "xkcd:spearmint")])

# fig, ax = plt.subplots(nrows=8, ncols=16, figsize=(30,15), sharex=True, sharey=True)

# # Architectures
# for a, _ in enumerate(ax.ravel()):
#     plt.sca(ax.ravel()[a])
#     plot_pRNN_architecture(wm_flags[ind[a]], ax=ax.ravel()[a], color='xkcd:light grey')

# # Initialise nodes 
# arch_animations = []
# for a in range(len(x_hist)):
#     markers = [[], [], []]
#     for b in range(3):
#         markers[b] = ax.ravel()[a].scatter(b, 1, edgecolor='white', c='white', s=120)
#     arch_animations.append(markers)

# # Animate 
# def update_animation(t):
#     for a in range(len(x_hist)):
#         for b in range(3):
#             arch_animations[a][b].set_facecolor(cmap(x_hist[ind[a], t, b]))
#             arch_animations[a][b].set_edgecolor(cmap(x_hist[ind[a], t, b]))

# anim = animation.FuncAnimation(fig, update_animation, frames=range(0, x_hist.shape[1]), blit=False)
# anim.save("Meep_dynamics_norm.gif", dpi=300, fps=6)