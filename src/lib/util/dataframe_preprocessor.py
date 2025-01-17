###########################################################
###############   Preprocessor of Dataframe   #############
###########################################################

import pandas as pd
import numpy as np
import os
import shutil
from sklearn.preprocessing import LabelEncoder
from . import df_ops

class DataframePreprocessor:

    _dataframe  = None
    _output_dir = {} # directories for output
    _col_encoders = {} # {column_name: encoder}
    _col_binners  = {} # {column_name: binner}
    dataframe_encoded = False
    target_feature    = None # feature name of target feature
    class_encoder     = None # label encoder for target feature 
    _from_path         = ""   # path of original data file
        

    def __init__(self, dataframe):
        """        
        dataframe: panda Dataframe 
        """        
        self._dataframe = dataframe
    
    @classmethod
    def dataframe_from_file(self, file_path, **kwargs):
        """
        Args:
            file_path: 

        Return: 
        """
        self._from_path = file_path
        return df_ops.load(file_path)


    
    @classmethod
    def init_from_file(self, file_path, **kwargs):
        """
        file_path: string
        sheetname: index of sheet in file
        """
        dataframe = self.dataframe_from_file(file_path, **kwargs)
        return DataframePreprocessor(dataframe)
        

    def flush_to_disk(self, **kargs):
        """flush updates to disk
        Return: 
        """
        df_ops.dump(self._dataframe, self._from_path, **kwargs)
    

    def dump(self, path = None, **kwargs):
        """save dataframe to file 
        Args:
            path: if None, dump to self._from_path

        Return: 
        """
        if path is None:
            path = self._from_path
        df_ops.dump(self._dataframe, path, **kwargs)


    def peek_head(self):
        """ return head of datafrrame  """
        return self._dataframe.head()


    def set_output_dir(self, output_dir):
        """
        Args:
            output_dir: string of output dir
        """
        if os.path.exists(output_dir): 
            print("{} already existed, removed.".format(output_dir))
            shutil.rmtree(output_dir)

        self._output_dir = { "img": os.path.join(output_dir, "img"), \
                            "data": os.path.join(output_dir, "data") }
        for d in self._output_dir.values():
            os.makedirs(d)
                                                                                                   

    def plot_count_by_feature(self, feature, save=True):
         """
         Args:
             feature: string
             save:    boolean 
         """
         assert feature in self._dataframe.keys(), "{} not a feature for the data!".format(feature)
         ax = plot.plot_count_by_feature(self._dataframe, feature)
         if save:
             save_path = os.path.join(self._output_dir["img"], "feature_count_of_{}.png".format(feature.replace(" ", "-")))
         ax.get_figure().savefig(save_path)
         return ax


    def get_dataframe(self):
        """
        Return: _dataframe 
        """
        return self._dataframe


    def report_shape(self):
        """
        Return: 
        """
        print("Shape of Data: {}".format(tuple(self._dataframe.shape)))


    def remove_rows_from(self, remove_from):
        """
        Args:
            remove_from: int | index of rows to remove from
        """
        old_shape = tuple(self._dataframe.shape)
        self._dataframe.drop(self._dataframe.index[range(remove_from, old_shape[0])], inplace=True)
        new_shape = tuple(self._dataframe.shape)
        print("Shape Updated from {} -> {} | {} Rows Removed.".format(old_shape, new_shape, old_shape[0]- new_shape[0]))

    def remove_cols(self, cols_to_remove, kind="index"):
        """
        Args:
            cols_to_remove: 
                - kind="index": [index of column to remove]
                - kind="name":  [name of column to remove]
            kind: |"index"|"name"|
        """
        old_shape = tuple(self._dataframe.shape)
        if kind=="index": self._dataframe.drop(self._dataframe.columns[cols_to_remove], inplace=True, axis=1)
        else:             self._dataframe.drop(cols_to_remove, inplace=True, axis=1)
        new_shape = tuple(self._dataframe.shape)
        print("Shape Updated from {} -> {} | {} Columns Removed.".format(old_shape, new_shape, old_shape[1] - new_shape[1]))
   

    def filter_rows_by_condition(self, feature, condition):
        """ filter out rows that does not satisfy <condition>
        Args:
            feature:    column name | string
            condition:  lambda function returnning boolean
        """
        old_shape = tuple(self._dataframe.shape)
        self._dataframe = self._dataframe[np.vectorize(condition)(self._dataframe[feature])]
        new_shape = tuple(self._dataframe.shape)
        print("Shape Updated from {} -> {} | {} Rows Removed.".format(old_shape, new_shape, old_shape[0]- new_shape[0]))

    def subframe_except_column(self, except_col):
        """return a sub-dataframe except a certain column
        Args:
            except_col: 

        Return: 
        """
        return self._dataframe.loc[:, self._dataframe.columns != except_col]


    def transform_category(self, feature, rule_dic):
        """
        Args:
            feature:  column name | string
            rule_dic: {old_category: new_category} 
                      if not specified in rule_dic, then keep the original category
        """
        print("Before Transfore: {}".format(self.unique_vals_for_feature(feature)))
        fn = lambda x: rule_dic[x] if x in rule_dic else x
        self._dataframe[feature] = np.vectorize(fn)(self._dataframe[feature])
        print("After Transfore:  {}".format(self.unique_vals_for_feature(feature)))


    def get_subframe_by_condition(self, feature, condition):
        """
        Args:
            feature:    column name | string
            condition:  lambda function returnning boolean

        Return:  dataframe
        """
        return self._dataframe[np.vectorize(condition)(self._dataframe[feature])]


    def unique_vals_for_feature(self, feature):
        """ 
        return unique values for a feature
        Args:
            feature:    column name | string
        Return: [val]
        """
        return self._dataframe[feature].unique().tolist()


    def save_subframes_by_feature(self, feature, kind="csv"):
        """
        save subframes to files for all uniqie values in feature
        Args:
            feature:    column name | string

        Return: [file path]
        """
        paths = []
        for val in self.unique_vals_for_feature(feature):
            subframe = self.get_subframe_by_condition(feature, lambda x: x==val)
            if kind=="csv":
                path = "{}/{}-{}.csv".format(self._output_dir["data"], feature.replace(" ", ""), val)
                subframe.to_csv(path, index=False)
                paths.append(path)
            print("save to file: {}".format(path))


    def get_column_names(self):
        """
        Return: [column_name]
        """
        return self._dataframe.keys().tolist()
    

    def force_column_dtype(self, column, dtype):
        """
        enforce column data type
        Args:
            column:    column name | string
            dtype:   data type - |str, float, int|
        """
        self._dataframe[column] = self._dataframe[column].astype(dtype)


    def feature_vals_dict(self):
        """
        Return: {feature: [unique value]}
        """
        return {f: self.unique_vals_for_feature(f) for f in self.get_column_names()}


    def num_feature_range(self, feature):
        """return (min, max) for dataframe.feature 
        Args:
            feature: 

        Return: 
        """
        vals = self._dataframe[feature]
        vals = [x for x in vals if not np.isnan(x)]
        return (min(vals), max(vals))

    def feature_num_unique_val(self):
        """
        Return: {feature: num of unique values}
        """
        return {f: len(self.unique_vals_for_feature(f)) for f in self.get_column_names()}

    def fillnan(self, val):
        self._dataframe = self._dataframe.fillna(val)

    def encode_column(self, feature):
        """
        Args:
            feature:    column name | string

        Return: 
        """
        try:
            encoder = LabelEncoder()
            encoder.fit(self._dataframe[feature])
            return encoder
        except Exception as e:
            print("Error: {} Does Not Have Consistent Datatype!".format(feature))
            print(e)
            # print(list((x, type(x)) for x in self._dataframe[feature]))
        

    def encode_categorical_cols(self, verbose=False):
        """
        Return: 
        """
        self.dataframe_encoded = True
        for col in self._dataframe.keys():
            if self._dataframe[col].dtype == "object":
                self.force_column_dtype(col, str)
                if verbose: print("Encoding: {}".format(col))
                encoder = self.encode_column(col)

                assert(encoder)
                self._col_encoders[col] = encoder
                self._dataframe[col]    = encoder.transform(self._dataframe[col])


    def decode_categorical_cols(self, verbose=False):
        """
        Return: 
        """
        self.dataframe_encoded = False
        for col, encoder in self._col_encoders.items():
                self._dataframe[col]    = encoder.inverse_transform(self._dataframe[col])
                if verbose: print("Decoding: {}".format(col))


    def convert_to_bins(self, feature, bins):
        """
        Args:
            feature:    column name | string
            bins:       [boundary] 

        Return: 
        """
        self._dataframe[feature] = np.digitize(self._dataframe[feature], bins, right=False)


    def prepare_model_data(self, target_feature):
        """ prepare data for ML modelling 
        Args:
            target_feature: 

        Return: (model_X, model_y) | (dataframe, np array )
        """
        self.target_feature = target_feature
        model_X = self._dataframe.drop([target_feature], inplace=False, axis=1)
        model_y = self._dataframe[target_feature]

        self.class_encoder = LabelEncoder()
        self.class_encoder.fit(model_y)
        # transform class labels to numbers 
        model_y = self.class_encoder.transform(model_y)
        return (model_X, model_y)

    def remove_cols_unless(self, keep_cols):
        """ keep only columns in keep_cols 
        Args:
            keep_cols: 

        Return: 
        """
        self.remove_cols(set(self._dataframe.keys()) - set(keep_cols), kind='name')


    def transform_column(self, column_name, fn):
        """ transform whole column values by fn
        Args:
            column_name: 
            fn: 

        Return: 
        """
        self._dataframe[column_name] = self._dataframe[column_name].apply(fn)


    def filter_rows_by_nonempty_column(self, column_name):
        """filter rows with valu in column as NULL 
        Args:
            column_name: 

        Return: 
        """
        old_shape = tuple(self._dataframe.shape)

        non_empty = self._dataframe[column_name].notnull()
        self._dataframe = self._dataframe[non_empty]

        new_shape = tuple(self._dataframe.shape)
        print("Shape Updated from {} -> {} | {} Rows Removed.".format(old_shape, new_shape, old_shape[0]- new_shape[0]))

    
    def values_for_column(self, column_name):
        """get list of values for a certain column
        Args:
            column_name: 

        Return: 
        """
        return list(self._dataframe[column_name])

    def append_columns(self, column_names, mat, remove=True):
        """append a column
        Args:
            column_name: 
            values: 

        Return: 
        """
        if remove:
            try:
                self.remove_cols(column_names, kind="name")
            except Exception as e:
                pass
        for i, col in enumerate(column_names):
            self.append_column(col, mat[:, i])

    def append_column(self, column_name, values):
        """append a column
        Args:
            column_name: 
            values: 

        Return: 
        """
        try:
            self._dataframe = self._dataframe.join(pd.DataFrame({column_name: values}))
        except Exception as e:
            self._dataframe[column_name] = values

    def update_with_df(self, df):
        """update with another dataframe
        Args:
            df: 

        Return: 
        """
        self._dataframe.update(df)
        
        
    def compress_by_rows(self, dimension_col, bucket_sz, **kwargs):
        """compress dataframe by rows
        Args:
            dimension_col: column name as the dimension
            bucket_sz:     number of rows in each bucket
            **kwargs: 

        Return: 
        """
        dimensions = self.values_for_column(dimension_col)
        sub_df = self.subframe_except_column(dimension_col)
        mat = sub_df.values
        nrows = mat.shape[0]
        new_mat = np.array([np.mean(mat[i: i + bucket_sz], axis = 0)\
                for i in range(0, nrows, bucket_sz)])
        if kwargs.get("round", 0):
            new_mat = np.around(new_mat, kwargs["round"])
        new_dimensions = [dimensions[i] for i in range(0, nrows, bucket_sz)]
        df = df_ops.mat2df(new_mat, list(sub_df.keys()))
        df.insert(0, dimension_col, new_dimensions)
        if kwargs.get("inplace", True):
            self._dataframe = df
        return df

    def value_matrix(self):
        """return the matrix of dataframe value 
        Return: 
        """
        return self._dataframe.as_matrix()
