# coding=utf8
"""
4 basic kind of plots:
---
1. scatter plot
2. histogram
3. bar plot
4. box plot
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import matplotlib.mlab as mlab
import matplotlib.patches as patches
import matplotlib.path as path

x = np.arange(0.0, 2.0, 0.02)
y1 = np.sin(2 * np.pi * x)
y2 = np.exp(-x)
y3 = np.sin(4 * np.pi * x)
y4 = np.exp(-2 * x)


def plot_by_axes():
    fig = plt.figure()
    # plot A
    ax1 = fig.add_axes([0.1, 0.1, 0.4, 0.7])
    l1, l2 = ax1.plot(x, y1, 'rs-', x, y2, 'go')
    fig.legend((l1, l2), ('Line 1', 'Line 2'), 'upper left', borderpad=1, handlelength=2, handleheight=2,
               labelspacing=2, fontsize='8', markerscale=0.8)
    # plot B
    ax2 = fig.add_axes([0.55, 0.1, 0.4, 0.7])
    l3, l4 = ax2.plot(x, y3, 'yd-', x, y4, 'k^')
    fig.legend((l3, l4), ('Line 3', 'Line 4'), 'upper right')

    plt.show()


def subplot_demo():
    fig = plt.figure()
    # plot A
    ax1 = fig.add_subplot(1, 2, 1)
    l1, l2 = ax1.plot(x, y1, 'rs-', x, y2, 'go')
    fig.legend((l1, l2), ('Line 1', 'Line 2'), 'upper left', borderpad=1, handlelength=2, handleheight=2,
               labelspacing=2, fontsize='8', markerscale=0.8)
    # plot B
    ax2 = fig.add_subplot(1, 2, 2)
    l3, l4 = ax2.plot(x, y3, 'yd-', x, y4, 'k^')
    fig.legend((l3, l4), ('Line 3', 'Line 4'), 'upper right')

    plt.show()


def stack_plot():
    x = [1, 2, 3, 4, 5]
    y1 = [1, 1, 2, 3, 5]
    y2 = [0, 4, 2, 6, 8]
    y3 = [1, 3, 5, 7, 9]

    y = np.vstack([y1, y2, y3])

    labels = ["Fibonacci ", "Evens", "Odds"]

    fig, ax = plt.subplots()
    ax.stackplot(x, y1, y2, y3, labels=labels)
    ax.legend(loc=2)

    fig, ax = plt.subplots()
    ax.stackplot(x, y)
    plt.show()


class ScatterPlotDemo:
    def __init__(self):
        print("---scatter plot demo")
        pass

    def basic(self):
        print("***basic sample")
        x_data = np.random.randint(0, 10, size=10)
        y_data = np.random.randint(0, 10, size=10)
        x_label = "x axis"
        y_label = "y axis"
        title = "scatter plot (basic)"
        color = "r"
        yscale_log = False
        # Create the plot object
        fig, ax = plt.subplots()
        # Plot the data, set the size (s), color and transparency (alpha)
        # of the points
        ax.scatter(x_data, y_data, s=10, color=color, alpha=0.75)
        if yscale_log == True:
            ax.set_yscale('log')
        # Label the axes and provide a title
        ax.set_title(title)
        ax.set_xlabel(x_label)
        ax.set_ylabel(y_label)
        plt.show()

    def advanced(self):
        print("advanced sample")
        # Load a numpy record array from yahoo csv data with fields date, open, close,
        # volume, adj_close from the mpl-data/example directory. The record array
        # stores the date as an np.datetime64 with a day unit ('D') in the date column.
        with cbook.get_sample_data('goog.npz') as datafile:
            price_data = np.load(datafile)['price_data'].view(np.recarray)
        price_data = price_data[-250:]  # get the most recent 250 trading days

        delta1 = np.diff(price_data.adj_close) / price_data.adj_close[:-1]

        # Marker size in units of points^2
        volume = (15 * price_data.volume[:-2] / price_data.volume[0]) ** 2
        close = 0.003 * price_data.close[:-2] / 0.003 * price_data.open[:-2]

        fig, ax = plt.subplots()
        ax.scatter(delta1[:-1], delta1[1:], c=close, s=volume, alpha=0.5)

        ax.set_xlabel(r'$\Delta_i$', fontsize=15)
        ax.set_ylabel(r'$\Delta_{i+1}$', fontsize=15)
        ax.set_title('Volume and percent change')

        ax.grid(True)
        fig.tight_layout()

        plt.show()


class HistogramDemo:
    def __init__(self):
        print("---histogram demo")
        pass

    def basic(self):
        np.random.seed(19680801)

        # example data
        mu = 100  # mean of distribution
        sigma = 15  # standard deviation of distribution
        x = mu + sigma * np.random.randn(437)

        num_bins = 50

        fig, ax = plt.subplots()

        # the histogram of the data
        n, bins, patches = ax.hist(x, num_bins, normed=1)

        # add a 'best fit' line
        y = mlab.normpdf(bins, mu, sigma)
        ax.plot(bins, y, '--')
        ax.set_xlabel('Smarts')
        ax.set_ylabel('Probability density')
        ax.set_title(r'Histogram of IQ: $\mu=100$, $\sigma=15$')

        # Tweak spacing to prevent clipping of ylabel
        fig.tight_layout()
        plt.show()

    def plot_beta_hist(self, ax, a, b):
        ax.hist(np.random.beta(a, b, size=10000), histtype="stepfilled", bins=25, alpha=0.8, normed=True)

    def overlaid_plot(self):
        plt.style.use('bmh')

        fig, ax = plt.subplots()
        self.plot_beta_hist(ax, 10, 10)
        self.plot_beta_hist(ax, 4, 12)
        self.plot_beta_hist(ax, 50, 12)
        self.plot_beta_hist(ax, 6, 55)
        ax.set_title("'bmh' style sheet")

        plt.show()

    def rectangle_hist(self):
        fig, ax = plt.subplots()

        # Fixing random state for reproducibility
        np.random.seed(19680801)

        # histogram our data with numpy

        data = np.random.randn(1000)
        n, bins = np.histogram(data, 50)

        # get the corners of the rectangles for the histogram
        left = np.array(bins[:-1])
        right = np.array(bins[1:])
        bottom = np.zeros(len(left))
        top = bottom + n

        # we need a (numrects x numsides x 2) numpy array for the path helper
        # function to build a compound path
        XY = np.array([[left, left, right, right], [bottom, top, top, bottom]]).T

        # get the Path object
        barpath = path.Path.make_compound_path_from_polys(XY)

        # make a patch out of it
        patch = patches.PathPatch(barpath)
        ax.add_patch(patch)

        # update the view limits
        ax.set_xlim(left[0], right[-1])
        ax.set_ylim(bottom.min(), top.max())

        plt.show()


class BarplotDemo:
    def __init__(self):
        print("---bar plot demo")

    def basic(self):
        data = ((3, 1000), (10, 3), (100, 30), (500, 800), (50, 1))

        dim = len(data[0])
        w = 0.75
        dimw = w / dim

        fig, ax = plt.subplots()
        x = np.arange(len(data))
        for i in range(len(data[0])):
            y = [d[i] for d in data]
            b = ax.bar(x + i * dimw, y, dimw, bottom=0.001)

        ax.set_xticks(x + dimw / 2, map(str, x))
        ax.set_yscale('log')

        ax.set_xlabel('x')
        ax.set_ylabel('y')

        plt.show()

    def stacked(self):
        N = 5
        menMeans = (20, 35, 30, 35, 27)
        womenMeans = (25, 32, 34, 20, 25)
        menStd = (2, 3, 4, 1, 2)
        womenStd = (3, 5, 2, 3, 3)
        ind = np.arange(N)  # the x locations for the groups
        width = 0.35  # the width of the bars: can also be len(x) sequence

        p1 = plt.bar(ind, menMeans, width, yerr=menStd)
        p2 = plt.bar(ind, womenMeans, width,
                     bottom=menMeans, yerr=womenStd)

        plt.ylabel('Scores')
        plt.title('Scores by group and gender')
        plt.xticks(ind, ('G1', 'G2', 'G3', 'G4', 'G5'))
        plt.yticks(np.arange(0, 81, 10))
        plt.legend((p1[0], p2[0]), ('Men', 'Women'))

        plt.show()

    def errbar(self):
        n_groups = 5

        means_men = (20, 35, 30, 35, 27)
        std_men = (2, 3, 4, 1, 2)

        means_women = (25, 32, 34, 20, 25)
        std_women = (3, 5, 2, 3, 3)

        fig, ax = plt.subplots()

        index = np.arange(n_groups)
        bar_width = 0.35

        opacity = 0.4
        error_config = {'ecolor': '0.3'}

        rects1 = ax.bar(index, means_men, bar_width,
                        alpha=opacity, color='b',
                        yerr=std_men, error_kw=error_config,
                        label='Men')

        rects2 = ax.bar(index + bar_width, means_women, bar_width,
                        alpha=opacity, color='r',
                        yerr=std_women, error_kw=error_config,
                        label='Women')

        ax.set_xlabel('Group')
        ax.set_ylabel('Scores')
        ax.set_title('Scores by group and gender')
        ax.set_xticks(index + bar_width / 2)
        ax.set_xticklabels(('A', 'B', 'C', 'D', 'E'))
        ax.legend()

        fig.tight_layout()
        plt.show()


class BoxplotDemo:
    def __init__(self):
        print("---box plot demo")

    def basics(self):
        # Fixing random state for reproducibility
        np.random.seed(19680801)

        # fake up some data
        spread = np.random.rand(50) * 100
        center = np.ones(25) * 50
        flier_high = np.random.rand(10) * 100 + 100
        flier_low = np.random.rand(10) * -100
        data = np.concatenate((spread, center, flier_high, flier_low), 0)

        fig, axs = plt.subplots(2, 3)

        # basic plot
        axs[0, 0].boxplot(data)
        axs[0, 0].set_title('basic plot')

        # notched plot
        axs[0, 1].boxplot(data, 1)
        axs[0, 1].set_title('notched plot')

        # change outlier point symbols
        axs[0, 2].boxplot(data, 0, 'gD')
        axs[0, 2].set_title('change outlier\npoint symbols')

        # don't show outlier points
        axs[1, 0].boxplot(data, 0, '')
        axs[1, 0].set_title("don't show\noutlier points")

        # horizontal boxes
        axs[1, 1].boxplot(data, 0, 'rs', 0)
        axs[1, 1].set_title('horizontal boxes')

        # change whisker length
        axs[1, 2].boxplot(data, 0, 'rs', 0, 0.75)
        axs[1, 2].set_title('change whisker length')

        fig.subplots_adjust(left=0.08, right=0.98, bottom=0.05, top=0.9,
                            hspace=0.4, wspace=0.3)

        # fake up some more data
        spread = np.random.rand(50) * 100
        center = np.ones(25) * 40
        flier_high = np.random.rand(10) * 100 + 100
        flier_low = np.random.rand(10) * -100
        d2 = np.concatenate((spread, center, flier_high, flier_low), 0)
        data.shape = (-1, 1)
        d2.shape = (-1, 1)

        plt.show()

    def colored(self):
        # Random test data
        np.random.seed(19680801)
        all_data = [np.random.normal(0, std, size=100) for std in range(1, 4)]
        labels = ['x1', 'x2', 'x3']

        fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(9, 4))

        # rectangular box plot
        bplot1 = axes[0].boxplot(all_data,
                                 vert=True,  # vertical box alignment
                                 patch_artist=True,  # fill with color
                                 labels=labels)  # will be used to label x-ticks
        axes[0].set_title('Rectangular box plot')

        # notch shape box plot
        bplot2 = axes[1].boxplot(all_data,
                                 notch=True,  # notch shape
                                 vert=True,  # vertical box alignment
                                 patch_artist=True,  # fill with color
                                 labels=labels)  # will be used to label x-ticks
        axes[1].set_title('Notched box plot')

        # fill with colors
        colors = ['pink', 'lightblue', 'lightgreen']
        for bplot in (bplot1, bplot2):
            for patch, color in zip(bplot['boxes'], colors):
                patch.set_facecolor(color)

        # adding horizontal grid lines
        for ax in axes:
            ax.yaxis.grid(True)
            ax.set_xlabel('Three separate samples')
            ax.set_ylabel('Observed values')

        plt.show()

    def comparison(self):
        fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(9, 4))

        # Fixing random state for reproducibility
        np.random.seed(19680801)

        # generate some random test data
        all_data = [np.random.normal(0, std, 100) for std in range(6, 10)]

        # plot violin plot
        axes[0].violinplot(all_data,
                           showmeans=False,
                           showmedians=True)
        axes[0].set_title('Violin plot')

        # plot box plot
        axes[1].boxplot(all_data)
        axes[1].set_title('Box plot')

        # adding horizontal grid lines
        for ax in axes:
            ax.yaxis.grid(True)
            ax.set_xticks([y + 1 for y in range(len(all_data))])
            ax.set_xlabel('Four separate samples')
            ax.set_ylabel('Observed values')

        # add x-tick labels
        plt.setp(axes, xticks=[y + 1 for y in range(len(all_data))],
                 xticklabels=['x1', 'x2', 'x3', 'x4'])
        plt.show()


if __name__ == '__main__':
    # plot_by_axes()
    # subplot_demo()
    # stack_plot()
    # sp = ScatterPlotDemo()
    # sp.basic()
    # sp.advanced()
    # hist = HistogramDemo()
    # hist.basic()
    # hist.overlaid_plot()
    # hist.rectangle_hist()
    # bar = BarplotDemo()
    # bar.basic()
    # bar.stacked()
    # bar.errbar()
    bxp = BoxplotDemo()
    bxp.basics()
    bxp.colored()
    bxp.comparison()
