import seaborn as sns
import matplotlib.pyplot as plt

if __name__=="__main__":

    # Incarcare set de date Iris
    iris = sns.load_dataset('iris')

    # 1. Pairplot complet iris.
    sns.pairplot(iris, hue='species', diag_kind='kde')
    plt.suptitle('Pairplot — dataset Iris', y=1.02)
    plt.savefig("assets/iris_pairplot_analiza.png", dpi=150, bbox_inches='tight')

    # 2. Set 1x4 Violinplots.
    fig, axes = plt.subplots(1, 4, figsize=(12, 5))
    fig.suptitle('Tipuri de grafice Violinplot - Dataset Iris', fontsize=16, fontweight='bold')

    sns.violinplot(data=iris, x='species', y='sepal_length',hue='species',split='false', ax=axes[0])
    sns.violinplot(data=iris, x='species', y='sepal_width',hue='species',split='false', ax=axes[1])
    sns.violinplot(data=iris, x='species', y='petal_length',hue='species',split='false', ax=axes[2])
    sns.violinplot(data=iris, x='species', y='petal_width',hue='species',split='false', ax=axes[3])

    plt.savefig("assets/iris_violin_analiza.png", dpi=150, bbox_inches='tight')

    axes[0].set_title('Violinplot — sepal_length')
    axes[1].set_title('Violinplot — sepal_width')
    axes[2].set_title('Violinplot — petal_length')
    axes[3].set_title('Violinplot — petal_width')

    plt.show()

