import pandas as pd


def judge_type(x, ind_rule_dict):
    size = ['大型', '中型', '小型', '微型']
    if x[0] in ind_rule_dict:
        rules = ind_rule_dict[x[0]]
        threshold1 = rules[0]
        threshold2 = rules[1]
        threshold3 = rules[2]
            
        if sum(pd.Series([threshold1, threshold2, threshold3]).isna()) == 1:
        
            if pd.Series(threshold3).any() == False:
                if (x[1]/10000 >= threshold1[0]) & (x[2] >= threshold2[0]):
                    return size[0]
                elif (threshold1[0] <= x[1]/10000 <= threshold1[1]) & (threshold2[0] <= x[2] <= threshold2[1]):
                    return size[1]
                elif (threshold1[1] <= x[1]/10000 <= threshold1[2]) & (threshold2[1] <= x[2] <= threshold2[2]):
                    return size[2]
                else:
                    return size[3]
            
            if pd.Series(threshold2).any() == False:
                if (x[1]/10000 >= threshold1[0]) & (x[3] >= threshold3[0]):
                    return size[0]
                elif (threshold1[0] <= x[1]/10000 <= threshold1[1]) & (threshold3[0] <= x[3] <= threshold3[1]):
                    return size[1]
                elif (threshold1[1] <= x[1]/10000 <= threshold1[2]) & (threshold3[1] <= x[3] <= threshold3[2]):
                    return size[2]
                else:
                    return size[3]
            
            if pd.Series(threshold1).any() == False:
                if (x[2] >= threshold2[0]) & (x[3] >= threshold2[0]):
                    return size[0]
                elif (threshold2[0] <= x[2] <= threshold2[1]) & (threshold3[0] <= x[3] <= threshold3[1]):
                    return size[1]
                elif (threshold2[1] <= x[2] <= threshold2[2]) & (threshold3[1] <= x[3] <= threshold3[2]):
                    return size[2]
                else:
                    return size[3]
            
        else:
            if x[2] >= 20000:
                return size[0]
            elif 500 <= x[2] < 20000:
                return size[1]
            elif 50 <= x[2] < 500:
                return size[2]
            else:
                return size[3]
    else:
        if (x[1]/10000) >= 300:
            return size[0]
        elif 100 <= (x[1]/10000) < 300:
            return size[1]
        elif 10 <= (x[1]/10000) < 100:
            return size[2]
        else:
            return size[3]
