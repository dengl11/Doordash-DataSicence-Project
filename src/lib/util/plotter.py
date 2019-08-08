#######################
###   Plot Utility  ###
#######################

# disable logging from matplotlib
import logging
logging.getLogger("matplotlib.pyplot").setLevel(logging.WARNING)
logging.getLogger("matplotlib.font_manager").setLevel(logging.WARNING)

from . import df_ops, logger
import numpy as np
import itertools
# import pygraphviz as graphviz
# from graphviz import Graph
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import warnings 
warnings.filterwarnings("ignore")
from matplotlib.ticker import MaxNLocator
from sklearn.manifold import TSNE

import seaborn as sns
import matplotlib.pyplot as plt
sns.set_context("notebook", font_scale=1.2, \
        rc={"font.size":12 ,"axes.titlesize": 10,"axes.labelsize":10, "axes.xticks.size": 8, "lines.linewidth": 2.5})
sns.set_style("white")
current_palette = sns.color_palette("Paired")
# Ref: http://seaborn.pydata.org/tutorial/color_palettes.html
# ['#e6f6e1', '#d7efd1', '#c6e9c2', '#abdeb6', '#8bd2bf', '#6bc3c9', '#4bb0d1', '#3192c1', '#1878b4', '#085da0']
# ['#ab162a', '#cf5246', '#eb9172', '#fac8af', '#feefe6', '#f1f1f1', '#d3d3d3', '#ababab', '#7c7c7c', '#484848']
# ['#ab162a', '#cf5246', '#eb9172', '#fac8af', '#faeae1', '#e6eff4', '#bbdaea', '#7bb6d6', '#3c8abe', '#1e61a5']
# ['#19122b', '#17344c', '#185b48', '#3c7632', '#7e7a36', '#bc7967', '#d486af', '#caa9e7', '#c2d2f3', '#d6f0ef']
# ['#a6cee3', '#1f78b4', '#b2df8a', '#33a02c', '#fb9a99', '#e31a1c', '#fdbf6f', '#ff7f00', '#cab2d6', '#6a3d9a']

gray = '#ababab'
blue = '#7bb6d6'
green ='#b2df8a'
light_purple = '#cab2d6'
purple = '#6a3d9a'
red = '#ab162a'
pink = '#cf5246'
orange = '#fdbf6f'
black = "#000000"

yellow = '#FFD92F'

palette_dict = {'green': green, 'gray': gray, 'blue': blue, 'red': '#ab162a', 'yellow': yellow, 'purple': purple, "pink": pink}
default_palette = [green, blue, gray]

myLogger = logger.ColoredLogger("plotter")

###########################################################
###############       Plot Toolkit        #################
###########################################################

# myLogger = ColoredLogger("Plot")

def set_axis_tick_size(ax, axis, size):
    """rotate axis ticks 
    """
    # ticks = ax.xaxis if axis == "x" else ax.yaxis
    # print(len(ticks.get_major_ticks()))
    ticks = ax.get_xticklabels() if axis == "x" else ax.get_yticklabels()
    for tick in ticks:
        tick.set_fontsize(angle)

def rotate_axis_ticks(ax, axis, angle):
    """rotate axis ticks 
    """
    ticks = ax.get_xticklabels() if axis == "x" else ax.get_yticklabels()
    for tick in ticks:
        tick.set_rotation(angle)

def ax_set_title(ax, title, size=12, weight='bold', color='gray'):
    """
    ax: matplotlib axes
    """
    ax.axes.set_title(title, size=size, color=color, weight=weight)
    return ax

def sns_set_title(title, size=12, weight='bold', color='gray'):
    """
    Args:
        title: 

    Return: 
    """
    plt.title(title, size=size, color=color, weight=weight)


def fig_set_title(fig, title, size=12, weight='bold', color='gray'):
    """
    Args:
    """
    return ax_set_title(fig.gca(), title, size, weight, color) 

def sns_countplot(data, feature, annotate=True, save_path=None, palette=default_palette):
    """
    data: dataframe
    feature: name of feature | string
    """
    plt.figure()
    assert feature in data.keys(), "{} not a feature of data!".format(feature)
    ax = sns.countplot(x = feature, data = data, palette=palette)
    if annotate:
        for p in ax.patches:
            ax.annotate(int(p.get_height()), (p.get_x() + p.get_width()/3, p.get_height()*1.01))
    title = "Count by {}".format(feature)
    ax_set_title(ax, title)
    if save_path:
        plt.savefig(save_path)
    return ax


def transform_palette(palette):
    """
    Args:
        palette: 

    Return: 
    """
    try:
        return [palette_dict[x] for x in palette]
    except Exception as e:
        return palette



def plot_confusion_matrix(cm, classes, normalize=False, title='Confusion matrix', save_path=None):
    """
    Input:
        cm     : confusion matrix
        classes: [class_name]
    """
    plt.figure()
    plt.imshow(cm, cmap='Purples')
    ax_set_title(plt.gca(), title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45, fontsize=16 )
    plt.yticks(tick_marks, classes,              fontsize=16 )

    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        cm = np.round(cm, 2)

    thresh = .8*cm.max() # minimal threshold for text to be white
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, cm[i, j], fontsize=16, horizontalalignment="center", color="white" if cm[i, j] > thresh else "black")

    plt.ylabel('True label',      fontsize=16 )
    plt.xlabel('Predicted label', fontsize=16 )
    plt.tight_layout() 
    if save_path:
        plt.savefig(save_path) 


def hbar_plot(yticks, y, xlabel, ylabel, title, **kwargs):
    """
    Args:
        xticks:  [tick]
        y:       [val] 
        xlabel:  str     
        y_label: str     
        save_path:  path to save fig
    Return:
        axes
    """
    size = kwargs.get('size', None)
    save_path = kwargs.get('save_path', None)
    ylabels = kwargs.get('ylabels', None)
    y_arr = kwargs.get('y_arr', None)
    xtick_rot = kwargs.get('xtick_rot', None)
    ytick_rot = kwargs.get('ytick_rot', None)
    color = kwargs.get('color', "green")
    color = get_color(color) 

    if size: fig = plt.figure(figsize=size)
    else:    fig = plt.figure()

    n = len(yticks)
    plt.barh(range(n), y, color=color)
        
    fig_set_title(fig, title)
    plt.yticks(range(n), yticks if ylabels is None else ylabels)
    plt.ylabel(ylabel, fontsize=10)
    plt.xlabel(xlabel, fontsize=10)
    ax =  plt.gca()

    if xtick_rot: rotate_axis_ticks(ax, "x", xtick_rot)
    if ytick_rot: rotate_axis_ticks(ax, "y", ytick_rot)

    plt.tight_layout()
    if save_path:
        plt.savefig(save_path)

    return plt.gca()


def bar_plot(xticks, y, xlabel = None, ylabel = None, title = None, **kwargs):
    """
    Args:
        xticks:  [tick]
        y:       [val] 
        xlabel:  str     
        y_label: str     
    Return:
        axes
    """
    if kwargs.get('new', True):
        plt.figure()
    save_path = kwargs.get('save_path', None)
    xlabels = kwargs.get('xlabels', None)
    y_arr = kwargs.get('y_arr', None)
    fig = plt.figure()
    n = len(xticks)
    plt.bar(range(n), y, color=light_purple)
        
    fig_set_title(fig, title)
    plt.xticks(range(n), xticks if xlabels is None else xlabels, rotation = 45)
    plt.ylabel(ylabel, fontsize=16)
    plt.xlabel(xlabel, fontsize=16)
    plt.tight_layout()
    ax =  plt.gca()
    if ( y_arr is not None ):
        for i in range( len( ax.patches ) ):
            p = ax.patches[i]
            ax.annotate(int(y_arr[i]), (p.get_x() + p.get_width()/3, p.get_height()*1.01))

    legend = kwargs.get('legend', [])
    if legend:
        plt.legend(legend)
    if save_path:
        plt.savefig(save_path)

    return plt.gca()

def scatter_plot(x, y, **kwargs):
    """
    Args:
        y:       [val]
        xlabel:  str
        y_label: str
        save_path:  path to save fig
    Return:
        axes
    """
    size = kwargs.get('size', None)
    save_path = kwargs.get('save_path', None)
    title = kwargs.get('title', "")
    ylabels = kwargs.get('ylabels', None)
    annotations = kwargs.get("annotations", [])

    fig = plt.figure()
    plt.scatter(x, y)
    fig_set_title(fig, title)
    # plt.ylabel(ylabel, fontsize=16)
    # plt.xlabel(xlabel, fontsize=16)
    plt.tight_layout()
    ax = plt.gca()

    for i, anno in enumerate(annotations):
        xi, yi = x[i], y[i]
        ax.annotate(anno, (xi, yi))
    if save_path:
        plt.savefig(save_path)
        myLogger.info("Figure saved at: {}".format(save_path))
    return ax



def stack_label_distribution(labels, x, feature_name, y_encoder,  n=200, size=(16, 6), ylabel="Number of Cases", kind = "bar"):
    target_win   = y_encoder.transform(["Won"])[0]
    target_lost  = y_encoder.transform(["Lost"])[0]
    target_cancel  = y_encoder.transform(["Cancelled"])[0]
    pairs = list(zip(x, labels))
    x_min, x_max = min(pairs)[0], max(pairs)[0]
    print('X Range: ({}, {})'.format(x_min, x_max))
    
    interval = (x_max - x_min)/n
    x_arr = list(x_min + i * interval for i in range(n+1))
    wins = [0]*(n+1)
    lost = wins[:]
    canceled = wins[:]
    offset = interval/4
    for (e, label) in pairs:
        ind = int((e-x_min)//interval)
        if   label == target_win:    wins[ind] += 1
        elif label == target_lost:   lost[ind] += 1
        elif label == target_cancel: canceled[ind] += 1
    fig = plt.figure(figsize=size)
    ax = plt.gca()
    plt.ylabel(ylabel, fontsize=16)
    plt.xlabel(feature_name, fontsize=16)
    xlabels = np.array(x_arr)
    plt.xticks(x_arr, xlabels.astype('int'), rotation = 45)
    if kind == "bar":
        rec2 = plt.bar(x_arr, lost,  width=offset)
        rec1 = plt.bar(list(xlabels-offset), wins, width=offset)
        rec3 = plt.bar(list(xlabels+offset), canceled, width=offset)
        autolabel(ax, rec1)
        # autolabel(ax, rec2)
        # autolabel(ax, rec3)
    else:
        rec2 = plt.plot(x_arr, lost, linewidth=4)
        rec1 = plt.plot(list(xlabels-offset), wins, linewidth=4)
        rec3 = plt.plot(list(xlabels+offset), canceled, linewidth=4)

    plt.legend(["Win", "Lost", "Cancelled"])
    plt.show()

def autolabel(ax, rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 0.5*height,
                '%d' % int(height),
                ha='center', va='bottom')




def sns_pairplot(dataframe, features, target_feature, save_path=None, size=4, palette = default_palette):
    """
    Args:
        dataframe: 
        features: 

    Return: 
    """
    fig = plt.figure()
    ax = sns.pairplot(dataframe, hue=target_feature,  vars=features, size=size, palette = palette)
    plt.gcf().suptitle("Correlation", weight="bold", color="gray", fontsize=12, y = 1.01)
    plt.tight_layout() 
    if save_path: ax.fig.savefig(save_path)
    return ax

def sns_line_plot(dataframe, x_feature, y_feature, **kwargs):
    """
    Args:
        dataframe: 
        x_feature: 
        y_feature: 
        conf: 

    Return: 
    """
    palette = kwargs.get("palette", None)
    save_path = kwargs.get("save_path", None)
    title = kwargs.get("title", "")
    xtick_rot = kwargs.get("xtick_rot", None)
    fontscale = kwargs.get('fontscale', None)
    if fontscale: sns.set(font_scale = fontscale) 
    if palette: palette = transform_palette(palette)

    plt.figure()
    ax = sns.lineplot(x_feature, y_feature,
                      data=dataframe,
                      )  

    if xtick_rot: rotate_axis_ticks(ax, "x", xtick_rot)
    sns_set_title(title)
    plt.tight_layout() 
    if save_path:
        ax.get_figure().savefig(save_path)
        myLogger.info("Figure saved at: {}".format(save_path))
    return ax


def sns_bar_plot(dataframe, x_feature, y_feature, **kwargs):
    """
    Args:
        dataframe: 
        x_feature: 
        y_feature: 
        conf: 

    Return: 
    """
    palette = kwargs.get("palette", None)
    save_path = kwargs.get("save_path", None)
    title = kwargs.get("title", "")
    xtick_rot = kwargs.get("xtick_rot", None)
    fontscale = kwargs.get('fontscale', None)
    if fontscale: sns.set(font_scale = fontscale) 
    if palette: palette = transform_palette(palette)

    plt.figure()
    ax = sns.barplot(x_feature, y_feature, data=dataframe, capsize= 0.2, palette=palette)  

    if xtick_rot: rotate_axis_ticks(ax, "x", xtick_rot)
    sns_set_title(title)
    plt.tight_layout() 
    if save_path:
        ax.get_figure().savefig(save_path)
        myLogger.info("Figure saved at: {}".format(save_path))
    return ax

def distribution_plot(data, **kwargs):
    """
    Return: 
    """
    bins = kwargs.get('bins', 10)
    xlim = kwargs.get('xlim', '')
    ylim = kwargs.get('ylim', '')
    xlabel = kwargs.get('xlabel', '')
    ylabel = kwargs.get('ylabel', '')
    title = kwargs.get('title', '')
    save_path = kwargs.get('save_path', None)

    # Histogram
    heights,bins = np.histogram(data, bins=bins)
    # Normalize
    heights = heights/float(sum(heights))
    binMids=bins[:-1]+np.diff(bins)/2.
    plt.hist(data)
    ax = plt.gca()
    ax.set_ylabel(ylabel, fontsize=10)
    ax_set_title(ax, title)
    ax.set(xlim=xlim)
    ax.set(ylim=ylim)
    plt.tight_layout() 
    if save_path: ax.get_figure().savefig(save_path)
    return ax

def sns_dist_plot(vals, ylim=None, xlim=None, color='green', **kwargs):
    """
    Args:
        vals: 
        xlabel: 
        ylabel: 
        title: 
    """
    plt.figure()
    normalize = kwargs.get('normalize', False)
    vertical = kwargs.get('vertical', False)
    xlabel = kwargs.get('xlabel', '')
    ylabel = kwargs.get('ylabel', '')
    title = kwargs.get('title', '')
    save_path = kwargs.get('save_path', None)
    plot_mean = kwargs.get('plot_mean', False)
    cumulative = kwargs.get('cumulative', False)
    ax = sns.distplot(vals, color=palette_dict[color], norm_hist=normalize, hist_kws = {'cumulative': cumulative}, vertical=vertical)

    if plot_mean: 
        m = np.round(np.mean(vals), 2)  # mean 
        plt.axvline(m, color='r')
        ax.set_xlabel(xlabel + " ( $\mu$={} ) ".format(m), fontsize=10)

    ax.set_ylabel(ylabel, fontsize=12)
    ax.set_xlabel(xlabel, fontsize=12)
    ax_set_title(ax, title)
    ax.set(xlim=xlim)
    ax.set(ylim=ylim)
    plt.tight_layout() 
    if save_path: ax.get_figure().savefig(save_path)
    return ax


def get_color(color):
    """ return hex for color 
    Args:
        color: 

    Return: 
    """
    return palette_dict[color]


def curve_plot(xs, ys, **kwargs):
    """plot (x, y)
    Args:
        xs: 
        ys: 

    Return: 
    """
    sns.set_style("darkgrid")
    if kwargs.get('new', True):
        fig = plt.figure()

    color = kwargs.get('color', "green")
    color = get_color(color)

    ax = plt.plot(xs, ys, color=color)
    ax = plt.gca() 
    ax_set_title(ax, kwargs.get('title', ''))
    ax.set_xlabel(kwargs.get('xlabel', ''), fontsize=12)
    ax.set_ylabel(kwargs.get('ylabel', ''), fontsize=12)
    legend = kwargs.get('legend', [])
    if legend:
        plt.legend(legend)
    if kwargs.get('show', False): plt.show()

    save_path = kwargs.get('save_path', None)
    if save_path:
        ax.get_figure().savefig(save_path)
        myLogger.info("Figure saved at: {}".format(save_path))
    return ax 

def sns_heatmap(matrix, **kwargs):
    """plot seaborn heatmap
    Args:
        matrix: 2D np array 
        **kwargs: 

    Return: 
    """
    size = kwargs.get('size', None)
    if size: fig = plt.figure(figsize=size)
    else:    fig = plt.figure()

    save_path = kwargs.get('save_path', None)
    ylabels = kwargs.get('ylabels', None)
    y_arr = kwargs.get('y_arr', None)
    xtick_rot = kwargs.get('xtick_rot', None)
    ytick_rot = kwargs.get('ytick_rot', None)
    xticklabels = kwargs.get('xticklabels', None)
    yticklabels = kwargs.get('yticklabels', None) 
    annotations = kwargs.get('annot', False) 
    fmt = kwargs.get('fmt', '') 
    fontscale = kwargs.get('fontscale', None)
    if fontscale: sns.set(font_scale = fontscale)

    ax = sns.heatmap(matrix, cmap="YlGnBu",
                     annot = annotations,
                     xticklabels = xticklabels,
                     fmt = fmt,
                     yticklabels=yticklabels)

    ax_set_title(ax, kwargs.get('title', ''))
    ax.set_xlabel(kwargs.get('xlabel', ''), fontsize=10)
    ax.set_ylabel(kwargs.get('ylabel', ''), fontsize=10)

    if xtick_rot: rotate_axis_ticks(ax, "x", xtick_rot)
    if ytick_rot: rotate_axis_ticks(ax, "y", ytick_rot)
    if kwargs.get('tight', True): plt.tight_layout() 

    if save_path: ax.get_figure().savefig(save_path)
    return ax 



def sns_clustermap(df, **kwargs):
    """plot seaborn cluster map 
    Args:
        matrix: 2D np array 
        **kwargs: 

    Return: 
    """
    size = kwargs.get('size', None)
    if size: fig = plt.figure(figsize=size)
    else:    fig = plt.figure()

    save_path = kwargs.get('save_path', None)
    ylabels = kwargs.get('ylabels', None)
    y_arr = kwargs.get('y_arr', None)
    xtick_rot = kwargs.get('xtick_rot', None)
    ytick_rot = kwargs.get('ytick_rot', None)
    xticklabels = kwargs.get('xticklabels', [])
    yticklabels = kwargs.get('yticklabels', [])
    fontscale = kwargs.get('fontscale', None)
    if fontscale: sns.set(font_scale = fontscale)


    g = sns.clustermap(df.corr(),
                    xticklabels = xticklabels,
                    yticklabels=yticklabels,
                    metric=kwargs.get('metric', "correlation"),
                    cmap="vlag")
                                                                                   
    ax = plt.gca()

    ax_set_title(ax, kwargs.get('title', ''))
    # NOT WORKING
    # -------
    # ax.set_xlabel(kwargs.get('xlabel', ''), fontsize=12)
    # ax.set_ylabel(kwargs.get('ylabel', ''), fontsize=12)
    # -------

    if xtick_rot: 
        plt.setp(g.ax_heatmap.get_xticklabels(), rotation=xtick_rot)
    if ytick_rot: 
        plt.setp(g.ax_heatmap.get_yticklabels(), rotation=ytick_rot)
        myLogger.info("Figure saved at: {}".format(save_path))

    plt.tight_layout() 

    if save_path:
        ax.get_figure().savefig(save_path)
        myLogger.info("Figure saved at: {}".format(save_path))
    return ax 

def force_axis_integer(ax, x = True):
    """
    Args:
        ax: 

    Return: 
    """
    if x:
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    else:
        ax.yaxis.set_major_locator(MaxNLocator(integer=True))

def sns_scatter_plot(dataframe, **kwargs):
    """
    Args:
        dataframe: df(x: [...], y:[...]) 

    Return: 
    """
    size = kwargs.get('size', None)
    if size: fig = plt.figure(figsize=size)
    else:    fig = plt.figure()

    g = sns.regplot(x="x",
                    y="y",
                    color="skyblue",
                    fit_reg=False,
                    data=dataframe)
    annotations = kwargs.get("annotations", [])
    fontscale = kwargs.get('fontscale', None)
    if fontscale: sns.set(font_scale = fontscale)
    for i, anno in enumerate(annotations):
        x, y = dataframe.x[i], dataframe.y[i]
        g.text(x, y, anno,
                horizontalalignment='left',
                size='small',  # xx-small, medium
                color='gray',
                weight='light')

    save_path = kwargs.get("save_path", None)
    if save_path:
        plt.savefig(save_path)
        myLogger.info("Figure saved at: {}".format(save_path))


def tsne_scatter(X, **kwargs):
    """
    Args:
        X: np array [nSample x nFeature]

    Return: 
    """
    init = kwargs.get("init", "pca")
    tsne = TSNE(n_components=2,
                init=init,
                n_iter = kwargs.get("n_iter", 1000),
                random_state=0)
    Embedding = tsne.fit_transform(X) # [nSample x 2]
    # scatter_plot(Embedding[:, 0], Embedding[:,1], **kwargs)
    df = df_ops.mat2df(Embedding, ["x", "y"])
    sns_scatter_plot(df, **kwargs)
    
