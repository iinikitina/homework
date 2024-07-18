import pandas as pd

# Создаем DataFrame
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Применяем one-hot кодирование
one_hot_encoded = pd.concat([data, pd.get_dummies(data['whoAmI'], prefix='whoAmI')], axis=1).drop(['whoAmI'], axis=1)

# Первые несколько строк one-hot закодированного DataFrame
print(one_hot_encoded.head())
