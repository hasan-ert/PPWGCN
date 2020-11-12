import tensorflow as tf

def masked_softmax_cross_entropy(preds, labels, mask):
    """Softmax cross-entropy loss with masking."""
    loss = tf.nn.softmax_cross_entropy_with_logits(logits=preds, labels=labels)
    mask = tf.cast(mask, dtype=tf.float32)
    mask /= tf.reduce_mean(mask)
    loss *= mask
    return tf.reduce_mean(loss)

def weight_masked_softmax_cross_entropy(preds, labels, mask, weight):
    class_weights = tf.constant(weight, dtype=tf.float32)
    print(class_weights.shape)
    class_weights = tf.expand_dims(class_weights, 0)
    weights = tf.reduce_sum(class_weights * labels, axis = 1)
    unweighted_losses = tf.nn.softmax_cross_entropy_with_logits(logits=preds, labels=labels)
    weighted_losses = unweighted_losses * weights
    mask = tf.cast(mask, dtype=tf.float32)
    mask /= tf.reduce_mean(mask)
    weighted_losses *= mask
    return tf.reduce_mean(weighted_losses)

def masked_accuracy(preds, labels, mask):
    """Accuracy with masking."""
    correct_prediction = tf.equal(tf.argmax(preds, 1), tf.argmax(labels, 1))

    accuracy_all = tf.cast(correct_prediction, tf.float32)
    mask = tf.cast(mask, dtype=tf.float32)
    mask /= tf.reduce_mean(mask)
    accuracy_all *= mask
    return tf.reduce_mean(accuracy_all)

def calculate_f_score(right, predict, class_num):
    predict = list(predict)
    right = list(right)
    last = []
    result = []
    for i in range(class_num):
        result.append([0, 0, 0])
    assert len(right) == len(predict)
    #print("precision/recall/F-measure")
    last.append('precision')
    last.append('recall')
    last.append('F-measure')
    for i in range(len(right)):
        #print(right[i],predict[i])
        result[right[i]][1] += 1
        result[predict[i]][2] += 1
        if right[i] == predict[i]:
            result[predict[i]][0] += 1
    f_score = []
    average_p = 0
    average_r = 0
    average_f_score = 0
    for i in range(class_num):
        p = result[i][0] / (result[i][2] or 1)
        r = result[i][0] / (result[i][1] or 1)
        f_score.append((2*p*r) / ((p+r) or 1))
        average_p += p
        average_r += r
        average_f_score += (2*p*r) / ((p + r) or 1)
        #print(str(round(p, 4)) + '\t' +  str(round(r, 4)) + '\t' + str(round(f_score[i], 4)))
        last.append(str(round(p, 4)))
        last.append(str(round(r, 4)))
        last.append(str(round(f_score[i], 4)))
    average_p = str(round(average_p / class_num, 4))
    average_r = str(round(average_r / class_num, 4))
    average_f_score = str(round(average_f_score / class_num, 4))
    last.append(average_p)
    last.append(average_r)
    last.append(str(average_f_score))
    #print(average_p + '\t' + average_r + '\t' + average_f_score)
    print("average_f_score:" + average_f_score)
    return last
