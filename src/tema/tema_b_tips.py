import seaborn as sns

if __name__=="__main__":
    tips = sns.load_dataset('tips')

    print(f"Dimensiune: {tips.shape[0]} linii × {tips.shape[1]} coloane")   
    print(f"\nTipuri de date:\n{tips.dtypes}")
    print("\n=== Statistici descriptive ===")
    print(tips.describe().round(2))

    avg_tip = tips.groupby(['day', 'sex']).mean(numeric_only=True)
    print("\n", avg_tip['tip'])

    copie = tips.copy()
    copie['procent_bacsis'] = (copie['tip'] / copie['total_bill']) * 100

    the_most_generous = copie.nlargest(5, 'procent_bacsis')
    print('\n', the_most_generous)

    meals_served = tips.groupby(['day', 'smoker'], observed=False).size()
    print('\n', meals_served)