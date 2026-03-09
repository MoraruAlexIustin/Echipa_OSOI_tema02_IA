import seaborn as sns
import matplotlib.pyplot as plt

if __name__=="__main__":
    tips = sns.load_dataset('tips')

    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    fig.suptitle('Tipuri de grafice Matplotlib — Dataset Tips', fontsize=16, fontweight='bold')

    # --- Scatter — Total_bill vs. tip, colorat per sex ---
    culori = {'Female': '#e74c3c', 'Male': '#3498db'}
    for sex_cat, culoare in culori.items():
        subset = tips[tips['sex'] == sex_cat]
        axes[0, 0].scatter(subset['total_bill'], subset['tip'],
                            label=sex_cat, color=culoare, alpha=0.7, s=50)
        
    axes[0, 0].set_title('Total bill vs. Tip (by Sex)')
    axes[0, 0].set_xlabel('Total bill ($)')
    axes[0, 0].set_ylabel('Tip ($)')
    axes[0, 0].legend()

    # --- Boxplot — distribuția total_bill per day, în ordinea Thur → Sun ---
    sns.boxplot(data=tips, x='day', y='total_bill', order=['Thur', 'Fri', 'Sat', 'Sun'], ax=axes[0, 1])
    axes[0, 1].set_title('Distribuția total_bill per zi')
    axes[0, 1].set_xlabel('Zi')
    axes[0, 1].set_ylabel('Total_bill ($)')

    # --- Histogramă cu KDE - distributia tip ---
    sns.histplot(data=tips, x='tip', hue='time', kde=True, bins=15, ax=axes[1, 0])
    axes[1, 0].set_title('Distributia bacsis')
    axes[1, 0].set_xlabel('Bacsis ($)')

    # Subplot 3: Rata per sex și clasă — parametrul hue colorează barele per sex
    sns.barplot(data=tips, x='day', y='tip',  errorbar='ci', order=['Thur', 'Fri', 'Sat', 'Sun'], 
                palette='Blues_d', ax=axes[1, 1])
    axes[1, 1].set_title('Bacsisul mediu per zi')
    axes[1, 1].set_xlabel('Ziua saptamanii')
    axes[1, 1].set_ylabel('Bacsis mediu ($)')

    plt.tight_layout()
    plt.show()
