import numpy as np

def classification_metrics(y_true, y_pred, average="micro", pos_label=1):
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)
    
    accuracy = float(np.mean(y_true == y_pred))
    
    if average == "binary":
        tp = np.sum((y_true == pos_label) & (y_pred == pos_label))
        fp = np.sum((y_true != pos_label) & (y_pred == pos_label))
        fn = np.sum((y_true == pos_label) & (y_pred != pos_label))
        
        precision = float(tp / (tp + fp)) if (tp + fp) > 0 else 0.0
        recall = float(tp / (tp + fn)) if (tp + fn) > 0 else 0.0
        f1 = float(2 * precision * recall / (precision + recall)) if (precision + recall) > 0 else 0.0
        
        return {"accuracy": accuracy, "precision": precision, "recall": recall, "f1": f1}
        
    classes = np.unique(np.concatenate([y_true, y_pred]))
    n_classes = len(classes)
    
    tp_cls = np.zeros(n_classes)
    fp_cls = np.zeros(n_classes)
    fn_cls = np.zeros(n_classes)
    support = np.zeros(n_classes)
    
    for idx, cls in enumerate(classes):
        tp_cls[idx] = np.sum((y_true == cls) & (y_pred == cls))
        fp_cls[idx] = np.sum((y_true != cls) & (y_pred == cls))
        fn_cls[idx] = np.sum((y_true == cls) & (y_pred != cls))
        support[idx] = np.sum(y_true == cls)
        
    if average == "micro":
        tp_sum = np.sum(tp_cls)
        fp_sum = np.sum(fp_cls)
        fn_sum = np.sum(fn_cls)
        
        precision = float(tp_sum / (tp_sum + fp_sum)) if (tp_sum + fp_sum) > 0 else 0.0
        recall = float(tp_sum / (tp_sum + fn_sum)) if (tp_sum + fn_sum) > 0 else 0.0
        f1 = float(2 * precision * recall / (precision + recall)) if (precision + recall) > 0 else 0.0

    elif average in ("macro", "weighted"):
        prec_denom = tp_cls + fp_cls
        rec_denom = tp_cls + fn_cls
        
        prec_cls = np.where(prec_denom > 0, tp_cls / prec_denom, 0.0)
        rec_cls = np.where(rec_denom > 0, tp_cls / rec_denom, 0.0)
        
        f1_denom = prec_cls + rec_cls
        f1_cls = np.where(f1_denom > 0, 2 * prec_cls * rec_cls / f1_denom, 0.0)
        
        if average == "macro":
            precision = float(np.mean(prec_cls))
            recall = float(np.mean(rec_cls))
            f1 = float(np.mean(f1_cls))
        else:
            total_support = np.sum(support)
            if total_support > 0:
                precision = float(np.sum(prec_cls * support) / total_support)
                recall = float(np.sum(rec_cls * support) / total_support)
                f1 = float(np.sum(f1_cls * support) / total_support)
            else:
                precision, recall, f1 = 0.0, 0.0, 0.0
                
    else:
        raise ValueError(f"Invalid averaging option strategy: {average}")
        
    return {"accuracy": accuracy, "precision": precision, "recall": recall, "f1": f1}
    pass