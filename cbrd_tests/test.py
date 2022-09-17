import tensorflow as tf

ro = tf.Variable( tf.random.uniform([5, ], dtype=tf.float32) )
Iext = tf.Variable(1.5, dtype=tf.float32)

with tf.GradientTape(persistent=False) as tape:
    tape.watch(ro)


    last_ro = ro[-1]
    ro_without_last =  ro[:-1]
    last_ro = last_ro + ro_without_last[-1]
    ro_without_last = tf.roll(ro_without_last, 1, axis=0)

    ro_fist = tf.math.reduce_sum(ro)
    ro_fist = tf.reshape(ro_fist, [-1, ])
    last_ro = tf.reshape(last_ro, [-1, ])

    ro = tf.concat([ro_fist, ro_without_last[1:], last_ro ], axis=0)

    firing = ro +  Iext

    grad = tape.gradient(firing, ro)

    print(grad)