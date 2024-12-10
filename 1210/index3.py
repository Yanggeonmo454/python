import seaborn as sns
import matplotlib.pyplot as plt

penguins = sns.load_dataset("penguins")

sns.barplot(x='species', y='body_mass_g', data=penguins)
plt.show()

sns. scatterplot(x='bill_length_mm', y='bill_depth_mm',
                 data=penguins, hue='species')
plt.show()

sns.violinplot(x='island', y='body_mass_g', data=penguins)
plt.show()
