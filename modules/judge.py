import pandas as pd


def judge(df, group, how, logi, result, df_raw, merge_key):
    """此函数为基于上一层触发和逻辑关系判断下一层触发

    Args:
        df (DataFrame): 基于什么Dataframe
        group (list): 分组依据
        how (str): 严重触发还是普通触发
        logi (str): 逻辑关系列
        result (str): 结果名列
        df_raw (DataFrame): 合并使用的原始Dataframe
        merge_key (_type_): 与原始Dataframe合并的键

    Returns:
        DataFrame: 返回的合并结果
    """
    
    df2 = df.groupby(group).apply(lambda x: x[how].all() if x[logi].iloc[0] == 'AND' else x[how].any()).reset_index().rename(columns={0:result})
    entity2 = df_raw.copy()
    entity2 = pd.merge(entity2, df2, on=merge_key)
    
    return entity2