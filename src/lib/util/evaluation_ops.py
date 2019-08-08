from collections import namedtuple

EvalResult = namedtuple("EvalResult", 
        ["Precision", "Recall", "FalseNegatives", "FalsePositives"])

def print_eval_result(result : EvalResult):
    print("Precision:      {:.1f}%".format(result.Precision * 100))
    print("Recall:         {:.1f}%".format(result.Recall * 100))
    print("FalseNegatives: {}".format(result.FalseNegatives))
    print("FalsePositives: {}".format(result.FalsePositives))
