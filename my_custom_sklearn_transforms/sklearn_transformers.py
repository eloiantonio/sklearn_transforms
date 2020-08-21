from sklearn.base import BaseEstimator, TransformerMixin


# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        # Retornamos um novo dataframe sem as colunas indesejadas
        return data.drop(labels=self.columns, axis='columns')

class AddNotasMedias(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        # Retornamos um novo dataframe com o dado NOTA_EXA
        #data_1 = data.assign(NOTA_EXA = (X["NOTA_DE"] + X["NOTA_EM"])/2.0)
        #data_2 = data_1.assign(NOTA_HUM = (X["NOTA_MF"] + X["NOTA_GO"])/2.0)
        data_3 = data.assign(NOTA_GERAL = (X["NOTA_DE"] + X["NOTA_MF"])/2.0)
        data_final = data_3.assign(DIFERENCA_NOTA = X["NOTA_DE"] - X["NOTA_MF"])
        return data_final
