# SOURCE: https://gist.github.com/vikramsoni2/3293b5dab320ba6d67eb8eed415e1c04
# Multiclass confusion matrix using Seaborn heatmap - clean style

y_true = le.inverse_transform(y_valid)
y_pred = le.inverse_transform(y_valid_pred_lr)

from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

data = confusion_matrix(y_true, y_pred)
df_cm = pd.DataFrame(data, columns=np.unique(y_true), index=np.unique(y_true))
df_cm.index.name = 'Actual'
df_cm.columns.name = 'Predicted'

f, ax = plt.subplots(figsize=(15, 15))
cmap = sns.cubehelix_palette(light=1, as_cmap=True)
sns.heatmap(df_cm, cbar=False, annot=True, cmap=cmap, square=True, fmt='.0f',
            annot_kws={'size': 10})
plt.title('Actuals vs Predicted')
plt.show()
